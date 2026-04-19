import pygame
from os import path


class Paddle(pygame.sprite.Sprite):
    """Defines the paddle class, which represents the player."""
    paddle_control = None
    WIDTH = 0


    def __init__(self,  image_folder, WIDTH, HEIGHT):
        self.paddle_control = True
        self.WIDTH = WIDTH

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75, 20))

        # Load the paddle image.
        self.image = pygame.image.load(
            path.join(image_folder, "Paddle.png")).convert()
        
        # Create a rectangle for collision detection
        self.rect = self.image.get_rect()

        # Position the paddle at the center-bottom of the window.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10


    def update(self):
        """Update the paddle's position based on user input."""
        self.x_speed = 0
        mouse_position = pygame.mouse.get_pos() # Grab the mouse position.
        key_state = pygame.key.get_pressed()

        # Checks which controls that user wants to use.
        if self.paddle_control:
            # Keyboard controls
            if key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
                self.x_speed = -5 # Move left
            if key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
                self.x_speed = 5 # Move right
        else:
            # Mouse controls
            if mouse_position[0] > 0 and mouse_position[0] < self.rect.x:
                self.x_speed = -5 # Move left
            if mouse_position[0] > 0 and mouse_position[0] > self.rect.right:
                self.x_speed = 5 # Move right

        # Update paddle's x position based on the speed
        self.rect.x += self.x_speed

        # Boundary checking to ensure paddle stays within the game window
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH