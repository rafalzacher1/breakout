import pygame
from os import path

class Brick(pygame.sprite.Sprite):
    """Defines the Brick class, which represents a single brick in the game."""
    
    def __init__(self, x, y, width, height, image_folder):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))

        # Set the color key for the surface to be transparent (black color)
        self.image.set_colorkey((0, 0, 0))

        # Load the brick image from the specified folder
        self.image = pygame.image.load(
            path.join(image_folder, "Brick.png")).convert()
        
        # Scale the image to the specified width and height
        self.image = pygame.transform.scale(self.image, (width, height))

        # Get the rectangle area of the image
        self.rect = self.image.get_rect()

        # Set the position of the brick based on the provided x and y coordinates.
        self.rect.x = x
        self.rect.y = y
