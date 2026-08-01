"""Scenes package for Galactic Space Reborn."""

from .base import BaseScene
from .manager import SceneManager, fade_screen
from .title import TitleScene, load as load_title, unload as unload_title
from .difficulty import DifficultyScene, load as load_difficulty, unload as unload_difficulty
from .options import OptionsScene, load as load_options, unload as unload_options
from .gameplay import GameplayScene, load as load_gameplay, unload as unload_gameplay

__all__ = [
    "BaseScene",
    "SceneManager",
    "fade_screen",
    "TitleScene",
    "DifficultyScene",
    "OptionsScene",
    "GameplayScene",
    "load_title",
    "unload_title",
    "load_difficulty",
    "unload_difficulty",
    "load_options",
    "unload_options",
    "load_gameplay",
    "unload_gameplay",
]
