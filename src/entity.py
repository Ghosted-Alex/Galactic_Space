"""Module for Entities"""

import pygame

from . import assets
import config

class Player:
    """Instance Class for player"""
    def __init__(self, x: int, y: int, color: int = 0):
        self.x = x
        self.y = y
        self.speed = 8
        self.health = 100
        self.health_drain = 100
        self.energy = 100
        self.texture = None
        self.invincible = False

        # Logic to pick texture based on the 'color' (color/type) argument
        if color == 0:
            self.texture = assets.Textures.player0
            print("Texture Set Blue")
        else:
            self.texture = assets.Textures.player_blank
            print("Texture Set None")

        print(self.texture)

        # This creates a Rect exactly the size of your image
        self.rect = self.texture.get_rect(center=(self.x, self.y))
        
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
    def __init__(self, x: int, y: int, enemy_type: int, shield: bool = False):
        self.x = x
        self.y = y
        self.start_y = y # Store the initial Y for wave patterns
        self.enemy_type = enemy_type
        self.isAlive = True
        self.shield = shield
        
        if self.enemy_type == 0:
            self.image = assets.Textures.enemy0
            self.health = 1
        elif self.enemy_type == 1:
            self.image = assets.Textures.enemy1
            self.health = 1
        elif self.enemy_type == 2:
            self.image = assets.Textures.enemy0
            self.health = 3
        
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
        self.max_health = self.health
        
        # Unique attributes based on type
        self.speed = 3 if enemy_type == 0 else 5
        self.angle = 0 # Used for math-based movement

    def move(self):
        """Updates position based on enemy_type"""
        if self.enemy_type == 0: # Standard Grunt
            self.x -= self.speed

        elif self.enemy_type == 1: # The "Fast Diver"
            self.x -= self.speed + 4
            # Slight drift towards center
            if self.y < 400: self.y += 1
            else: self.y -= 1

        elif self.enemy_type == 2: # The "Waver" (Sine Wave) - Also includes Health so it takes more than 1 shot to kill
            self.x -= self.speed - 1
            self.angle += 0.1
            # Move side-to-side using a sine wave
            self.y = self.start_y + config.math.sin(self.angle) * 50

    def update(self):
        # Call move and then update the rect
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface):
        if self.enemy_type == 0:
            img = pygame.transform.flip(self.image, True, False)
        elif self.enemy_type == 2:
            img = pygame.transform.flip(self.image, True, False)
        else:
            img = self.image
        
        self.shield_image = assets.Textures.shield
        
        if self.shield:
            shield_rect = assets.Textures.shield.get_rect(
                right=self.rect.left + 5, # Slightly overlapping the left side
                centery=self.rect.centery
            )
            surface.blit(assets.Textures.shield, shield_rect)

        surface.blit(img, self.rect) 
        
        bar_width = 30
        bar_height = 4
        # Calculate health percentage
        health_pct = self.health / self.max_health
        
        # Position: Center it under the enemy, 2 pixels below the sprite
        bar_x = self.rect.centerx - (bar_width // 2)
        bar_y = self.rect.bottom + 2
        
        # Draw background (Red)
        pygame.draw.rect(surface, (200, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        # Draw current health (Green)
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_width * health_pct, bar_height))
        # ---------------------------------
        
        if config.debug:
            pygame.draw.rect(surface, (255, 51, 51), self.rect, 1)

# armada = [] #create empty list
# for i in range (4): #handles rows
#     for j in range (14): #handles columns
#         armada.append(Enemy(j*60+50, i*50+50, assets.Textures.Enemy.enemy0, 0)) #push Enemy objects into list

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")