import pygame

import config

def single_press(event: pygame.event.Event, key: config.KeyLike) -> bool:
    """Checks if a specific key was pressed once (KEYDOWN)."""
    return event.type == pygame.KEYDOWN and event.key == key

def repeat_press(key: config.KeyLike) -> bool:
    """Checks if a key is currently held down."""
    keys = pygame.key.get_pressed()
    return keys[key]