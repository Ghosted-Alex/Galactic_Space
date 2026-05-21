"Module for Bullet"

import subprocess
import pygame
import src.config as config
import src.assets as assets

class Normal:
    def __init__(self, x, y, image=None):
        self.image = image if image else assets.Textures.Bullet.blank
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # Move the rect, which is the "source of truth" for position
        self.rect.y -= self.speed

    def draw(self, surface):
        # Draw the actual image at the rect's current position
        surface.blit(self.image, self.rect)

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")