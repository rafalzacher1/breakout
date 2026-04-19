import pygame
import random
from Text import Text
from Brick import Brick

class Progress():
    Text = None
    HEIGHT = None
    WIDTH = None
    CENTRE_Y = None
    CENTRE_X = None
    game_ball = None
    level = None
    all_game_bricks = None
    all_game_sprites = None
    image_folder = None

    def __init__(self, HEIGHT, WIDTH, CENTRE_X, CENTRE_Y, game_ball, level, all_game_bricks, all_game_sprites, image_folder, game_play_screen):
        self.Text = Text(pygame.font.match_font("arial"), (0, 255, 0), game_play_screen, CENTRE_X, CENTRE_Y, HEIGHT)
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.CENTRE_Y = CENTRE_Y
        self.CENTRE_X = CENTRE_X
        self.Brick = Brick
        self.game_ball = game_ball
        self.level = level
        self.all_game_bricks
        self.all_game_bricks = all_game_bricks
        self.all_game_sprites = all_game_sprites
        self.image_folder = image_folder

    
    # This is the start page, the page that the player sees first
    def show_game_start(self, game_clock, FPS, game_play_screen, background, background_rectangle, TITLE):
        paddle_control = True
        game_running = True
        waiting = True

        # The player is held at this screen until specific event is triggered
        while waiting:
            game_clock.tick(FPS)
            game_play_screen.blit(background, background_rectangle)

            # Shows the title of the game
            self.Text.draw_text(game_play_screen, TITLE, 64, self.CENTRE_X, self.CENTRE_Y - 220)
            # Enables the user to change through controls
            
            self.Text.show_game_controlls(paddle_control)

            # This executes specific function with accordance to specific events
            pygame.display.flip()
            for cross in pygame.event.get():
                if cross.type == pygame.QUIT:
                    game_running = False
                    waiting = False
                key_state = pygame.key.get_pressed()
                if key_state[pygame.K_m]:
                    paddle_control = False
                if key_state[pygame.K_k]:
                    paddle_control = True
                if key_state[pygame.K_y]:
                    game_running = True
                    waiting = False
        return game_running


    # This tells the player that they have lost
    # It provides them with information from the current game play
    def show_game_over(self, game_play_screen, background, background_rectangle, game_clock, FPS, score, level):
        # score, level
        running = True
        # Sets the background
        game_play_screen.blit(background, background_rectangle)
        
        self.Text.show_game_over(score, level)
        
        pygame.display.flip()

        # Checks if the user want to carry on playing
        waiting = True
        while waiting:
            game_clock.tick(FPS)
            # Quits the game
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    waiting = False
                    running = False

            # Resets the game to the beginning
            key_state = pygame.key.get_pressed()    # Checks for any events in the code
            if key_state[pygame.K_y]:
                waiting = False
                level = 1
                score = 0
                self.new_game()
        return running


    # This shows the completed level to the user
    def level_over(self, game_play_screen, background, background_rectangle, game_clock, FPS, score, level):
        # global score, level

        running = True
        # Sets the background
        game_play_screen.blit(background, background_rectangle)
        
        self.Text.show_level_over(score, level)

        pygame.display.flip()

        # Checks if the user want to carry on playing
        waiting = True
        while waiting:
            game_clock.tick(FPS)
            for game_event in pygame.event.get():    # Checks for any events in the code
                if game_event.type == pygame.QUIT:
                    waiting = False
                    running = False
            key_state = pygame.key.get_pressed()    # Looks for a specific key pressed
            # Increases the level
            if key_state[pygame.K_y]:
                waiting = False
                level += 1
                self.new_game()
        return running


    def new_game(self):
        global brick_rows, brick_columns

        # Generates more bricks per level
        brick_rows = 2 * self.level
        brick_columns = 3 * self.level

        BRICK_HEIGHT = 15
        PADDING = 5
        

        # This resets the bricks to beginning when user starts again
        for brick in self.all_game_bricks:
            brick.kill()    # Removes all bricks from memory

        # Generates the bricks
        brick_width = (self.WIDTH // brick_columns) - 1

        for i in range(brick_rows):
            for j in range(brick_columns):
                x = (j * (brick_width + PADDING)) + PADDING
                y = (i * (BRICK_HEIGHT + PADDING)) + PADDING
                brick = Brick(x, y, brick_width, BRICK_HEIGHT, self.image_folder)
                self.all_game_sprites.add(brick)
                self.all_game_bricks.add(brick)

        # Randomly position the ball on the screen on each level
        self.game_ball.centerx = random.randint(50, self.WIDTH - 50)
        self.game_ball.rect.centery = random.randint(self.CENTRE_Y, self.HEIGHT - 300)    