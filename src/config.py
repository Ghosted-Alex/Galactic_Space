"Config Module"

import os
import subprocess
import math
import pygame
import pathlib
import datetime

<<<<<<< HEAD
WIN_PATH = os.getcwd()

=======
WIN_PATH = pathlib.Path(__file__).resolve().parent
>>>>>>> 8da15c44f4c070c58bb4faba08c2557537738336
SPRITE_SCALING = 6

error = 0000
error_text = ""
error_origin = pathlib.Path()

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
<<<<<<< HEAD
=======

class Keybinds:
    restart_key = pygame.K_r
    quit_key = pygame.K_ESCAPE
>>>>>>> 8da15c44f4c070c58bb4faba08c2557537738336

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
    