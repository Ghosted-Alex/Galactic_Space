# Galactic Space Reborn
# Copyright (c) Ghosted Alex 2026
# Made under the MIT license: https://opensource.org/license/mit

# General Imports
import os
import random
import subprocess
import pygame

pygame.init()

# Source Imports
import src.assets as assets
import config
import src.entity as entity
import src.powerup as powerup
import src.bullet as bullet
import src.update as update
import src.ui as ui

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

def draw_game_over_ui(surface):
    config.game_over_ui_shown = True

    # 1. Create a temporary surface with the same size as the screen
    # pygame.SRCALPHA makes it capable of transparency
    overlay = pygame.Surface((config.Screen.Size.w, config.Screen.Size.h), pygame.SRCALPHA)
    
    # 2. Fill it with a semi-transparent color (R, G, B, Alpha)
    # Alpha 128 is 50% transparent (0 is invisible, 255 is solid)
    overlay.fill((0, 0, 0, 150)) 
    
    # 3. Blit the overlay onto the main screen
    surface.blit(overlay, (0, 0))

    # 4. Let the game know that the game over UI was shown
    config.game_over_ui_shown = True

    if config.score > config.high_score:
        config.high_score = config.score
    else:
        with open(config.HIGH_SCORE_FILE, "r") as file:
            config.high_score = int(file.read().strip())

    # 5. Create text lines
    if config.score < config.high_score:
        score_go_str = assets.monocraft.render(f"Score: {config.score}", True, (255, 255, 255))
        print("Regular Score")
    else:
        score_go_str = assets.monocraft.render(f"New High Score!", True, (255, 180, 0))
        print("")
    hi_score_go_str = assets.monocraft.render(f"High Score: {config.high_score}", True, (255, 255, 255))

    ins_restart = assets.monocraft.render(f"Press \"{pygame.key.name(config.Keybinds.restart_key, False)}\" to Restart Game", True, (255, 255, 255))

    # 6. Draw the UI on top
    surface.blit(assets.Textures.UI.game_over, (318, 225))
    surface.blit(score_go_str, (318, 275))
    surface.blit(hi_score_go_str, (318, 315))

    surface.blit(ins_restart, (215, 500))


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

    if config.error != 0:
        config.Game.running = False

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
                    if event.key == pygame.K_KP_PLUS:
                        if config.score < 10:
                            config.score += 10
                        else:
                            config.score += config.score * 10
                    if event.key == pygame.K_1:
                        game_over()
                if event.key == pygame.K_SPACE or event.key == pygame.K_z:
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
        
        if config.delay == random.randint(1, 60): # Trigger exactly halfway through the enemy spawn cycle
            chance = random.randint(0, 99)
            print(f"Roll (%): {chance}")

            # Check for Health
            if player.health <= 95 and 0 <= chance <= 15:
                print("Wrench Powerup Summoned!")
                new_powerup = powerup.Spawn(random.randint(48, 874), -75, 0)
                powerups.append(new_powerup)
                
            # Check for Ammunition (Independent or Else-If)
            if player.energy <= 95 and 16 <= chance <= 50:
                print("Ammo Powerup Summoned!")
                new_powerup = powerup.Spawn(random.randint(48, 874), -75, 2)
                powerups.append(new_powerup)
            
            if config.powerup_active == False:
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

        ui.show_panel_ui(SCR, player=player)

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
            draw_game_over_ui(SCR)

    pygame.display.flip()


print(f"Exited with error code: {config.error}")
if config.error_text != "":
    print(f"[{config.datetime.datetime.now()}] CRITICAL: Task failed in: {config.error_origin.name}")
    print(f"Code: {config.error} | Message: {config.error_text}")

pygame.quit()
