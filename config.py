"""Config Module"""

import pygame
import os
import pathlib
import math

class KeyBinds:
    """Organizes control inputs into categories for easy access."""
    class Gameplay:
        """Controls for player movement and actions."""
        up = pygame.K_w
        left = pygame.K_a
        down = pygame.K_s
        right = pygame.K_d
        shoot = (pygame.K_SPACE, pygame.K_z)
    class Debug:
        """Keys reserved for development and troubleshooting."""
        numpad_plus = pygame.K_KP_PLUS
        numrow_1 = pygame.K_1
        debug_key = pygame.K_F12
    class General:
        """Miscellaneous game controls."""
        reset = pygame.K_r

# Project paths and environment
WIN_PATH = pathlib.Path(__file__).resolve().parent
"""Absolute path to the game directory."""

# --- This part is for modding, only modify this if you know what you are doing ----
if os.environ.get("GSR_USE_MODS") == "True" and os.environ.get("GSR_ACTIVE_MOD"):
    _mod_name = os.environ.get("GSR_ACTIVE_MOD")
    
    # Divert manifest paths straight into the active workspace folder
    MANIFEST_FILE = WIN_PATH / "mods" / _mod_name / "manifest.json"
    MODS_ACTIVE = True
    print(f"[Engine Config] Mod Active: Layering paths to '/mods/{_mod_name}/'")
else:
    # Vanilla fallback path configuration
    MANIFEST_FILE = WIN_PATH / "manifest.json"
    MODS_ACTIVE = False
    print("[Engine Config] Run profile: Vanilla. Native pipeline active.")
# -----------------------------------------------------------------------------------

SPRITE_SCALING = 3
"""Multiplier for sprite asset scaling."""

difficulty = 1
"""Current game difficulty multiplier (default: 1)."""

debug = False
"""Boolean flag to enable/disable debug mode."""

HIGH_SCORE_FILE = pathlib.Path(f"{WIN_PATH}/high_score.txt")
"""Path object for the high score storage file."""
HIGH_SCORE_FILE_EXISTS = pathlib.Path.exists(HIGH_SCORE_FILE)
"""Boolean check: True if high_score.txt exists on disk."""

# Color constants (RGB)
background_health_color = (15, 15, 15)
background_energy_color  = (15, 15, 15)

health_color_high = (50, 168, 82)   # Green
health_color_med = (166, 164, 51)   # Yellow
health_color_low = (166, 51, 51)    # Red
health_color_drain = (135, 242, 255) # Cyan

energy_color = (219, 212, 53)

blink_timer_max = 60
"""Max frames for UI blink animations."""

class Screen:
    """Screen settings."""
    class Size:
        """Resolution dimensions."""
        w = 1072
        """Window width."""
        h = 861
        """Window height."""

class Game:
    """Global game metadata."""
    title = "Galactic Space Reborn"

format_ver = 1
"""The format version for manifest.json

Args:
    Int: The version is supported in the game engine"""

p02_pos = [Screen.Size.w-246, Screen.Size.h-195]
"""Position anchor for the Panel 02 UI Element."""

if __name__ == "__main__":
    print(ModuleNotFoundError("No module named config.__main__; 'config' is a dedicated module for Galactic Space Reborn and cannot be directly executed"))
    print("(Run the game with main.py, not the config file)")
