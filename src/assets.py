"Module for Assets"

import pathlib

import pygame

import src.config as config

pygame.mixer.init()

monocraft = None
"""Font used in-game"""

# -------------------------------------
try:
    monocraft = pygame.font.Font(f"{config.WIN_PATH}/fonts/monocraft.ttf", 30)

    class RawTextures:
        """Base Class for Unscaled Textures, Only use for scaling!"""
        # Player
<<<<<<< HEAD
        player_blank_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/player/player-1.png").convert_alpha()
        player0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/player/player0.png").convert_alpha()

        # Enemy
        enemy0_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/enemy/enemy0.png").convert_alpha()

        # Bullet
        bullet_blank_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/bullet/bullet-1.png").convert_alpha()

        # Powerup
        wrench_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp0.png").convert_alpha()
        power_wrench_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp1.png").convert_alpha()
        ammo_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/powerUp/powerUp2.png").convert_alpha()

        # UI
        game_over_unscaled = pygame.image.load(f"{config.WIN_PATH}/textures/ui/txt/game_over.png").convert_alpha()
=======
        player0_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/player/player0.png"))

        # Enemy
        enemy0_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/enemy/enemy0.png"))

        # Bullet
        bullet_blank_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/bullet/bullet-1.png"))

        # Powerup
        wrench_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/powerUp/powerUp0.png"))
        power_wrench_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/powerUp/powerUp1.png"))
        ammo_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/powerUp/powerUp2.png"))

        # UI
        game_over_unscaled = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/ui/txt/game_over.png"))
>>>>>>> 8da15c44f4c070c58bb4faba08c2557537738336


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
<<<<<<< HEAD
            panel_01 = pygame.image.load(f"{config.WIN_PATH}/textures/ui/panel/panel_01.png").convert_alpha()
            panel_02 = pygame.image.load(f"{config.WIN_PATH}/textures/ui/panel/panel_02.png").convert_alpha()
=======
            panel_01 = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/ui/panel/panel_01.png"))
            panel_02 = pygame.image.load(pathlib.Path(f"{config.WIN_PATH}/textures/ui/panel/panel_02.png"))
>>>>>>> 8da15c44f4c070c58bb4faba08c2557537738336
            game_over = pygame.transform.scale_by(RawTextures.game_over_unscaled, config.SPRITE_SCALING)


    class Sounds:
        """Base Class for Sounds"""

        entity_damage = pygame.mixer.Sound(pathlib.Path(f"{config.WIN_PATH}/sounds/entity_damage.wav"))
        player_death = pygame.mixer.Sound(pathlib.Path(f"{config.WIN_PATH}/sounds/player_death.wav"))
        player_shoot = pygame.mixer.Sound(pathlib.Path(f"{config.WIN_PATH}/sounds/player_shoot.wav"))


    class Music:
        """Base Class for Music"""

        invincibility = pathlib.Path(f"{config.WIN_PATH}/music/invincibility.wav")


    def load_music(song, songhint: str = ""):
        pygame.mixer.music.load(filename=song, namehint=songhint)

except Exception as e:
    config.error = 1010
    config.error_text = f"An error occured while loading one or more assets!\nError: {e}"
    # This automatically gets the current file's absolute path
    config.error_origin = config.pathlib.Path(__file__).resolve()

    print(f"Error Loading One or More Assets ({config.error})")
    print(f"Details of Error: {config.error_text}")
    print(f"Error Came From: {config.error_origin}")
    print(f"Current Working Directory: {config.WIN_PATH}")


# -------------------------------------

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    