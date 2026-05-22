"Update Module"

import config
from . import assets
import pygame

def update_entities(enemies, bullets, powerups, player, screen):
    for e in enemies[:]:
                e.move()    
                e.update()
    
                if e.y > config.Screen.Size.h:
                    enemies.remove(e)
                    continue
                
                # Check Bullet Collision
                for b in bullets[:]:
                    if e.rect.colliderect(b.rect):
                        assets.Sounds.entity_damage.play()
                        if e in enemies: enemies.remove(e)
                        if b in bullets: bullets.remove(b)
                        config.score += 1
                        break # Enemy is dead, stop checking bullets for it
                    
                # Check Player Collision
                if e.rect.colliderect(player.rect):
                    config.health_blink_timer = 0
    
                    assets.Sounds.entity_damage.play()
    
                    if player.invincible == False:
                        if config.difficulty == 0:
                            player.health -= 10
                        else:
                            player.health -= 15
    
                    if e in enemies: enemies.remove(e)
    
                    if player.invincible == True:
                        config.score += 1
    
                e.draw(screen) # Draw it here
            
    for b in bullets[:]: # [:] creates a copy so we can safely remove items
        b.update()
        b.draw(screen)
        
        # Optimization: Delete bullet if it leaves the Screen
        if b.rect.bottom < 0:
            bullets.remove(b)
    for p in powerups[:]:
        p.move()    
        p.update()
    
        if p.y > config.Screen.Size.h:
            powerups.remove(p)
            continue
        
        # Check player Collision
        if p.rect.colliderect(player.rect):
            if p.type == 0:
                config.health_blink_timer = 0
                if player.health < 100:
                    if config.difficulty == 0:
                        player.health += 10
                    else:
                        player.health += 5
            if p.type == 2:
                if player.energy < 100:
                    if config.difficulty == 0:
                        player.energy += 10
                    else:
                        player.energy += 5
            if p.type == 1:
                config.health_blink_timer = 0
                if player.health < 100:
                    player.health = 100
                config.powerup_timer = 16
                player.invincible = True
                config.powerup_active = True
                assets.load_music(assets.Music.invincibility, "wav")
                pygame.mixer.music.play()
                config.powerup_type_text = "Invincibility"
                
    
            if p in powerups: powerups.remove(p)
    
        p.draw(screen) # Draw it here