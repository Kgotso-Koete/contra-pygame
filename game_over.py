import pygame, sys
from settings import *
from text import Text


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class GameOver:
    """
    Create a screen that informs the player that the game is over
    reference: http://programarcadegames.com/python_examples/f.php?file=game_over.py
    """

    def __init__(self):
        """Initialize pygame variables"""
        # Loop until the user clicks the close button.
        self.done = False
        return

    def display_game_over(self):

        game_over_text = Text("Game Over", pos=((WINDOW_WIDTH / 2) - 80, WINDOW_HEIGHT / 2))
        game_over_text.draw()
        pygame.display.update()

        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

        pygame.quit()
        sys.exit()
