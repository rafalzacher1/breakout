import pygame
from os import path


# This defines the paddle.
class Paddle(pygame.sprite.Sprite):
    paddle_control = None
    WIDTH = 0


    def __init__(self,  image_folder, WIDTH, HEIGHT):
        self.paddle_control = True
        self.WIDTH = WIDTH

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75, 20))
        self.image = pygame.image.load(
            path.join(image_folder, "Paddle.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10


    def update(self):
        # Reset horizontal speed to zero at the start of the update.
        self.x_speed = 0

        # Get the current position of the mouse.
        mouse_position = pygame.mouse.get_pos() # Grab the mouse position.
        
        # Get the current state of all keyboard keys.
        key_state = pygame.key.get_pressed()

        # Check if the paddle control mode is set to keyboard.
        if self.paddle_control:
            # Move paddle left if left arrow key or 'A' key is pressed.
            if key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
                self.x_speed = -5

            # Move paddle right if right arrow key or 'D' key is pressed.
            if key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
                self.x_speed = 5
        else:
            # If paddle control mode is set to mouse, move paddle based on mouse position.
            # Move paddle left if the mouse is to the left of the paddle's left edge.
            if mouse_position[0] > 0 and mouse_position[0] < self.rect.x:
                self.x_speed = -5

            # Move paddle right if the mouse is to the right of the paddle's right edge.
            if mouse_position[0] > 0 and mouse_position[0] > self.rect.right:
                self.x_speed = 5

        # Update the paddle's position based on the calculated horizontal speed.
        self.rect.x += self.x_speed

        # Ensure the paddle does not move off the left edge of the screen.
        if self.rect.left < 0:
            self.rect.left = 0

        # Ensure the paddle does not move off the right edge of the screen.
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH