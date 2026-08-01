"""Starfield Module"""

import random

class Generate:
    def __init__(self, width, height, num_stars=40):
        self.width = width
        self.height = height
        self.stars = []
        
        for _ in range(num_stars):
            # star = [x, y, speed]
            # Slower stars (speed 1) are further away; Faster stars (speed 3) are closer
            speed = random.randint(1, 3) 
            self.stars.append([random.randrange(0, width), random.randrange(0, height), speed])

    def update(self):
        for star in self.stars:
            # Move based on speed
            star[0] -= star[2] 
            
            if star[0] < 0:
                star[0] = self.width  # Reset to the right edge
                star[1] = random.randrange(0, self.height) # Pick a new random Y

    def draw(self, surface):
        for star in self.stars:
            # Parallax visual trick: Faster/closer stars are brighter/larger
            # 255 = white (close), 100 = dark gray (far)
            brightness = 100 + (star[2] * 50) 
            color = (brightness, brightness, brightness)
            surface.set_at((star[0], star[1]), color)