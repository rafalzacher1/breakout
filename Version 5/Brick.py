import pygame
from os import path

# This defines the brick class.
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_folder):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.image.load(
            path.join(image_folder, "Brick.png")).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
