"""Module for Bullet"""

from . import assets

class Normal:
    def __init__(self, x, y, btype=0):
        match btype:
            case 0:
                self.image = assets.Textures.bullet0
            case 1:
                self.image = assets.Textures.bullet0
            case 2:
                self.image = assets.Textures.bullet0
            case 3:
                self.image = assets.Textures.bullet0
            case _:
                self.image = assets.Textures.bullet_blank
        self.speed = 25
        self.rect = self.image.get_rect(midtop=(x, y))

    def update(self):
        # Move the rect, which is the "source of truth" for position
        self.rect.x += self.speed

    def draw(self, surface):
        # Draw the actual image at the rect's current position
        surface.blit(self.image, self.rect)

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")