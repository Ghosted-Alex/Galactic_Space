"""Controls Module"""

import pygame

import config

def single_press(event: pygame.event.Event, key: config.KeyLike, input_type: str = "none") -> bool:
    """Checks if a specific key was pressed once (KEYDOWN)."""
    if event.type != pygame.KEYDOWN:
        return False
    if isinstance(key, (tuple, list)):
        return event.key in key

    return event.key == key

def repeat_press(key: config.KeyLike) -> bool:
    """Checks if a key is currently held down."""
    
    keys = pygame.key.get_pressed()
    
    return keys[key]

def check_combo(event: pygame.event.Event, keys: list[int]) -> bool:
    """
    Checks if a specific combo was completed.
    
    Args:
        event: The current KEYDOWN event.
        keys: A list of key constants (e.g., [pygame.K_F12, pygame.K_1]).
        The last key in this list is treated as the 'trigger' key.
    """
    if event.type != pygame.KEYDOWN:
        return False

    # 1. Check if the trigger key (the last one in the list) is the one just pressed
    trigger_key = keys[-1]
    if event.key != trigger_key:
        return False
    
    # 2. Check if all other keys in the list are currently being held down
    pressed_keys = pygame.key.get_pressed()
    for key in keys[:-1]:
        if not pressed_keys[key]:
            return False
            
    return True