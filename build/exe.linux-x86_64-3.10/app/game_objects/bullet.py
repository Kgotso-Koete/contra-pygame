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

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        # destroy the bullet after some time
        if (pygame.time.get_ticks() - self.start_time) > MAX_LIFETIME:
            self.kill()


class FireAnimation(pygame.sprite.Sprite):
    def __init__(self, entity, surf_list, direction, groups):
        super().__init__(groups)
        # setup
        self.entity = entity
        self.frames = surf_list
        self.z = LAYERS["Level"]

        # flip direction of fire frames
        if direction.x < 0:
            self.frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]

        # image
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        # offset to move fire animation to end of gun barrel
        x_offset = 60 if direction.x > 0 else -60
        y_offset = 10 if entity.duck else -16
        self.offset = vector(x_offset, y_offset)

        # position
        self.rect = self.image.get_rect(center=self.entity.rect.center + self.offset)
        return

    def animate(self, dt):
        # destroy the sprite after the animation is complete
        self.frame_index += 15 * dt
        if self.frame_index >= len(self.frames):
            self.kill()
        # animate the sprite using frames
        else:
            self.image = self.frames[(int(self.frame_index))]
        return

    def move(self):
        self.rect.center = self.entity.rect.center + self.offset

    def update(self, dt):
        self.animate(dt)
        self.move()
