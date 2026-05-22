"Module for Entities"

import pygame

from . import assets
import config

class Player:
    """Instance Class for player"""
    def __init__(self, x: int, y: int, c: int = 0):
        self.x = x
        self.y = y
        self.speed = 8
        self.health = 100
        self.health_drain = 100
        self.energy = 100
        self.texture = None
        self.invincible = False

        # Logic to pick texture based on the 'c' (color/type) argument
        if c == 0:
            self.texture = assets.Textures.Player.player0
        else:
            self.texture = assets.Textures.Player.player_blank

        # This creates a Rect exactly the size of your image
        self.rect = self.texture.get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        """Blits the player texture\n
        Draws a white hitbox rectangle (if debug mode is on)"""
        # Draw the actual ship sprite
        surface.blit(self.texture, self.rect)
        # Draw the white outline (useful for debugging hitboxes!)
        if config.debug:
            pygame.draw.rect(surface, (51, 255, 51), self.rect, 1)

    # In player.py -> handle_input
    def handle_input(self, key):
        # 1. Get Input
        up = key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_i] or key[pygame.K_o]
        down = key[pygame.K_s] or key[pygame.K_DOWN] or key[pygame.K_k]
        left = key[pygame.K_a] or key[pygame.K_LEFT] or key[pygame.K_j]
        right = key[pygame.K_d] or key[pygame.K_RIGHT] or key[pygame.K_l]
        a = key[pygame.K_z] or key[pygame.K_SPACE]
        b = key[pygame.K_x] or key[pygame.K_RETURN]

        # 2. Apply Movement
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
        if left:
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed

        # self.rect.x += (right - left) * 15
        # self.rect.y += (down - up) * 15

        # 3. The Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.Screen.Size.w:
            self.rect.right = config.Screen.Size.w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > config.Screen.Size.h-45:
            self.rect.bottom = config.Screen.Size.h-45

class Enemy:
    def __init__(self, x: int, y: int, image: pygame.surface.Surface, enemy_type: int):
        self.x = x
        self.y = y
        self.start_x = x # Store the initial X for wave patterns
        self.image = image
        self.enemy_type = enemy_type
        self.isAlive = True
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
        # Unique attributes based on type
        self.speed = 3 if enemy_type == 0 else 5
        self.angle = 0 # Used for math-based movement

    def move(self):
        """Updates position based on enemy_type"""
        if self.enemy_type == 0: # Standard Grunt
            self.y += self.speed

        elif self.enemy_type == 1: # The "Waver" (Sine Wave)
            self.y += self.speed - 1
            self.angle += 0.1
            # Move side-to-side using a sine wave
            self.x = self.start_x + config.math.sin(self.angle) * 50

        elif self.enemy_type == 2: # The "Fast Diver"
            self.y += self.speed + 4
            # Slight drift towards center
            if self.x < 400: self.x += 1
            else: self.x -= 1

    def update(self):
        # Call move and then update the rect
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
    # Flip the sprite for enemies (facing down)
        img = pygame.transform.flip(self.image, False, True)
        # Use self.rect instead of (self.x, self.y)
        surface.blit(img, self.rect) 
        
        if config.debug:
            pygame.draw.rect(surface, (255, 51, 51), self.rect, 1)

# armada = [] #create empty list
# for i in range (4): #handles rows
#     for j in range (14): #handles columns
#         armada.append(Enemy(j*60+50, i*50+50, assets.Textures.Enemy.enemy0, 0)) #push Enemy objects into list

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")