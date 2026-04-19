# Breaker Game
# Rafal Zacher
# 21/02/2019
# Version 2

# Import external library
import pygame
import random
from os import path

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

# Define my frames per second
FPS = 30

# Basic colours - these are constant
# Defined in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
colors = [RED, GREEN, BLUE, YELLOW]




##################################
BRICK_HEIGHT = 15
PADDING = 1

brick_rows = 2
brick_columns = 3

score = 0

# font_name = pygame.font.Font(path.join(img_folder,"Duck_in_Shipah.ttf", 50))
font_name = pygame.font.match_font("arial")
###################################


# Title of my game
TITLE = "Basic Game Ball"



#####################################
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect .midtop = (x, y)
    surf.blit(text_surface, text_rect)


def show_scores():
    draw_text(game_play_screen, "Score: {}". format(score), 22, 50, 300)
    draw_text(game_play_screen, "Bricks Remaining: {}".format(len(all_game_bricks)), 22, 50, 330)
#####################################


# Self means to use the object within the class - self relates to only one instance
# Creates a object
class Ball(pygame.sprite.Sprite):
    # Sprite for the ball
    def __init__(self):  # Initialize the object once when the program runs
        # Must call the PyGame sprite init
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(image_folder, "rainbow_ball.png")).convert()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image.set_colorkey(BLACK)      # If any of the background colour is black make it transparent
        self.rect = self.image.get_rect()   # Provides a rectangle set to the ball's surface
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

    def reverse(self):
        self.y_speed = self.y_speed * -1

    def paddle_hit(self, game_paddle):
        self.x_speed = 8 * ((self.rect.centerx - (game_paddle.rect.left + paddle.rect.width / 2)) / paddle.rect.width)




######################################################
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # every sprite must have an image and a rect
        self.image = pygame.Surface((75, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        self.x_speed = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
            self.x_speed = -5
        if key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
            self.x_speed = 5
        self.rect.x += self.x_speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.set_colorkey(BLACK)
        self.image.fill(random.choice(colors))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
###############################################


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



##############################
pygame.mixer.music.load(path.join(sound_folder, "entering_the_skies.mp3"))
pygame.mixer.music.set_volume(0.2)
bang_sound = pygame.mixer.Sound(path.join(sound_folder, "boom1.wav"))
##############################

# Creates an array to store all the sprites
all_game_sprites = pygame.sprite.Group()
all_game_paddle = pygame.sprite.Group()
all_game_bricks = pygame.sprite.Group()

# Create the actual ball
game_ball = Ball()

# Add ball to sprite group
all_game_sprites.add(game_ball)
paddle = Paddle()
all_game_sprites.add(paddle)
all_game_paddle.add(paddle)



##############################
brick_width = (WIDTH // brick_columns) - 1
for i in range(brick_rows):
    for j in range(brick_columns):
        x = (j * (brick_width + PADDING)) + PADDING
        y = (i * (BRICK_HEIGHT + PADDING)) + PADDING
        brick = Brick(x, y, brick_width, BRICK_HEIGHT)
        all_game_sprites.add(brick)
        all_game_bricks.add(brick)


pygame.mixer.music.play(loops=-1)
##############################

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


    #####################################
    hits = pygame.sprite.spritecollide(game_ball, all_game_bricks, True)
    if hits:
        score += 5
        game_ball.reverse()
        bang_sound.play()

    if game_ball.rect.top < 1:
        score -= 2

    # check for collision between ball and the paddle
    hits = pygame.sprite.spritecollide(game_ball, all_game_paddle, False)
    if hits:
        # hit the paddle
        game_ball.reverse()
        game_ball.paddle_hit(paddle)
    elif game_ball.rect.bottom > HEIGHT:
        running = False
    ##################################

    # Render - this draws to the buffer not to the screen
    game_play_screen.fill(BLACK)    # Sets the background colour to black
    show_scores()
    all_game_sprites.draw(game_play_screen)     # Draws the sprites to the screen
    pygame.display.flip()   # Displays whats in the buffer to the screen

pygame.quit()   # Closes the game
