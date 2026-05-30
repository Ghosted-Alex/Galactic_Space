"User Interface Module"

from . import assets
import config
import pygame

def draw_game_over_ui(screen):
    config.game_over_ui_shown = True

    # 1. Create a temporary screen with the same size as the screen
    # pygame.SRCALPHA makes it capable of transparency
    overlay = pygame.Surface((config.Screen.Size.w, config.Screen.Size.h), pygame.SRCALPHA)
    
    # 2. Fill it with a semi-transparent color (R, G, B, Alpha)
    # Alpha 128 is 50% transparent (0 is invisible, 255 is solid)
    overlay.fill((0, 0, 0, 150)) 
    
    # 3. Blit the overlay onto the main screen
    screen.blit(overlay, (0, 0))

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
        print("High Score")
    hi_score_go_str = assets.monocraft.render(f"High Score: {config.high_score}", True, (255, 255, 255))

    ins_restart = assets.monocraft.render(f"Press \"{pygame.key.name(config.Keybinds.restart_key, False)}\" to Restart Game", True, (255, 255, 255))

    # 6. Draw the UI on top
    screen.blit(assets.Textures.UI.game_over, (318, 225))
    screen.blit(score_go_str, (318, 275))
    screen.blit(hi_score_go_str, (318, 315))

    screen.blit(ins_restart, (215, 500))

def draw_panel_ui(screen, player):

    # Replace that whole 'for i in range(2)' block with this:
    if config.blink_timer < 60:
        # This checks if the timer is in the first or second half of a 30-frame cycle
        if (config.blink_timer // 15) % 2 == 0:
            config.BACKGROUND_AMMO_COLOR = (166, 51, 51) # Red
        else:
            config.BACKGROUND_AMMO_COLOR = (15, 15, 15)  # Dark
    else:
        config.BACKGROUND_AMMO_COLOR = (15, 15, 15) # Default Dark
    
    if config.health_blink_timer < 60:
        # This checks if the timer is in the first or second half of a 30-frame cycle
        if (config.health_blink_timer // 15) % 2 == 0:
            config.HEALTH_COLOR_HIGH = (255, 255, 255) # White
            config.HEALTH_COLOR_LOW = (255, 255, 255) # White
            config.HEALTH_COLOR_MED = (255, 255, 255) # White
            config.HEALTH_COLOR_DRAIN = (135, 242, 255) # Drain Color (Cyan)
            config.BACKGROUND_HEALTH_COLOR = (204, 53, 53) # Red
        else:
            if player.invincible == True and config.powerup_active == True:
                config.HEALTH_COLOR_HIGH = (219, 157, 0) # Invincible Health Color (Gold)
            else:
                config.HEALTH_COLOR_HIGH = (50, 168, 82) # High Health Color (Green)
            config.HEALTH_COLOR_MED = (255, 255, 0) # Medium Health Color (Yellow)
            config.HEALTH_COLOR_LOW = (255, 0, 0) # Low Health Color (Red)
            config.HEALTH_COLOR_DRAIN = (135, 242, 255) # Drain Color (Cyan)
            config.BACKGROUND_HEALTH_COLOR = (15, 15, 15)
    else:
        if player.invincible == True and config.powerup_active == True:
            config.HEALTH_COLOR_HIGH = (219, 157, 0) # Invincible Health Color (Gold)
        else:
            config.BACKGROUND_HEALTH_COLOR = (15, 15, 15)
            config.HEALTH_COLOR_HIGH = (50, 168, 82) # High Health Color (Green)
            config.HEALTH_COLOR_MED = (255, 255, 0) # Medium Health Color (Yellow)
            config.HEALTH_COLOR_LOW = (166, 51, 51) # Low Health Color (Red)
            config.HEALTH_COLOR_DRAIN = (135, 242, 255) # Drain Color (Cyan)

    timer_str = assets.monocraft.render(f"{config.powerup_type_text}: {config.powerup_timer}", True, (255,255,255))
    score_str = assets.monocraft.render(f"SC: {config.score}", True, (255,255,255))
    high_score_str = assets.monocraft.render(f"HI: {config.high_score}", True, (255,255,255))

    screen.blit(assets.Textures.UI.panel_01, (0, config.Screen.Size.h-45))
    screen.blit(assets.Textures.UI.panel_02, (config.Screen.Size.w-246, config.Screen.Size.h-195))

    # Modifies the X position of score and high score when a new digit is reached, like if you go from 9 to 10
    text_width = score_str.get_width()
    margin = 20
    score_x_pos = config.Screen.Size.w - text_width - margin

    text_width = high_score_str.get_width()
    margin = 20
    hi_x_pos = config.Screen.Size.w - text_width - margin

    screen.blit(score_str, (score_x_pos, 20+config.Screen.Size.h-187))
    screen.blit(high_score_str, (hi_x_pos, 87+config.Screen.Size.h-187))

    # pygame.draw.rect(screen, (51, 255, 51), self.rect, 1)
    pygame.draw.rect(screen, config.BACKGROUND_HEALTH_COLOR, (15, 656, 400, 25))

    pygame.draw.rect(screen, config.HEALTH_COLOR_DRAIN, (15, 656, player.health_drain*4, 25))
    
    if player.health > 50:
        pygame.draw.rect(screen, config.HEALTH_COLOR_HIGH, (15, 656, player.health*4, 25))
    if 50 >= player.health > 25:
        pygame.draw.rect(screen, config.HEALTH_COLOR_MED, (15, 656, player.health*4, 25))
    if player.health <= 25:
        pygame.draw.rect(screen, config.HEALTH_COLOR_LOW, (15, 656, player.health*4, 25))

    if player.health_drain > player.health:
        player.health_drain -= .1
    elif player.health_drain < player.health:
        player.health_drain = player.health

    # 1. Background Bar (The gray slot)
    # Starts at 507, width 400 (507 + 400 = 907)
    pygame.draw.rect(screen, config.BACKGROUND_AMMO_COLOR, (507, 656, 400, 25))

    # 2. The Draining Logic
    # We calculate the width first
    energy_width = player.energy * 4

    # To make it "reverse," we push the X-coordinate forward by the missing amount
    # 507 + (400 - energy_width)
    reverse_x = 507 + (400 - energy_width)

    # 3. Draw the Energy Bar (Yellow)
    if player.energy > 0:
        pygame.draw.rect(screen, config.AMMO_COLOR, (reverse_x, 656, energy_width, 25))

    if player.health > 100:
        player.health = 100
    if player.energy > 100:
        player.energy = 100

    if config.powerup_timer > 0:
        if config.debug:
            screen.blit(timer_str, (20, 20))
            print(config.powerup_timer)