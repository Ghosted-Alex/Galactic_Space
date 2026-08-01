"""Module for Animations"""

import config
from . import assets
import time
import pygame

class ShootEffect:
    def __init__(self, x, y):
        self.anim = Animation(
            frames=[], 
            sprite_sheet=assets.Textures.effect_shoot, 
            frame_size=(32, 32)
        )
        self.rect = pygame.Rect(x, y, 32, 32)
        
        # Calculate total lifetime based on frame count and duration
        total_frames = self.anim.get_total_frames()
        self.lifetime = total_frames * self.anim.frame_duration
        self.start_time = time.time()

    def update(self):
        self.anim.update()

    def draw(self, screen):
        screen.blit(self.anim.get_current_frame(), self.rect)
        
    def is_expired(self):
        """Checks if the animation has played through all its frames."""
        return time.time() - self.start_time > self.lifetime

class Animation:
    def __init__(self, frames, frame_duration=0.1, sprite_sheet=None, frame_size=(32, 32)):
        self.frames = frames  # If using individual images, this is a list of Surfaces
        self.sprite_sheet = sprite_sheet # If using a sheet, this is the master Surface
        self.frame_size = frame_size # (width, height) of each frame
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.last_update = time.time()

    def _get_frame_from_sheet(self, index):
        """Extracts a frame from a sprite sheet."""
        # Calculate row and column based on index
        cols = self.sprite_sheet.get_width() // self.frame_size[0]
        row = index // cols
        col = index % cols
        rect = pygame.Rect(col * self.frame_size[0], row * self.frame_size[1], 
        self.frame_size[0], self.frame_size[1])
        
        # Create a surface to hold the frame
        frame = pygame.Surface(self.frame_size, pygame.SRCALPHA)
        frame.blit(self.sprite_sheet, (0, 0), rect)
        return frame

    def update(self):
        now = time.time()
        if now - self.last_update > self.frame_duration:
            # Determine number of frames based on source
            num_frames = len(self.frames) if self.sprite_sheet is None else \
                         (self.sprite_sheet.get_width() // self.frame_size[0]) * \
                         (self.sprite_sheet.get_height() // self.frame_size[1])
            
            self.current_frame = (self.current_frame + 1) % num_frames
            self.last_update = now

    def get_current_frame(self):
        if self.sprite_sheet:
            return self._get_frame_from_sheet(self.current_frame)
        return self.frames[self.current_frame]

    def get_total_frames(self):
        """Returns the total number of frames in the animation."""
        if self.sprite_sheet:
            # Calculate frames based on sprite sheet dimensions
            cols = self.sprite_sheet.get_width() // self.frame_size[0]
            rows = self.sprite_sheet.get_height() // self.frame_size[1]
            return cols * rows
        return len(self.frames)

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")
    