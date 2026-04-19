# Basic Template
# Rafal Zacher
# 08/02/2019
# Version 0

# This can be used to make other games

# Import external library
import pygame

# Define game surface size
WIDTH = 480
HEIGHT = 600

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
TITLE = "Basic Game Template"

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

        # Render - this draws to the buffer not to the screen
        game_play_screen.fill(BLACK)    # Sets the background colour to black
        pygame.display.flip()   # Displays whats in the buffer to the screen

pygame.quit()   # Closes the game
