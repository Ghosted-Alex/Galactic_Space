"""Module for Powerups """
from . import assets
import config
import pygame

class Spawn:
    def __init__(self, x: int, y: int, powerup_type: int):
        self.x = x
        self.y = y
        self.type = powerup_type

        # Fetch dynamically or fallback safely
        if self.type == 0:
            self.image = getattr(assets.Textures, 'wrench', None)
        elif self.type == 1:
            self.image = getattr(assets.Textures, 'power_wrench', None)
        elif self.type == 2:
            self.image = getattr(assets.Textures, 'energy', None)

        # Ultimate fallback if it's still somehow None
        if self.image is None:
            self.image = pygame.Surface((32, 32))
            self.image.fill((255, 0, 255))

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 3

    def move(self):
        """Updates position based on type"""
        if self.type == 0: # Standard Wrench
            self.x -= self.speed
        elif self.type == 1: # Power Wrench
            self.x -= (self.speed + 1)
        elif self.type == 2: # Energy Cell
            self.x -= (self.speed - 1)

    def update(self):
        # Call move and then update the rect
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        # Use self.rect instead of (self.x, self.y)
        surface.blit(self.image, self.rect) 
        
        if config.debug:
            pygame.draw.rect(surface, (255, 51, 51), self.rect, 1)