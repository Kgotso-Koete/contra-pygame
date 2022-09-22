import pygame
from settings import *
from pygame.math import Vector2 as vector


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()

    def custom_draw(self, player):
        # change the offset vector
        # calculate offset so that the player is always at the middle of the window
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        # blit all sprites
        for sprite in self.sprites():
            # get copy of the rectangle of the current sprite
            offset_rect = sprite.image.get_rect(center=sprite.rect.center)
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
