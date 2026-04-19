import pygame
from os import path


class Ball(pygame.sprite.Sprite):
    """Defines the ball class, which represents the object to break bricks."""
    HEIGHT = 0
    WIDTH = 0

    def __init__(self, image_folder, BLACK, CENTRE_X, CENTRE_Y, HEIGHT, WIDTH):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

        pygame.sprite.Sprite.__init__(self)

        # Loads the image and resizes it to the required specs.
        self.image = pygame.image.load(
            path.join(image_folder, "rainbow_ball.png")).convert()
        self.image = pygame.transform.scale(self.image, (32, 32))

        # If any of the background colour is black make it transparent.
        self.image.set_colorkey(BLACK)

        # Provides a rectangle set to the ball's surface
        self.rect = self.image.get_rect()

        # Place the ball in the middle of the screen
        self.rect.center = (CENTRE_X, CENTRE_Y)

        # Define the speed of the ball
        self.x_speed = 5
        self.y_speed = 5

    def update(self):
        """Every time the frame updates the ball will be re-drawn on the screen."""
        # Will change the position of the ball with the set speed.
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Change the direction of the ball if the ball hits the bottom.
        if self.rect.bottom > self.HEIGHT:
            self.y_speed = -5

        # Change the direction of the ball if the ball hits the top.
        if self.rect.top < 0:
            self.y_speed = 5

        # Change the direction of the ball if the ball hits the left side.
        if self.rect.left < 0:
            self.x_speed = 5

        # Change the direction of the ball if the ball hits the right side.
        if self.rect.right > self.WIDTH:
            self.x_speed = -5

    def reverse(self):
        """Reverses the direction of the vertical speed of the object."""
        self.y_speed = self.y_speed * -1

    def paddle_hit(self, Paddle):
        """Adjusts the ball's horizontal speed based on the position where it hits the paddle."""
        self.x_speed = 8 * \
            ((self.rect.centerx - (Paddle.rect.left +
             Paddle.rect.width / 2)) / Paddle.rect.width)
