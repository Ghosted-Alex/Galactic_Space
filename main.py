# Galactic Space Reborn
# Copyright (c) Ghosted Alex 2026
# Made under the MIT license: https://opensource.org/license/mit

# General Imports
import os
import pathlib
import random
import subprocess
import pygame
import configparser

pygame.init()

# Source Imports
import config

from src import assets
from src import entity
from src import powerup
from src import bullet
from src import update
from src import ui
from src import controls

def load_settings(settings_path=pathlib.Path(f"{config.WIN_PATH}/settings.ini")):
    parser = configparser.ConfigParser()
    parser.read(settings_path)
    
    # Pre-computed map for speed
    key_map = {attr[2:].lower(): getattr(pygame, attr) for attr in dir(pygame) if attr.startswith("K_")}
    
    for section in parser.sections():
        if hasattr(config.KeyBinds, section):
            category = getattr(config.KeyBinds, section)
            for key, value in parser.items(section):
                # Look up the key constant
                # (You might need a small mapping function here to handle 'kp_plus' vs 'plus')
                key_const = key_map.get(value.lower())
                if key_const:
                    setattr(category, key, key_const)

def initialize():
    global FPS, SCR
    
    FPS = pygame.time.Clock()

    SCR = pygame.display.set_mode((config.Screen.Size.w, config.Screen.Size.h))

    pygame.display.set_caption(config.Game.title)

    return FPS, SCR

player = entity.Player(config.Screen.Size.w / 2 - 20, config.Screen.Size.h / 2 - 20)# Instead of manual math:
player_rect = player.texture.get_rect(center=(config.Screen.Size.w / 2, config.Screen.Size.h / 2))
player.x, player.y = player_rect.topleft

bullet_normal = bullet.Normal(player.x+28, player.y)

a1 = entity.Enemy(random.randint(16, 906), -5, assets.Textures.Enemy.enemy0, 0)

enemies = []
bullets = []
powerups = []

def game_over():
    print("Game Over!")
    assets.Sounds.player_death.play()
    config.game_over = True
    if config.score == config.high_score:
        config.high_score = config.score
        with open(config.HIGH_SCORE_FILE, "w") as file:
            file.write(str(config.high_score))
        print("High Score Saved!")

if not config.HIGH_SCORE_FILE_EXISTS:
    with open(config.HIGH_SCORE_FILE, "w") as file:
        file.write(str(config.high_score))
else:
    with open(config.HIGH_SCORE_FILE, "r") as file:
        config.high_score = int(file.read().strip())

FPS, SCR = initialize()

