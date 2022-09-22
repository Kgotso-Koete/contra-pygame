import pygame, sys
from settings import *
from pytmx.util_pygame import load_pygame
from tile import Tile


class Main:
    """Game class that runs the game's loops"""

    def __init__(self):
        """Initialize pygame variables"""
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Contra")
        self.clock = pygame.time.Clock()

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.setup()
        return

    def setup(self):
        tmx_map = load_pygame("./c1_setup/data/map.tmx")
        for x, y, surf in tmx_map.get_layer_by_name("Level").tiles():
            Tile((x * 0, y * 0), surf, self.all_sprites)
            print(x)
            print(y)
            print(surf)
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

            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
