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
        self.done = False
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        return

    def get_font(self, size):
        return pygame.font.Font("./assets/graphics/menu/font.ttf", size)

    def display_game_over(self):

        self.screen.fill((249, 131, 103))
        header_text = self.get_font(100).render("GAME OVER", True, "#d7fcd4")
        header_text_rect = header_text.get_rect(center=(640, 100))
        self.screen.blit(header_text, header_text_rect)
        pygame.display.update()

        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                    self.done = True

        pygame.quit()
        sys.exit()
