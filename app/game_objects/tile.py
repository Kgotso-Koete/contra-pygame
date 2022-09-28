import pygame
from settings import *
from pygame.math import Vector2 as vector

PLATFORM_SPEED = 200


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z


class CollisionTile(Tile):
    def __init__(self, pos, surf, groups):
        z = LAYERS["Level"]
        super().__init__(pos, surf, groups, z)
        # collision
        self.old_rect = self.rect.copy()


class MovingPlatform(CollisionTile):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)

        # float based movement
        self.direction = vector(0, -1)
        self.speed = PLATFORM_SPEED
        self.pos = vector(self.rect.topleft)

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.pos.y += self.direction.y * self.speed * dt
        x_pos = round(self.pos.x)
        y_pos = round(self.pos.y)
        self.rect.topleft = (x_pos, y_pos)
