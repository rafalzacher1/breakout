# Breaker Game
# Rafal Zacher
# 01/03/2019
# Version 5

# Import external library
import pygame
from os import path
from Brick import Brick;
from Paddle import Paddle;
from Ball import Ball;
from Text import Text;
from Progress import Progress;

# Locate the folders
game_folder = path.dirname(__file__)
image_folder = path.join(game_folder, "Assets")    # Images folder
sound_folder = path.join(game_folder, "Sounds")    # Sounds folder

# Define game surface size
WIDTH = 480
HEIGHT = 600

# Defines the Y and X axes
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

FPS = 30    # Define my frames per second

# Basic colours - these are constant
BLACK = (0, 0, 0)

brick_rows = 2
brick_columns = 3

level = 1    # Defines the variable for level and sets it to one
score = 0    # Defines the variable for score and sets it to zero

# Control the paddle with either mouse of keyboard
paddle_control = True    # True is for keyboard and False is for mouse

TITLE = "Breakout"    # Title of my game

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

# Loads music into the game
pygame.mixer.music.load(path.join(sound_folder, "entering_the_skies.mp3"))
pygame.mixer.music.set_volume(0.2)    # Sets the sound to specific volume
bang_sound = pygame.mixer.Sound(path.join(sound_folder, "boom.wav"))

# Loads image into th game
background = pygame.image.load(
    path.join(image_folder, "Mountain.gif")).convert()
background = pygame.transform.scale(
    background, (WIDTH, HEIGHT))    # Sets the are for the image
background_rectangle = background.get_rect()

# Creates an array to store all the sprites
all_game_sprites = pygame.sprite.Group()
all_game_paddle = pygame.sprite.Group()
all_game_bricks = pygame.sprite.Group()

# Create the actual ball
game_ball = Ball(image_folder, BLACK, CENTRE_X, CENTRE_Y, HEIGHT, WIDTH)

# Add ball and paddle to sprite group
all_game_sprites.add(game_ball)
Paddle = Paddle(image_folder, WIDTH, HEIGHT)
all_game_sprites.add(Paddle)
all_game_paddle.add(Paddle)

# Start the background music
pygame.mixer.music.play(loops=-1)

Progress = Progress(HEIGHT, WIDTH, CENTRE_X, CENTRE_Y, game_ball, level, all_game_bricks, all_game_sprites, image_folder, game_play_screen)

Progress.level_over(game_play_screen, background, background_rectangle, game_clock, FPS, score, level)

Progress.new_game()

# Now the basic game loop
game_running = Progress.show_game_start(game_clock, FPS, game_play_screen, background, background_rectangle, TITLE)

# Define the text's specification
Text = Text(pygame.font.match_font("arial"), (0, 255, 0), game_play_screen, CENTRE_X, CENTRE_Y, HEIGHT)

while game_running:
    # Maintain set FPS - delay the computer to maintain this
    game_clock.tick(FPS)
    # Check if user has closed the window
    for game_event in pygame.event.get():   # This looks for an input from the user
        # Checks if the user clicked on the close window - uses a constant from pygame
        if game_event.type == pygame.QUIT:
            game_running = True    # Close the loop

    # Update
    all_game_sprites.update()

    # Increases the score when a brick is hit
    hits = pygame.sprite.spritecollide(game_ball, all_game_bricks, True)
    if hits:
        score += 5
        game_ball.reverse()
        bang_sound.play()

    # Decreases the score when brick is missed
    if game_ball.rect.top < 1:
        score -= 2

    # Check for collision between ball and the paddle
    hits = pygame.sprite.spritecollide(game_ball, all_game_paddle, False)
    if hits:
        # Hit the paddle
        game_ball.reverse()
        game_ball.paddle_hit(Paddle)
    elif game_ball.rect.bottom > HEIGHT:
        game_running = Progress.show_game_over(game_play_screen, background, background_rectangle, game_clock, FPS, score, level)

    # End of level
    if len(all_game_bricks) == 0:
        game_running = Progress.level_over()

    # Render - this draws to the buffer not to the screen
    game_play_screen.fill(BLACK)    # Sets the background colour to black
    game_play_screen.blit(background, background_rectangle)
    Text.show_scores(all_game_bricks, score)
    # Draws the sprites to the screen
    all_game_sprites.draw(game_play_screen)
    pygame.display.flip()   # Displays whats in the buffer to the screen

pygame.quit()   # Closes the game
