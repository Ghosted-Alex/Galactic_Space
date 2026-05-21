"""Module for Powerups """
import src.assets as assets
import src.config as config
import pygame

class Spawn:
    def __init__(self, x: int, y: int, powerUpType: int):
        self.x = x
        self.y = y
        self.type = powerUpType

        if self.type == 0:
            self.image = assets.Textures.PowerUp.wrench
        elif self.type == 1:
            self.image = assets.Textures.PowerUp.power_wrench
        elif self.type == 2:
            self.image = assets.Textures.PowerUp.ammo

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 3

    def move(self):
        """Updates position based on type"""
        if self.type == 0: # Standard Wrench
            self.y += self.speed
        if self.type == 1:
            self.y += self.speed+1
        if self.type == 2:
            self.y += self.speed-1

    def update(self):
        # Call move and then update the rect
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        # Use self.rect instead of (self.x, self.y)
        surface.blit(self.image, self.rect) 
        
        if config.debug:
            pygame.draw.rect(surface, (255, 51, 51), self.rect, 1)