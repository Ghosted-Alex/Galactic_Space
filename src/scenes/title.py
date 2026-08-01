"""Title Screen / Scene for Galactic Space Reborn.

Provides dedicated load(), unload(), handle_event(), update(), and draw() functions
as well as a TitleScene class wrapper.
"""

import sys
import pygame
import config
from src import assets
from src import starfield
from src import stats
from src import events
from .base import BaseScene


# Scene state container for functional module interface
_state = {
    "loaded": False,
    "stars_bg": None,
    "selected_index": 0,
    "options": ["PLAY GAME", "OPTIONS", "QUIT GAME"],
    "option_rects": [],
    "timer": 0,
}


def load(*args, **kwargs):
    """Dedicated scene load function. Initializes title screen assets and state."""
    _state["loaded"] = True
    _state["selected_index"] = 0
    _state["timer"] = 0
    _state["stars_bg"] = starfield.Generate(config.Screen.Size.w, config.Screen.Size.h)
    _state["option_rects"] = []

    # Ensure high score is updated
    if config.HIGH_SCORE_FILE_EXISTS:
        stats.high_score = events.load_high_score(config.HIGH_SCORE_FILE)


def unload():
    """Dedicated scene unload function. Cleans up title screen state."""
    _state["loaded"] = False
    _state["stars_bg"] = None
    _state["option_rects"].clear()


def handle_event(event: pygame.event.Event, manager=None):
    """Dedicated event handler for title screen interaction."""
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)

    if event.type == pygame.KEYDOWN:
        if event.key in (pygame.K_UP, pygame.K_w):
            _state["selected_index"] = (_state["selected_index"] - 1) % len(_state["options"])
            if hasattr(assets, 'Sounds') and hasattr(assets.Sounds, 'player_shoot'):
                pass  # option select sound if desired
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            _state["selected_index"] = (_state["selected_index"] + 1) % len(_state["options"])
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            _activate_option(_state["selected_index"], manager)

    elif event.type == pygame.MOUSEMOTION:
        mouse_pos = event.pos
        for idx, rect in enumerate(_state["option_rects"]):
            if rect and rect.collidepoint(mouse_pos):
                _state["selected_index"] = idx

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = event.pos
        for idx, rect in enumerate(_state["option_rects"]):
            if rect and rect.collidepoint(mouse_pos):
                _activate_option(idx, manager)


def _activate_option(index: int, manager=None):
    """Executes the selected title menu option."""
    if index == 0:  # PLAY GAME -> Opens Run Setup / Difficulty Menu
        if manager:
            from .difficulty import DifficultyScene
            manager.set_scene(DifficultyScene(), fade=True)
    elif index == 1:  # OPTIONS -> Opens Options menu
        if manager:
            from .options import OptionsScene
            manager.set_scene(OptionsScene(), fade=True)
    elif index == 2:  # QUIT GAME
        pygame.quit()
        sys.exit(0)


def update(dt: float = 1.0):
    """Dedicated update function. Advances background starfield and UI animations."""
    if _state["stars_bg"]:
        _state["stars_bg"].update()
    _state["timer"] += 1


def draw(screen: pygame.Surface):
    """Dedicated draw function. Renders title screen elements to surface."""
    screen.fill((0, 0, 0))

    # 1. Draw Starfield Background
    if _state["stars_bg"]:
        _state["stars_bg"].draw(screen)

    center_x = config.Screen.Size.w // 2

    # 2. Main Title Banner
    font_large = getattr(assets, 'pressStart2P', None)
    if font_large:
        title_surf = font_large.render("GALACTIC SPACE", True, (255, 255, 255))
        sub_title_surf = font_large.render("REBORN", True, (135, 242, 255))

        title_rect = title_surf.get_rect(center=(center_x, 150))
        sub_title_rect = sub_title_surf.get_rect(center=(center_x, 200))

        # Title shadow effect
        shadow_surf = font_large.render("GALACTIC SPACE", True, (40, 40, 60))
        sub_shadow_surf = font_large.render("REBORN", True, (40, 80, 120))
        screen.blit(shadow_surf, title_rect.move(0, 3))
        screen.blit(sub_shadow_surf, sub_title_rect.move(0, 3))

        screen.blit(title_surf, title_rect)
        screen.blit(sub_title_surf, sub_title_rect)

    # 3. High Score Display
    if font_large:
        score_text = f"HIGH SCORE: {int(stats.high_score)}"
        hs_surf = font_large.render(score_text, True, (219, 212, 53))
        screen.blit(hs_surf, hs_surf.get_rect(center=(center_x, 260)))

    # 4. Render Menu Options (driven directly from _state["options"] so nav & display are always in sync)
    _state["option_rects"] = []
    start_y = 360
    spacing = 65

    for idx, opt_text in enumerate(_state["options"]):
        is_selected = (idx == _state["selected_index"])
        color = (255, 255, 255) if not is_selected else (135, 242, 255)

        if font_large:
            prefix = "> " if is_selected else "  "
            full_text = prefix + opt_text + (" <" if is_selected else "  ")
            text_surf = font_large.render(full_text, True, color)
            rect = text_surf.get_rect(center=(center_x, start_y + idx * spacing))

            icon_rect = None

            clickable_rect = rect
            _state["option_rects"].append(clickable_rect)

            # Draw background box for active hover option
            if is_selected:
                box_rect = clickable_rect.inflate(24, 16)
                pygame.draw.rect(screen, (30, 45, 65), box_rect, border_radius=6)
                pygame.draw.rect(screen, (135, 242, 255), box_rect, width=2, border_radius=6)

            screen.blit(text_surf, rect)

    # 6. Controls Helper Footer
    if font_large:
        help_surf = font_large.render("W/S or UP/DOWN to Select\n\nENTER to Confirm", True, (120, 130, 150))
        help_rect = help_surf.get_rect(center=(center_x, config.Screen.Size.h - 60))
        screen.blit(help_surf, help_rect)


class TitleScene(BaseScene):
    """Class wrapper for Title Screen scene."""

    def load(self, *args, **kwargs):
        load(*args, **kwargs)

    def unload(self):
        unload()

    def handle_event(self, event: pygame.event.Event):
        handle_event(event, self.manager)

    def update(self, dt: float = 1.0):
        update(dt)

    def draw(self, screen: pygame.Surface):
        draw(screen)