while config.Game.running:
    FPS.tick(60)

    config.frame += 1

    if config.game_over == False:
        if config.blink_timer < 60:
            config.blink_timer += 1
        
        if config.health_blink_timer < 60:
            config.health_blink_timer += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.Game.running = False
            
            # Check for the initial key press here
            if event.type == pygame.KEYDOWN:
                if config.debug:
                    if controls.single_press(event, config.KeyBinds.Debug.numpad_plus):
                        if config.score < 10:
                            config.score += 10
                        else:
                            config.score += config.score * 10
                    if controls.single_press(event, config.KeyBinds.Debug.numrow_1):
                        game_over()
                if controls.single_press(event, config.KeyBinds.Gameplay.shoot):
                    if config.game_over == False:
                        # Create the bullet at the player's current position
                        if player.energy > 0:
                            new_bullet = bullet.Normal(player.rect.centerx, player.rect.top)
                            bullets.append(new_bullet)
                            assets.Sounds.player_shoot.play()
                            player.energy -= 5
                        else:
                            config.blink_timer = 0
                            
                if event.key == pygame.K_F12:
                    config.debug = not config.debug

        if not config.Game.running:
            break

        keys = pygame.key.get_pressed()

        # RENDERING
        # Inside your "RENDERING" section in main.py
        # For Rendering stuff ALWAYS put rendering functionality between SCR.fill() and pygame.display.flip()
        SCR.fill((0, 0, 0))

        # Updates
        update.update_entities(enemies=enemies, bullets=bullets, powerups=powerups, player=player, screen=SCR)

        player.handle_input(keys)
        player.draw(SCR)

        config.delay -= 1
        if config.delay < 0:
            config.delay = 60
        
        if config.delay == 0:
            # Create a new enemy and ADD it to the list instead of overwriting
            new_enemy = entity.Enemy(random.randint(48, 874), -75, assets.Textures.Enemy.enemy0, 0)
            enemies.append(new_enemy)
        
        if config.delay == random.randint(1, 60): # Trigger randomly within the 60 frames per second
            chance = random.randint(0, 99)
            print(f"Roll (%): {chance}")

            # Check for Health
            if player.health <= 95 and 0 <= chance <= 15:
                print("Wrench Powerup Summoned!")
                new_powerup = powerup.Spawn(random.randint(48, 874), -75, 0)
                powerups.append(new_powerup)
                
            # Check for Ammunition
            elif player.energy <= 95 and 16 <= chance <= 50:
                print("Ammo Powerup Summoned!")
                new_powerup = powerup.Spawn(random.randint(48, 874), -75, 2)
                powerups.append(new_powerup)
            
            # Check for Active Powerup
            elif config.powerup_active == False:
                # Check for 5% Chance, regardless of health and ammo
                if 50 <= chance <= 55:
                    print("Power Wrench Powerup Summoned!")
                    new_powerup = powerup.Spawn(random.randint(48, 874), -75, 1)
                    powerups.append(new_powerup)
                    
        if config.delay == 0:
            if config.powerup_timer > 0:
                config.powerup_timer -= 1
        
        if config.powerup_timer <= 0 and config.powerup_active == True:
            if config.powerup_type == 0:
                config.health_blink_timer = 0
                config.powerup_active = False
                player.invincible = False

        if player.health <= 0:
            game_over()

        # This ensures the score never exceeds 999,999
        config.score = min(config.score, 999999)
        config.high_score = min(config.high_score, 999999)

        ui.draw_panel_ui(SCR, player=player)

    else:
        # This runs when the game is over
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.Game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Example: Restart game
                    # Reset your variables here
                    config.game_over = False
                    config.game_over_ui_shown = False
                    player.health = 100
                    enemies.clear()

        if config.game_over_ui_shown == False:
            SCR.blit(assets.Textures.UI.panel_01, (0, config.Screen.Size.h-45))

            # pygame.draw.rect(surface, (51, 255, 51), self.rect, 1)
            pygame.draw.rect(SCR, config.BACKGROUND_HEALTH_COLOR, (15, 656, 400, 25))

            pygame.draw.rect(SCR, config.HEALTH_COLOR_DRAIN, (15, 656, player.health_drain*4, 25))

            if player.health > 50:
                pygame.draw.rect(SCR, config.HEALTH_COLOR_HIGH, (15, 656, player.health*4, 25))
            if 50 >= player.health > 25:
                pygame.draw.rect(SCR, config.HEALTH_COLOR_MED, (15, 656, player.health*4, 25))
            if player.health <= 25:
                pygame.draw.rect(SCR, config.HEALTH_COLOR_LOW, (15, 656, player.health*4, 25))
            if player.health <= 0:
                game_over()

            if player.health_drain > player.health:
                player.health_drain -= .1
            elif player.health_drain < player.health:
                player.health_drain = player.health

            # 1. Background Bar (The gray slot)
            # Starts at 507, width 400 (507 + 400 = 907)
            pygame.draw.rect(SCR, config.BACKGROUND_AMMO_COLOR, (507, 656, 400, 25))

            # 2. The Draining Logic
            # We calculate the width first
            energy_width = player.energy * 4

            # To make it "reverse," we push the X-coordinate forward by the missing amount
            # 507 + (400 - energy_width)
            reverse_x = 507 + (400 - energy_width)

            # 3. Draw the Energy Bar (Yellow)
            if player.energy > 0:
                pygame.draw.rect(SCR, config.AMMO_COLOR, (reverse_x, 656, energy_width, 25))

            # Draw the transparent GUI
            ui.draw_game_over_ui(screen=SCR)

    pygame.display.flip()

pygame.quit()
