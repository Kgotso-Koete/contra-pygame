import pygame, sys
from settings import *


class Main:
    """Game class that runs the game's loops"""

    def __init__(self):
        """Initialize pygame variables"""
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Contra")
        self.clock = pygame.time.Clock()
        return

    def run(self):
        """Run the main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick() / 1000
            self.display_surface.fill((249, 131, 103))
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
