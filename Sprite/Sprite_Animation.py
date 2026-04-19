# Basic Template
# Rafal Zacher
# 01/03/2019
# Version 1

# Import external library
import pygame
import math
from os import path

# Locate the folders
game_folder = path.dirname(__file__)
image_folder = path.join(game_folder, "Assets")    # Images folder
sound_folder = path.join(game_folder, "Sounds")    # Sounds folder

# Define game surface size
WIDTH = 400
HEIGHT = 400

# Define my frames per second
FPS = 60

# Basic colours - these are constant
# Defined in RGB
BLACK = (0, 0, 0)

# Title of my game
TITLE = "Basic Sprite Template"

# create the game surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Defines the sprite
class Spritesheet():
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()    # Loads the image and converts the background to transparent

    def get_image(self, x, y, w, h):
        # Grabs the single image from the big sprite sheet
        image = pygame.Surface((w, h))    # Sets a rectangle for each image
        image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))    # Relates to the measurements in the sprite images
        return image


class Explode(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((93, 100))    # Defines the size of each image
        self.image.fill(BLACK)    # Fills the background to black
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)    # Centers all the images into one position
        self.frame = 1    # Sets the speed to change each image every frame
        self.last_update = pygame.time.get_ticks()
        self.sprite_sheet = sprite_sheet

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            frame_x = ((self.frame - 1) % 10) * self.rect.width
            frame_y = math.floor(self.frame / 10) * 100
            self.image = self.sprite_sheet.get_image(frame_x, frame_y, 93, 100)
            self.frame += 1
            if self.frame > 40:
                self.kill


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

all_sprites = pygame.sprite.Group()
sprite_sheet = Spritesheet(path.join(image_folder, "explosion.png"))
esound = pygame.mixer.Sound(path.join(sound_folder, "explosion.wav"))
explode = Explode(sprite_sheet)
all_sprites.add(explode)
esound.play()

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
        all_sprites.update()
        # Render - this draws to the buffer not to the screen
        game_play_screen.fill(BLACK)    # Sets the background colour to black
        all_sprites.draw(screen)    # Shows the sprite images on the screen
        pygame.display.flip()   # Displays whats in the buffer to the screen

pygame.quit()   # Closes the game
