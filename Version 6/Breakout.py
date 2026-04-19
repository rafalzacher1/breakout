import pygame
from os import path
from Brick import Brick
from Paddle import Paddle
from Ball import Ball
from Text import Text
from Progress import Progress

# Constants
WIDTH, HEIGHT = 480, 600
CENTRE_X, CENTRE_Y = WIDTH / 2, HEIGHT / 2
FPS = 30
BLACK = (0, 0, 0)
BRICK_ROWS, BRICK_COLUMNS = 2, 3
INITIAL_LEVEL, INITIAL_SCORE = 1, 0
TITLE = "Breakout"
PADDLE_CONTROL = True  # True is for keyboard and False is for mouse

# Initialize pygame and setup
def initialize_game():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(TITLE)
    return pygame.display.set_mode((WIDTH, HEIGHT)), pygame.time.Clock()

def load_assets():
    # Locate the folders
    game_folder = path.dirname(__file__)
    image_folder = path.join(game_folder, "Assets")    # Images folder
    sound_folder = path.join(game_folder, "Sounds")    # Sounds folder
    
    # Load music and sounds
    pygame.mixer.music.load(path.join(sound_folder, "entering_the_skies.mp3"))
    pygame.mixer.music.set_volume(0.2)    # Sets the sound to specific volume
    bang_sound = pygame.mixer.Sound(path.join(sound_folder, "boom.wav"))

    # Load background image
    background = pygame.image.load(path.join(image_folder, "Mountain.gif")).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))    # Sets the area for the image
    background_rect = background.get_rect()
    
    return image_folder, sound_folder, background, background_rect, bang_sound

def create_sprites(image_folder):
    # Create sprite groups
    all_game_sprites = pygame.sprite.Group()
    all_game_paddle = pygame.sprite.Group()
    all_game_bricks = pygame.sprite.Group()

    # Create the actual ball
    game_ball = Ball(image_folder, BLACK, CENTRE_X, CENTRE_Y, HEIGHT, WIDTH)
    all_game_sprites.add(game_ball)

    # Create and add the paddle
    paddle = Paddle(image_folder, WIDTH, HEIGHT)
    all_game_sprites.add(paddle)
    all_game_paddle.add(paddle)

    return all_game_sprites, all_game_paddle, all_game_bricks, game_ball, paddle

def main():
    # Initialize game components
    game_play_screen, game_clock = initialize_game()
    image_folder, sound_folder, background, background_rect, bang_sound = load_assets()
    all_game_sprites, all_game_paddle, all_game_bricks, game_ball, paddle = create_sprites(image_folder)

    # Start background music
    pygame.mixer.music.play(loops=-1)

    # Create Progress object
    progress = Progress(HEIGHT, WIDTH, CENTRE_X, CENTRE_Y, game_ball, INITIAL_LEVEL, all_game_bricks, all_game_sprites, image_folder, game_play_screen)
    
    # Initialize game state
    progress.level_over(game_play_screen, background, background_rect, game_clock, FPS, INITIAL_SCORE, INITIAL_LEVEL)
    progress.new_game()

    # Create Text object for score display
    text = Text(pygame.font.match_font("arial"), (0, 255, 0), game_play_screen, CENTRE_X, CENTRE_Y, HEIGHT)

    # Initialize score
    score = INITIAL_SCORE

    # Main game loop
    game_running = progress.show_game_start(game_clock, FPS, game_play_screen, background, background_rect, TITLE)
    
    while game_running:
        game_clock.tick(FPS)  # Maintain set FPS
        
        # Check if user has closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = True    # Close the loop

        # Update game state
        all_game_sprites.update()

        # Increase the score when a brick is hit
        hits = pygame.sprite.spritecollide(game_ball, all_game_bricks, True)
        if hits:
            score += 5
            game_ball.reverse()
            bang_sound.play()
        
        # Decrease the score when brick is missed
        if game_ball.rect.top < 1:
            score -= 2

        # Check for collision between ball and paddle
        hits = pygame.sprite.spritecollide(game_ball, all_game_paddle, False)
        if hits:
            # Ball hit the paddle
            game_ball.reverse()
            game_ball.paddle_hit(paddle)
        elif game_ball.rect.bottom > HEIGHT:
            game_running = progress.show_game_over(game_play_screen, background, background_rect, game_clock, FPS, score, INITIAL_LEVEL)

        # End of level
        if len(all_game_bricks) == 0:
            game_running = progress.level_over()

        # Render the game
        game_play_screen.fill(BLACK)    # Set the background color to black
        game_play_screen.blit(background, background_rect)
        text.show_scores(all_game_bricks, score)
        all_game_sprites.draw(game_play_screen)
        pygame.display.flip()   # Update the display with new frame

    pygame.quit()   # Close the game

if __name__ == "__main__":
    main()
