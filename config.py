"""Config Module"""

import pygame
import os
import pathlib
import sys
import math

# ------------------- PYINSTALLER EXCLUSIVE CODE | DO NOT EDIT --------------
if hasattr(sys, "_MEIPASS"):
  # Compiled Exe: Static assets and manifests come from the read-only temp sandbox
  WIN_PATH = pathlib.Path(sys._MEIPASS)
  # Writable Data: Saves, settings, and mods go next to the actual game launcher executable
  DATA_PATH = pathlib.Path(sys.executable).resolve().parent
else:
  # Dev Mode: Everything lives relative to config.py
  WIN_PATH = pathlib.Path(__file__).resolve().parent
  DATA_PATH = WIN_PATH
# ----------------------------------------------------------------------------

# --- Static Engine Files (Bundled in PyInstaller) ---
MANIFEST_FILE = (
    WIN_PATH / "manifest.json"
)  # Defaults to temp folder when compiled

# --- Writable User Data / Saves / External Content ---
HIGH_SCORE_FILE = DATA_PATH / "high_score.txt"
OPTIONS_FILE = DATA_PATH / "options.txt"
SETTINGS_FILE = DATA_PATH / "settings.json"
RESOURCE_PACK_SELECTION_FILE = DATA_PATH / "resource_pack.json"

# Resource packs and mods should live outside so players can add them easily!
RESOURCE_PACKS_DIR = DATA_PATH / "resource_packs"

PACKS_ACTIVE = False
"""Whether the current runtime is using a resource pack instead of vanilla assets."""


def check_high_score_exists() -> bool:
    """Dynamic boolean check: True if high_score.txt exists on disk right now."""
    return HIGH_SCORE_FILE.exists()


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
        escape = pygame.K_ESCAPE


# --- This part is for modding, only modify this if you know what you are doing ----
if os.environ.get("GSR_USE_MODS") == "True" and os.environ.get("GSR_ACTIVE_MOD"):
    _mod_name = os.environ.get("GSR_ACTIVE_MOD")

    # Divert manifest paths straight into the active workspace folder
    MANIFEST_FILE = DATA_PATH / "mods" / _mod_name / "manifest.json"
    MODS_ACTIVE = True
    print(f"[Engine Config] Mod Active: Layering paths to '/mods/{_mod_name}/'")
else:
    # Vanilla fallback path configuration
    MANIFEST_FILE = DATA_PATH / "manifest.json"
    MODS_ACTIVE = False
    print("[Engine Config] Run profile: Vanilla. Native pipeline active.")
# -----------------------------------------------------------------------------------

SPRITE_SCALING = 3
"""Multiplier for sprite asset scaling."""

debug = False
"""Boolean flag to enable/disable debug mode."""

# Color constants (RGB)
background_health_color = (15, 15, 15)
background_energy_color = (15, 15, 15)

health_color_high = (50, 168, 82)  # Green
health_color_med = (166, 164, 51)  # Yellow
health_color_low = (166, 51, 51)  # Red
health_color_drain = (135, 242, 255)  # Cyan

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

version_string = "1.0-beta.1"
"""Args:
    String: '<major>.<minor>-beta|build.<beta|build_number>'"""

# Initialize variables
major, minor = "0", "0"
build = "0"

# 1. Separate the core version (e.g., "1.0") from the metadata tail
if "-" in version_string:
    core, tail = version_string.split("-", 1)
else:
    core, tail = version_string, ""

# 2. Extract major and minor
version_bits = core.split(".")
major = version_bits[0]
if len(version_bits) > 1:
    minor = version_bits[1]

build = tail # e.g., "beta.1 / build.20260822"

version = f"{major}.{minor}-{build}"

p02_pos = [Screen.Size.w - 246, Screen.Size.h - 195]
"""Position anchor for the Panel 02 UI Element."""

if __name__ == "__main__":
    print(ModuleNotFoundError(
        "No module named config.__main__; 'config' is a dedicated module for Galactic Space Reborn and cannot be directly executed"))
    print("(Run the game with main.py, not the config file)")
