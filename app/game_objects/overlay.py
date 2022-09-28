import pygame
from settings import *

HEALTH_BAR_GAP = 4


class Overlay:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        health_bar_path = os.path.join(GRAPHICS_DIR, "health.png")
        self.health_surf = pygame.image.load(health_bar_path).convert_alpha()
        return

    def display(self):
        # blit the health surface as many times as the player has health
        for h in range(self.player.health):
            x = 10 + h * (self.health_surf.get_width() + HEALTH_BAR_GAP)
            y = 10
            self.display_surface.blit(self.health_surf, (x, y))
