import pygame

class Text():
    """Defines text class, which represents all text drawn on the UI."""
    font_name = None
    colour = None
    game_play_screen = None
    CENTRE_X = None
    CENTRE_Y = None
    HEIGHT = None

    def __init__(self, font_name, colour, game_play_screen, CENTRE_X, CENTRE_Y, HEIGHT):
        self.font_name = font_name
        self.colour = colour
        self.game_play_screen = game_play_screen
        self.CENTRE_X = CENTRE_X
        self.CENTRE_Y = CENTRE_Y
        self.HEIGHT = HEIGHT

    def draw_text(self, surf, text, size, x, y):
        """Draws the text into the screen."""
        font = pygame.font.Font(self.font_name, size)

        # Sets the text to specific colour.
        text_surface = font.render(text, True, self.colour)
        text_rect = text_surface.get_rect()

        # Positions the text to specific location.
        text_rect.midtop = (x, y)

        # Draws each string into its own rectangle
        surf.blit(text_surface, text_rect)

    def show_scores(self, all_game_bricks, score):
        """Creates the text to show the score and bricks for the user."""
        self.draw_text(self.game_play_screen, "This Is Your Score: {}".format(score), 22, 100, 300)
        self.draw_text(self.game_play_screen, "This Is How Many Bricks You Remaining: {}".format(len(all_game_bricks)), 22, 185, 330)

    def show_game_controlls(self, paddle_control):
        """Creates the text to show the controls for the user."""
        # Show the controls for the keyboard.
        if paddle_control:
            self.draw_text(self.game_play_screen, "Use the left and right arrow keys to control the paddle", 24, self.CENTRE_X, self.CENTRE_Y - 100)
            self.draw_text(self.game_play_screen, "Press m to select the mouse".title(), 24, self.CENTRE_X, self.CENTRE_Y - 70)
        
        # Show the controls for the mouse.
        else:
            self.draw_text(self.game_play_screen, "Use the mouse to control the paddle", 24, self.CENTRE_X, self.CENTRE_Y - 100)
            self.draw_text(self.game_play_screen, "Press k to select the keyboard".title(), 24, self.CENTRE_X, self.CENTRE_Y - 70)
        self.draw_text(self.game_play_screen, "Press y to start".title(),
                  24, self.CENTRE_X, self.HEIGHT - 200)     


    def show_game_over(self, score, level):
        """Creates the text to show game over status."""
        self.draw_text(self.game_play_screen, "Sorry but you have failed!".title(), 40, self.CENTRE_X, self.HEIGHT / 4)
        self.draw_text(self.game_play_screen, "Your score is {}".format(score).title(), 40, self.CENTRE_X, self.CENTRE_Y)
        self.draw_text(self.game_play_screen, "Press y to play the next level".title(), 30, self.CENTRE_X, self.HEIGHT * 3/4)
        self.draw_text(self.game_play_screen, "Well done you got to level {}".format(level).title(), 22, self.CENTRE_X, self.HEIGHT - 100)


    def show_level_over(self, score, level):
        """Creates the text to show level completed message."""
        self.draw_text(self.game_play_screen, "you have completed level {}".format(level).title(), 40, self.CENTRE_X, self.HEIGHT / 4)
        self.draw_text(self.game_play_screen, "your score is {}".format(score).title(), 40, self.CENTRE_X, self.CENTRE_Y)
        self.draw_text(self.game_play_screen, "press y to play the next level".title(), 30, self.CENTRE_X, self.HEIGHT * 3/4)                   