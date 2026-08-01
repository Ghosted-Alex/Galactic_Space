"""Run Settings / Difficulty Selector Screen for Galactic Space Reborn.

Provides dedicated load(), unload(), handle_event(), update(), and draw() functions
as well as a DifficultyScene class wrapper for mission setup before starting a game.
"""

import sys
import pygame
import config
from src import assets
from src import starfield
from .base import BaseScene

_state = {
    "loaded": False,
    "stars_bg": None,
    "selected_index": 1,  # Default to Normal (1.0x)
    "focus_area": "difficulty",  # "difficulty", "debug", "back", "start"
    "options": [
        {
            "name": "EASY",
            "texture": "difficulty0",
            "multiplier": 0.75,
            "color": (70, 160, 255),  # Blue
        },
        {
            "name": "NORMAL",
            "texture": "difficulty1",
            "multiplier": 1.0,
            "color": (60, 220, 200),  # Teal
        },
        {
            "name": "MEDIUM",
            "texture": "difficulty2",
            "multiplier": 1.25,
            "color": (60, 210, 90),  # Green
        },
        {
            "name": "HARD",
            "texture": "difficulty3",
            "multiplier": 1.5,
            "color": (245, 210, 45),  # Yellow
        },
        {
            "name": "INSANE",
            "texture": "difficulty4",
            "multiplier": 1.75,
            "color": (255, 140, 35),  # Orange
        },
        {
            "name": "GALACTIC",
            "texture": "difficulty5",
            "multiplier": 2.0,
            "color": (255, 65, 65),  # Red
        },
    ],
    "option_rects": [],
    "debug_rect": None,
    "back_rect": None,
    "start_rect": None,
    "hover_item": None,
}


def load(*args, **kwargs):
    """Dedicated scene load function. Initializes difficulty selector state."""
    _state["loaded"] = True
    _state["stars_bg"] = starfield.Generate(config.Screen.Size.w, config.Screen.Size.h)
    _state["option_rects"] = []

    current_mult = getattr(config, "difficulty", 1.0)
    for idx, opt in enumerate(_state["options"]):
        if opt["multiplier"] == current_mult:
            _state["selected_index"] = idx
            break


def unload():
    """Dedicated scene unload function. Cleans up state."""
    _state["loaded"] = False
    _state["stars_bg"] = None
    _state["option_rects"].clear()


def handle_event(event: pygame.event.Event, manager=None):
    """Dedicated event handler for difficulty & run settings."""
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)

    if event.type == pygame.KEYDOWN:
        if event.key in (pygame.K_UP, pygame.K_w):
            _state["selected_index"] = (_state["selected_index"] - 1) % len(_state["options"])
            config.difficulty = _state["options"][_state["selected_index"]]["multiplier"]
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            _state["selected_index"] = (_state["selected_index"] + 1) % len(_state["options"])
            config.difficulty = _state["options"][_state["selected_index"]]["multiplier"]
        elif event.key == pygame.K_d:  # Toggle debug with D
            config.debug = not config.debug
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            _start_gameplay(manager)
        elif event.key == pygame.K_ESCAPE:
            _return_to_title(manager)

    elif event.type == pygame.MOUSEMOTION:
        mouse_pos = event.pos
        _state["hover_item"] = None
        for idx, rect in enumerate(_state["option_rects"]):
            if rect and rect.collidepoint(mouse_pos):
                _state["selected_index"] = idx
                config.difficulty = _state["options"][idx]["multiplier"]
                _state["hover_item"] = f"opt_{idx}"
        if _state["debug_rect"] and _state["debug_rect"].collidepoint(mouse_pos):
            _state["hover_item"] = "debug"
        elif _state["back_rect"] and _state["back_rect"].collidepoint(mouse_pos):
            _state["hover_item"] = "back"
        elif _state["start_rect"] and _state["start_rect"].collidepoint(mouse_pos):
            _state["hover_item"] = "start"

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = event.pos
        for idx, rect in enumerate(_state["option_rects"]):
            if rect and rect.collidepoint(mouse_pos):
                _state["selected_index"] = idx
                config.difficulty = _state["options"][idx]["multiplier"]

        if _state["debug_rect"] and _state["debug_rect"].collidepoint(mouse_pos):
            config.debug = not config.debug
        elif _state["back_rect"] and _state["back_rect"].collidepoint(mouse_pos):
            _return_to_title(manager)
        elif _state["start_rect"] and _state["start_rect"].collidepoint(mouse_pos):
            _start_gameplay(manager)


def _start_gameplay(manager=None):
    """Applies current settings and launches gameplay."""
    selected_opt = _state["options"][_state["selected_index"]]
    config.difficulty = selected_opt["multiplier"]
    print(f"[Engine Config] Starting run on difficulty {selected_opt['name']} ({config.difficulty}x)")
    if manager:
        from .gameplay import GameplayScene
        manager.set_scene(GameplayScene(), fade=True)


