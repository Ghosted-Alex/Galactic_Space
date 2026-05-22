"Module for Assets"

import pathlib
import pygame
import config

pygame.mixer.init()

# -------------------------------------
monocraft = pygame.font.Font(f"{config.WIN_PATH}/assets/fonts/Monocraft.ttf", 30)
class RawTextures:
    """Base Class for Unscaled Textures, Only use for scaling!"""
    # Player
    player0_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/player/player0.png"))
    player_blank_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets/textures/player/player-1.png"))
    # Enemy
    enemy0_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/enemy/enemy0.png"))
    # Bullet
    bullet_blank_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/bullet/bullet-1.png"))
    # Powerup
    wrench_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/powerUp/powerUp0.png"))
    power_wrench_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/powerUp/powerUp1.png"))
    ammo_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/powerUp/powerUp2.png"))
    # UI
    game_over_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/ui/txt/game_over.png"))
class Textures:
    """Base Class for Textures"""
    class Player:
        """Player Class for Textures"""
        player_blank = pygame.transform.scale_by(RawTextures.player_blank_unscaled, config.SPRITE_SCALING)
        player0 = pygame.transform.scale_by(RawTextures.player0_unscaled, config.SPRITE_SCALING)
    class Enemy:
        """Enemy Class for textures"""
        enemy0 = pygame.transform.scale_by(RawTextures.enemy0_unscaled, config.SPRITE_SCALING)
    class Bullet:
        """Bullet Class for Textures"""
        blank = pygame.transform.scale_by(RawTextures.bullet_blank_unscaled, config.SPRITE_SCALING)
    class PowerUp:
        """PowerUp Class for Textures"""
        wrench = pygame.transform.scale_by(RawTextures.wrench_unscaled, config.SPRITE_SCALING)
        power_wrench = pygame.transform.scale_by(RawTextures.power_wrench_unscaled, config.SPRITE_SCALING)
        ammo = pygame.transform.scale_by(RawTextures.ammo_unscaled, config.SPRITE_SCALING)
    class UI:
        """UI Class for Textures"""
        panel_01 = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/ui/panel/panel_01.png"))
        panel_02 = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/assets//textures/ui/panel/panel_02.png"))
        game_over = pygame.transform.scale_by(RawTextures.game_over_unscaled, config.SPRITE_SCALING)
class Sounds:
    """Base Class for Sounds"""
    entity_damage = pygame.mixer.Sound(pathlib.Path(f"{config.WIN_PATH}/assets//sounds/entity_damage.wav"))
    player_death = pygame.mixer.Sound(pathlib.Path(f"{config.WIN_PATH}/assets//sounds/player_death.wav"))
    player_shoot = pygame.mixer.Sound(pathlib.Path(f"{config.WIN_PATH}/assets//sounds/player_shoot.wav"))
class Music:
    """Base Class for Music"""
    invincibility = pathlib.Path(f"{config.WIN_PATH}/assets//music/invincibility.wav")
def load_music(song, songhint: str = ""):
    pygame.mixer.music.load(filename=song, namehint=songhint)

# -------------------------------------

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    