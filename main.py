#!/usr/bin/env python3

# Galactic Space Reborn
# Copyright (c) Ghosted Alex 2026
# Code Made under the MIT license:
# Github: https://github.com/Ghosted-Alex/Galactic_Space_Reborn?tab=MIT-2-ov-file
# GitLab: https://gitlab.com/ghostedalex/Galactic_Space_Reborn/-/blob/main/LICENSE_MIT?ref_type=heads

# General Imports
import os
import pathlib
import random
import sys

import pygame

# Quick Initialization
pygame.init()

# Source Imports
import config

from src import assets
from src import entity
from src import update
from src import ui
from src import controls
from src import starfield
from src import stats
from src import clock
from src import states
from src import events
from src.scenes import SceneManager, TitleScene, fade_screen

try:
    from src.mod import load_behavioral_mixins, verify_manifest
    MODDING_AVAILABLE = True
except ImportError:
    MODDING_AVAILABLE = False
    def load_behavioral_mixins():
        """Fallback when src/mod.py is not present."""
        pass

    def verify_manifest() -> bool:
        """Fallback when src/mod.py is not present."""
        return True


def show_loading_screen():
    """Load all assets with a visual loading screen, displaying the splash screen when progress reaches halfway."""
    
    if not verify_manifest():
        print("[Engine Core] Aborting asset streaming sequence due to manifest file verification errors.")
        pygame.quit()
        sys.exit(1)

    # Pre-resolve pre-roll splash texture configuration
    manifest = assets.get_merged_manifest()
    pre_roll_cfg = manifest.get("textures", {}).get("pre_roll", "textures/ui/preRoll.png")
    if isinstance(pre_roll_cfg, dict):
        rel_path = pre_roll_cfg.get("file", "textures/ui/preRoll.png")
        scale = pre_roll_cfg.get("scale", config.SPRITE_SCALING)
    else:
        rel_path = pre_roll_cfg
        scale = config.SPRITE_SCALING

    pre_roll_path = assets.resolve_asset_path(rel_path)
    pre_roll_img = None
    if pre_roll_path.is_file():
        try:
            raw_pre_roll = pygame.image.load(str(pre_roll_path)).convert_alpha()
            pre_roll_img = pygame.transform.scale_by(raw_pre_roll, scale)
        except Exception as err:
            print(f"[Engine Core] Error loading pre-roll graphic: {err}")
    
    # 1. Start asset loading generator
    loader = assets.load_assets_generator()
    screen_rect = SCR.get_rect()
    
    # 2. Progress loop
    for progress in loader:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        SCR.fill((0, 0, 0))
        
        # Calculate loading bar dimensions
        bar_width = 400
        bar_height = 20
        bar_x = screen_rect.centerx - (bar_width // 2)
        bar_y = screen_rect.centery + 100  # Shift bar lower to provide space for splash above
        progress_bar_width = (progress / 100) * bar_width

        # Display splash screen graphic ABOVE the loading bar when progress reaches >= 50%
        if progress >= 50 and pre_roll_img is not None:
            pre_roll_rect = pre_roll_img.get_rect(center=(screen_rect.centerx, bar_y - 150))
            SCR.blit(pre_roll_img, pre_roll_rect)
        
        # Draw progress bar outlines and fill
        pygame.draw.rect(SCR, (255, 255, 255), (bar_x, bar_y, progress_bar_width, bar_height))
        pygame.draw.rect(SCR, (255, 255, 255), (bar_x - 4, bar_y - 4, bar_width + 8, bar_height + 8), 1)

        # Draw progress & loading title text
        if hasattr(assets, 'pressStart2P') and assets.pressStart2P is not None:
            status = assets.pressStart2P.render(f"({progress}%)", True, (255, 255, 255))
            title = assets.pressStart2P.render("Loading Game...", True, (255, 255, 255))
            
            title_rect = title.get_rect(center=(screen_rect.centerx, bar_y - 30))
            status_rect = status.get_rect(center=(screen_rect.centerx, bar_y + 45))
            
            SCR.blit(title, title_rect)
            SCR.blit(status, status_rect)
        
        pygame.display.flip()

    # Fade out loading screen to black before entering title screen
    fade_screen(SCR, mode="out", speed=15)


def initialize():
    """Initialize Game State and Engine Window."""
    global FPS, SCR
    
    FPS = pygame.time.Clock()
    SCR = pygame.display.set_mode((config.Screen.Size.w, config.Screen.Size.h))    
    
    pygame.display.set_caption(config.Game.title)
    
    # Load and execute mod mixins before loading assets
    load_behavioral_mixins()
    
    # Run asset loader with pre-roll splash halfway through
    show_loading_screen()
    
    if assets.Textures.icon is not None:
        pygame.display.set_icon(assets.Textures.icon)
    else:
        vanilla_icon_path = pathlib.Path(config.WIN_PATH) / "assets" / "textures" / "ui" / "icon.png"
        if vanilla_icon_path.is_file():
            fallback_surface = pygame.image.load(str(vanilla_icon_path)).convert_alpha()
            pygame.display.set_icon(fallback_surface)
            print("[Engine Core] Mod icon undefined. Safely loaded vanilla fallback display icon.")
    
    return FPS, SCR


FPS, SCR = initialize()

# Initialize Scene Manager & set initial Title Scene (with smooth fade-in)
scene_manager = SceneManager(SCR)
scene_manager.set_scene(TitleScene(), fade=True, fade_speed=12)

running = True

while running:
    dt = FPS.tick(60) / 1000.0  # Framerate clock tick

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        scene_manager.handle_event(event)

    scene_manager.update(dt)
    scene_manager.draw(SCR)
    pygame.display.flip()

pygame.quit()
