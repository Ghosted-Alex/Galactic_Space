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
from src import settings
from src.scenes import SceneManager, TitleScene, fade_screen

try:
    from src.pack import load_resources, verify_manifest
    PACK_USE_AVAILABLE = True
except ImportError:
    PACK_USE_AVAILABLE = False
    def load_resources():
        """Fallback when the resource-pack module is not present."""
        pass

    def verify_manifest() -> bool:
        """Fallback when src/packs.py is not present."""
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

    # Fade-in state for the pre-roll splash
    pre_roll_alpha = 0          # current alpha (0=transparent, 255=opaque)
    FADE_SPEED = 32              # alpha units added per frame (~32 frames to full opacity)

    # 2. Progress loop
    for progress, current_file_text in loader:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        SCR.fill((0, 0, 0))

        bar_width = 400
        bar_height = 20
        bar_x = screen_rect.centerx - (bar_width // 2)
        bar_y = screen_rect.centery + 100
        progress_bar_width = (progress / 100) * bar_width

        if progress >= 25 and pre_roll_img is not None:
            pre_roll_alpha = min(255, pre_roll_alpha + FADE_SPEED)
            pre_roll_img.set_alpha(pre_roll_alpha)
            pre_roll_rect = pre_roll_img.get_rect(center=(screen_rect.centerx, bar_y - 150))
            SCR.blit(pre_roll_img, pre_roll_rect)

        # Draw progress bar outlines and fill
        pygame.draw.rect(SCR, (255, 255, 255), (bar_x, bar_y, progress_bar_width, bar_height))
        pygame.draw.rect(SCR, (255, 255, 255), (bar_x - 4, bar_y - 4, bar_width + 8, bar_height + 8), 1)

        # Draw progress, title, and current file text
        if hasattr(assets, 'pressStart2P') and assets.pressStart2P is not None:
            title = assets.pressStart2P.render("Loading Game...", True, (255, 255, 255))
            status = assets.pressStart2P.render(f"({progress}%)", True, (255, 255, 255))

            # Create a smaller font or render the current file string (you can scale it down if 30pt is too big)
            file_surf = assets.pressStart2P.render(current_file_text, True, (180, 180, 180))
            # Optional: Scale down file text so it doesn't overflow the screen width
            file_surf = pygame.transform.smoothscale(file_surf, (int(file_surf.get_width() * 0.5),
                                                                 int(file_surf.get_height() * 0.5)))

            title_rect = title.get_rect(center=(screen_rect.centerx, bar_y - 30))
            status_rect = status.get_rect(center=(screen_rect.centerx, bar_y + 45))
            file_rect = file_surf.get_rect(center=(screen_rect.centerx, bar_y + 80))

            SCR.blit(title, title_rect)
            SCR.blit(status, status_rect)
            SCR.blit(file_surf, file_rect)

        pygame.display.flip()

    # Fade out loading screen to black before entering title screen
    fade_screen(SCR, mode="out", speed=15)


def initialize():
    """Initialize Game State and Engine Window."""
    global FPS, SCR
    
    FPS = pygame.time.Clock()
    settings.load()
    SCR = settings.create_display()
    
    pygame.display.set_caption(config.Game.title)
    
    # Restore the player's resource-pack choice before resolving any assets.
    load_resources()
    
    # Run asset loader with pre-roll splash halfway through
    show_loading_screen()
    settings.apply_audio()
    
    if assets.Textures.icon is not None:
        pygame.display.set_icon(assets.Textures.icon)
    else:
        vanilla_icon_path = pathlib.Path(config.DATA_PATH) / "assets" / "textures" / "ui" / "icon.png"
        if vanilla_icon_path.is_file():
            fallback_surface = pygame.image.load(str(vanilla_icon_path)).convert_alpha()
            pygame.display.set_icon(fallback_surface)
            print("[Engine Core] Pack icon undefined. Safely loaded vanilla fallback display icon.")
    
    return FPS, SCR


FPS, SCR = initialize()

# Initialize Scene Manager & set initial Title Scene (with smooth fade-in)
scene_manager = SceneManager(SCR)
scene_manager.set_scene(TitleScene(), fade=True, fade_speed=12)


def reload_game_window():
    """Recreate pygame's window and refill the asset cache for a new pack."""
    global SCR

    pygame.mixer.stop()
    pygame.display.quit()
    pygame.display.init()
    SCR = settings.create_display()
    pygame.display.set_caption(config.Game.title)

    show_loading_screen()
    settings.apply_audio()
    if assets.Textures.icon is not None:
        pygame.display.set_icon(assets.Textures.icon)

    scene_manager.replace_screen(SCR)
    # A fresh title scene avoids keeping gameplay/menu surfaces tied to the old display.
    scene_manager.set_scene(TitleScene(), fade=False)

running = True

while running:
    dt = FPS.tick(60) / 1000.0  # Framerate clock tick

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        scene_manager.handle_event(event)

    if scene_manager.consume_window_reload_request():
        reload_game_window()

    scene_manager.update(dt)
    scene_manager.draw(SCR)

    pygame.display.flip()

pygame.quit()