def _return_to_title(manager=None):
    """Transitions back to Title screen."""
    if manager:
        from .title import TitleScene
        manager.set_scene(TitleScene(), fade=True)


def update(dt: float = 1.0):
    """Dedicated update function. Advances background starfield."""
    if _state["stars_bg"]:
        _state["stars_bg"].update()


def draw(screen: pygame.Surface):
    """Dedicated draw function. Renders run setup options & bottom buttons."""
    screen.fill((0, 0, 0))

    if _state["stars_bg"]:
        _state["stars_bg"].draw(screen)

    center_x = config.Screen.Size.w // 2
    font = getattr(assets, 'pressStart2P', None)

    # 1. Header Title
    if font:
        title_surf = font.render("RUN CONFIGURATION", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(center_x, 50))
        screen.blit(title_surf, title_rect)

        sub_surf = font.render("Select Difficulty and\nMission Parameters", True, (135, 242, 255))
        screen.blit(sub_surf, sub_surf.get_rect(center=(center_x, 105)))

    # 2. Render Difficulty Cards (6 Cards)
    _state["option_rects"] = []
    start_y = 150
    card_height = 70
    spacing = 80
    card_width = 720

    for idx, opt in enumerate(_state["options"]):
        is_selected = (idx == _state["selected_index"])
        is_active = (opt["multiplier"] == config.difficulty)

        card_rect = pygame.Rect(center_x - (card_width // 2), start_y + idx * spacing, card_width, card_height)
        _state["option_rects"].append(card_rect)

        # Card Background & Border Styling
        bg_color = (30, 45, 65) if is_selected else (18, 22, 32)
        border_color = opt["color"] if (is_selected or is_active) else (55, 65, 80)
        border_width = 3 if is_selected else (2 if is_active else 1)

        pygame.draw.rect(screen, bg_color, card_rect, border_radius=8)
        pygame.draw.rect(screen, border_color, card_rect, width=border_width, border_radius=8)

        # Left Accent Color Strip
        strip_rect = pygame.Rect(card_rect.x, card_rect.y, 10, card_height)
        pygame.draw.rect(screen, opt["color"], strip_rect, border_top_left_radius=8, border_bottom_left_radius=8)

        # Draw Difficulty Texture Badge Image
        tex_surf = getattr(assets.Textures, opt["texture"], None)
        text_x_offset = card_rect.x + 30

        if tex_surf is not None:
            tex_rect = tex_surf.get_rect(midleft=(card_rect.x + 25, card_rect.centery))
            screen.blit(tex_surf, tex_rect)
            text_x_offset = tex_rect.right + 20

        if font:
            title_str = f"{opt['name']}"
            opt_title = font.render(title_str, True, opt["color"] if is_selected else (230, 230, 230))
            screen.blit(opt_title, (text_x_offset, card_rect.y + 12))

    # 4. Bottom Navigation Action Bar: BACK and START Buttons
    button_y = config.Screen.Size.h - 68
    btn_width = 240
    btn_height = 46

    back_rect = pygame.Rect(center_x - btn_width - 20, button_y, btn_width, btn_height)
    start_rect = pygame.Rect(center_x + 20, button_y, btn_width, btn_height)
    _state["back_rect"] = back_rect
    _state["start_rect"] = start_rect

    is_back_hover = (_state["hover_item"] == "back")
    is_start_hover = (_state["hover_item"] == "start")

    # Draw BACK Button
    back_bg = (50, 30, 35) if is_back_hover else (30, 25, 32)
    back_border = (255, 100, 100) if is_back_hover else (120, 70, 80)
    pygame.draw.rect(screen, back_bg, back_rect, border_radius=8)
    pygame.draw.rect(screen, back_border, back_rect, width=2 if is_back_hover else 1, border_radius=8)

    if font:
        back_surf = font.render("< BACK", True, (255, 255, 255))
        screen.blit(back_surf, back_surf.get_rect(center=back_rect.center))

    # Draw START MISSION Button
    start_bg = (30, 80, 50) if is_start_hover else (20, 55, 35)
    start_border = (100, 255, 140) if is_start_hover else (50, 168, 82)
    pygame.draw.rect(screen, start_bg, start_rect, border_radius=8)
    pygame.draw.rect(screen, start_border, start_rect, width=2 if is_start_hover else 1, border_radius=8)

    if font:
        start_surf = font.render("START >", True, (255, 255, 255))
        screen.blit(start_surf, start_surf.get_rect(center=start_rect.center))


class DifficultyScene(BaseScene):
    """Class wrapper for Difficulty / Run Setup scene."""

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
