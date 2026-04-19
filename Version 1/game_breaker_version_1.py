# Breaker Game
# Rafal Zacher
# 08/02/2019
# Version 1

# Import external library
import pygame

# Define game surface size
WIDTH = 480
HEIGHT = 600

# Defines the Y and X axes
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

# Define my frames per second
FPS = 30

# Basic colours - these are constant
# Defined in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Title of my game
TITLE = "Basic Game Ball"


# Self means to use the object within the class - self relates to only one instance
# Creates a object
class Ball(pygame.sprite.Sprite):
    # Sprite for the ball
    def __init__(self):  # Initialize the object once when the program runs
        # Must call the PyGame sprite init
        pygame.sprite.Sprite.__init__(self)
        # Every sprite must have an image and a rectangle - a rectangle is the surface for the image
        self.image = pygame.Surface((40, 40))     # Defines the rectangle for the ball
        self.image.set_colorkey(BLACK)      # If any of the background colour is black make it transparent
        self.rect = self.image.get_rect()   # Provides a rectangle set to the ball's surface
        self.radius = int(self.rect.width * 0.8 / 2)   # Sets radius of the ball
        pygame.draw.circle(self.image, WHITE, self.rect.center, self.radius)   # Draws the ball inside the rectangle
        self.rect.center = (CENTRE_X, CENTRE_Y)     # Place the ball in the middle of the screen
        # Define the speed of the ball
        self.x_speed = 5
        self.y_speed = 5

    # Every time the frame updates the ball will be re-drawn on the screen
    def update(self):
        # Will change the position of the ball with the set speed
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        # Change the direction of the ball if the ball hits the bottom
        if self.rect.bottom > HEIGHT:
            self.y_speed = -5
        # Change the direction of the ball if the ball hits the top
        if self.rect.top < 0:
            self.y_speed = 5
        # Change the direction of the ball if the ball hits the left side
        if self.rect.left < 0:
            self.x_speed = 5
        # Change the direction of the ball if the ball hits the right side
        if self.rect.right > WIDTH:
            self.x_speed = -5


# Initialize the game engine
pygame.init()

# Initialize the music mixer
pygame.mixer.init()

# Create the game play surface
game_play_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Set the game clock ticking
# Needed to maintain FPS
game_clock = pygame.time.Clock()

# Creates an array to store all the sprites
all_game_sprites = pygame.sprite.Group()

# Create the actual ball
game_ball = Ball()

# Add ball to sprite group
all_game_sprites.add(game_ball)

# Now the basic game loop
game_running = True
while game_running:
    # Maintain set FPS - delay the computer to maintain this
    game_clock.tick(FPS)
    # Check if user has closed the window
    for game_event in pygame.event.get():   # This looks for an input from the user
        if game_event.type == pygame.QUIT:    # Checks if the user clicked on the close window - uses a constant from pygame
            game_running = False    # Close the loop

    # Update
    all_game_sprites.update()

    # Render - this draws to the buffer not to the screen
    game_play_screen.fill(BLACK)    # Sets the background colour to black
    all_game_sprites.draw(game_play_screen)     # Draws the sprites to the screen
    pygame.display.flip()   # Displays whats in the buffer to the screen

pygame.quit()   # Closes the game
