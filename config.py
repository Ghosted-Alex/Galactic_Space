"Config Module"

import pygame
import pathlib
from typing import TypeAlias, Union, Tuple

KeyLike: TypeAlias = Union[int, Tuple[int, ...]]

class KeyBinds:
    """
    Configuration class for mapping input keys to actions.

    Usage:
        To access a keybind: KeyBinds.Category.ACTION_NAME

    Naming Conventions:
        - Numpad keys: use prefix 'numpad_' (e.g., 'numpad_1')
        - Top row numbers: use prefix 'numrow_' (e.g., 'numrow_1')

    Example:
        up = KeyBinds.Gameplay.up
    """
    class Gameplay:
        "Gameplay Category for Keybinds"
        up: KeyLike = pygame.K_w
        left: KeyLike = pygame.K_a
        down: KeyLike = pygame.K_s
        right: KeyLike = pygame.K_d
        shoot: KeyLike = (pygame.K_SPACE, pygame.K_z)
    class Debug:
        "Debug Category for Keybinds"
        numpad_plus: KeyLike = pygame.K_KP_PLUS
        numrow_1: KeyLike = pygame.K_1

WIN_PATH = pathlib.Path(__file__).resolve().parent
SPRITE_SCALING = 6

delay = 60

game_over_delay = 180

difficulty = 0

debug = False

score = 0

high_score = 0

HIGH_SCORE_FILE = pathlib.Path(f"{WIN_PATH}/high_score.txt")

HIGH_SCORE_FILE_EXISTS = pathlib.Path.exists(HIGH_SCORE_FILE)

powerup_timer = 0

powerup_active = False

powerup_type = 0

powerup_type_text = "powerup_display.identifier.txt"

frame = 0

BACKGROUND_HEALTH_COLOR = (15, 15, 15)
BACKGROUND_AMMO_COLOR = (15, 15, 15)

HEALTH_COLOR_HIGH = (50, 168, 82) # High Health Color (Green)
HEALTH_COLOR_MED = (166, 164, 51) # Medium Health Color (Yellow)
HEALTH_COLOR_LOW = (166, 51, 51) # Low Health Color (Red)
HEALTH_COLOR_DRAIN = (135, 242, 255) # Drain Color (Cyan)

AMMO_COLOR = (219, 212, 53)

blink_timer = 60
health_blink_timer = 60

game_over = False
game_over_ui_shown = False

class Screen:
    "Base Class for Screen"
    class Size:
        "Size of Screen"
        w = 922
        "width: 922"
        h = 691
        "height: 691"

class Game:
    title = "Galactic Space Reborn"
    running = True

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    