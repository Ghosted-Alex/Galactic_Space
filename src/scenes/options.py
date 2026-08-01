"""Options Screen / Scene for Galactic Space Reborn.

Provides dedicated load(), unload(), handle_event(), update(), and draw() functions
as well as an OptionsScene class wrapper.
"""

import sys
import pygame
import config
from src import assets
from src import starfield
from src import stats
from .base import BaseScene


_state = {
    "loaded": False,
    "stars_bg": None,
    "back_rect": None,
    "debug_rect": None,
    "hover_item": None,  # "debug" | "back" | None
}


def load(*args, **kwargs):
    """Dedicated scene load function. Initializes options screen state."""
    _state["loaded"] = True
    _state["stars_bg"] = starfield.Generate(config.Screen.Size.w, config.Screen.Size.h)


def unload():
    """Dedicated scene unload function. Cleans up options screen state."""
    _state["loaded"] = False
    _state["stars_bg"] = None


def handle_event(event: pygame.event.Event, manager=None):
    """Dedicated event handler for options menu."""
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            _return_to_title(manager)
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            # Only toggle debug when the debug row is hovered / focused
            if _state["hover_item"] == "debug":
                config.debug = not config.debug

    elif event.type == pygame.MOUSEMOTION:
        mouse_pos = event.pos
        _state["hover_item"] = None
        if _state["debug_rect"] and _state["debug_rect"].collidepoint(mouse_pos):
            _state["hover_item"] = "debug"
        elif _state["back_rect"] and _state["back_rect"].collidepoint(mouse_pos):
            _state["hover_item"] = "back"

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = event.pos
        if _state["debug_rect"] and _state["debug_rect"].collidepoint(mouse_pos):
            config.debug = not config.debug
        elif _state["back_rect"] and _state["back_rect"].collidepoint(mouse_pos):
            _return_to_title(manager)


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
    """Dedicated draw function. Renders options settings & controls guide."""
    screen.fill((0, 0, 0))

    if _state["stars_bg"]:
        _state["stars_bg"].draw(screen)

    center_x = config.Screen.Size.w // 2
    font = getattr(assets, 'pressStart2P', None)

    # 1. Header Title
    if font:
        title_surf = font.render("GAME OPTIONS", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(center_x, 90))
        screen.blit(title_surf, title_rect)

        sub_surf = font.render("System Settings & Controls", True, (135, 242, 255))
        screen.blit(sub_surf, sub_surf.get_rect(center=(center_x, 135)))

    # 2. Options Settings Card Container
    container_rect = pygame.Rect(center_x - 360, 180, 720, 460)
    pygame.draw.rect(screen, (18, 24, 36), container_rect, border_radius=10)
    pygame.draw.rect(screen, (60, 80, 110), container_rect, width=2, border_radius=10)

    if font:
        start_y = 220
        spacing = 55

        # Item 1: Window Resolution
        res_label = font.render("RESOLUTION:", True, (200, 200, 200))
        res_val = font.render(f"{config.Screen.Size.w} x {config.Screen.Size.h}", True, (135, 242, 255))
        screen.blit(res_label, (container_rect.x + 30, start_y))
        screen.blit(res_val, (container_rect.x + 355, start_y))

        # Item 2: Sprite Scaling
        scale_label = font.render("SPRITE SCALING:", True, (200, 200, 200))
        scale_val = font.render(f"{config.SPRITE_SCALING}x", True, (135, 242, 255))
        screen.blit(scale_label, (container_rect.x + 30, start_y + spacing))
        screen.blit(scale_val, (container_rect.x + 475, start_y + spacing))

        # Item 3: Debug Mode Toggle
        dbg_label = font.render("DEBUG OVERLAY:", True, (200, 200, 200))
        dbg_val_str = "[ON]" if config.debug else "[OFF]"
        dbg_val_color = (50, 168, 82) if config.debug else (166, 51, 51)
        dbg_val = font.render(dbg_val_str, True, dbg_val_color)
        
        dbg_row_rect = pygame.Rect(container_rect.x + 20, start_y + 2 * spacing - 8, 680, 42)
        _state["debug_rect"] = dbg_row_rect
        
        if _state["hover_item"] == "debug":
            pygame.draw.rect(screen, (30, 45, 65), dbg_row_rect, border_radius=6)
            pygame.draw.rect(screen, (135, 242, 255), dbg_row_rect, width=1, border_radius=6)

        screen.blit(dbg_label, (container_rect.x + 30, start_y + 2 * spacing))
        screen.blit(dbg_val, (container_rect.x + 440, start_y + 2 * spacing))

        # Divider line
        div_y = start_y + 3 * spacing + 10
        pygame.draw.line(screen, (60, 80, 110), (container_rect.x + 30, div_y), (container_rect.x + 690, div_y), 2)

        # Section: Controls Reference
        ctrl_hdr = font.render("CONTROLS REFERENCE", True, (219, 212, 53))
        screen.blit(ctrl_hdr, (container_rect.x + 30, div_y + 20))

        controls_list = [
            ("MOVE SHIP", "W/A/S/D"),
            ("SHOOT", "SPACE/Z"),
            ("DEBUG TOGGLE", "F12"),
            ("RESTART RUN", "R"),
        ]

        for idx, (action, key_name) in enumerate(controls_list):
            row_y = div_y + 60 + idx * 35
            act_surf = font.render(action, True, (160, 175, 195))
            key_surf = font.render(key_name, True, (255, 255, 255))
            screen.blit(act_surf, (container_rect.x + 30, row_y))
            screen.blit(key_surf, (container_rect.x + 500, row_y))

    # 3. Bottom Back Button
    back_rect = pygame.Rect(center_x - 120, config.Screen.Size.h - 80, 240, 44)
    _state["back_rect"] = back_rect

    is_hover = (_state["hover_item"] == "back")
    bg_col = (45, 30, 35) if is_hover else (30, 25, 35)
    border_col = (255, 135, 135) if is_hover else (135, 242, 255)

    pygame.draw.rect(screen, bg_col, back_rect, border_radius=6)
    pygame.draw.rect(screen, border_col, back_rect, width=1, border_radius=6)

    if font:
        back_surf = font.render("BACK", True, (255, 255, 255))
        screen.blit(back_surf, back_surf.get_rect(center=back_rect.center))


class OptionsScene(BaseScene):
    """Class wrapper for Options scene."""

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
