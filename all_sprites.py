import pygame
from pytmx.util_pygame import load_pygame
from settings import *
from pygame.math import Vector2 as vector

SKY_Y_POS = 800


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()

        # import sky
        self.fg_sky = pygame.image.load("./assets/graphics/sky/fg_sky.png").convert_alpha()
        self.bg_sky = pygame.image.load("./assets/graphics/sky/bg_sky.png").convert_alpha()
        tmx_map = tmx_map = load_pygame("./assets/data/map.tmx")

        # dimensions
        self.padding = WINDOW_WIDTH / 2
        self.sky_width = self.bg_sky.get_width()
        map_width = (tmx_map.tilewidth * tmx_map.width) + (2 * self.padding)  # tile width  * number of tiles
        self.sky_num = int(map_width // self.sky_width)
        return

    def custom_draw(self, player):
        # change the offset vector
        # calculate offset so that the player is always at the middle of the window
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        # place all clouds in the display surface
        for x in range(self.sky_num):
            x_pos = -self.padding + (x * self.sky_width)
            self.display_surface.blit(self.bg_sky, (x_pos - (self.offset.x / 2.5), SKY_Y_POS - (self.offset.y / 2.5)))
            self.display_surface.blit(self.fg_sky, (x_pos - (self.offset.x / 2), SKY_Y_POS - (self.offset.y / 2)))

        # blit all sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.z):
            # get copy of the rectangle of the current sprite
            offset_rect = sprite.image.get_rect(center=sprite.rect.center)
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
