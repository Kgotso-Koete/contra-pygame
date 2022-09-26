import pygame
from settings import *
from pygame.math import Vector2 as vector

BULLET_SPEED = 1200
MAX_LIFETIME = 1000


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, surf, direction, groups):
        super().__init__(groups)
        self.image = surf

        # flip the image if the direction.x is negative
        if direction.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS["Level"]

        # float based movement
        self.direction = direction
        self.speed = BULLET_SPEED
        self.pos = vector(self.rect.center)

        # destroy the bullet after some time
        self.start_time = pygame.time.get_ticks()

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        # destroy the bullet after some time
        if (pygame.time.get_ticks() - self.start_time) > MAX_LIFETIME:
            self.kill()
