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
        self.load_sky()
        return

    def load_sky(self):
        # import sky
        fg_sky_path = os.path.join(GRAPHICS_DIR, "sky", "fg_sky.png")
        self.fg_sky = pygame.image.load(fg_sky_path).convert_alpha()
        bg_sky_path = os.path.join(GRAPHICS_DIR, "sky", "bg_sky.png")
        self.bg_sky = pygame.image.load(bg_sky_path).convert_alpha()
        tmx_map_path = os.path.join(DATA_DIR, "map.tmx")
        tmx_map = tmx_map = load_pygame(tmx_map_path)

        # dimensions
        self.padding = WINDOW_WIDTH / 2
        self.sky_width = self.bg_sky.get_width()
        map_width = (tmx_map.tilewidth * tmx_map.width) + (2 * self.padding)  # tile width  * number of tiles
        self.sky_num = int(map_width // self.sky_width)

        return

    def draw_sky(self):
        # place all clouds in the display surface
        for x in range(self.sky_num):
            x_pos = -self.padding + (x * self.sky_width)
            self.display_surface.blit(self.bg_sky, (x_pos - (self.offset.x / 2.5), SKY_Y_POS - (self.offset.y / 2.5)))
            self.display_surface.blit(self.fg_sky, (x_pos - (self.offset.x / 2), SKY_Y_POS - (self.offset.y / 2)))

        return

    def draw_all_sprites(self):
        # blit all sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.z):
            # get copy of the rectangle of the current sprite
            offset_rect = sprite.image.get_rect(center=sprite.rect.center)
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)

        return

    def custom_draw(self, player):
        # change the offset vector
        # calculate offset so that the player is always at the middle of the window
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        # place all clouds in the display surface
        self.draw_sky()
        # blit all sprites
        self.draw_all_sprites()

        return
