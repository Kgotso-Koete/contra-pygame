import os
from os import walk
import pygame
from settings import *
from pygame.math import Vector2 as vector


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAVITY = 15
SPEED = 400
JUMP_SPEED = 1400


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path, collision_sprites):
        super().__init__(groups)
        self.import_assets(path)
        self.frame_index = 0
        self.status = "right"

        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=pos)
        self.z = LAYERS["Level"]

        # float based movement
        self.direction = vector()
        self.pos = vector(self.rect.topleft)
        self.speed = SPEED
        # collision
        self.old_rec = self.rect.copy()
        self.collision_sprites = collision_sprites

        # vertical movement
        self.gravity = GRAVITY
        self.jump_speed = JUMP_SPEED
        self.on_floor = False  # only be able to jump if the player is on the floor
        self.duck = False
        self.moving_floor = None
        return

    def get_status(self):
        # idle
        if self.direction.x == 0 and self.on_floor:
            self.status = self.status.split("_")[0] + "_idle"
        # jump
        if not self.direction.y == 0 and not self.on_floor:
            self.status = self.status.split("_")[0] + "_jump"

        # duck
        if self.on_floor and self.duck:
            self.status = self.status.split("_")[0] + "_duck"

        return

    def check_contact(self):
        bottom_rect = pygame.Rect(0, 0, self.rect.width, 5)
        bottom_rect.midtop = self.rect.midbottom

        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(bottom_rect):
                # if the player is moving downwards
                if self.direction.y > 0:
                    self.on_floor = True
                # check if in contact with moving platform
                if hasattr(sprite, "direction"):
                    self.moving_floor = sprite

    def import_assets(self, path):
        self.animations = {}

        # create keys in animations named after each folder with an action
        for index, folder in enumerate(walk(path)):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in sorted(folder[2], key=lambda file_string: int(file_string.split(".")[0])):
                    path = BASE_DIR + folder[0].replace("./", "/") + "/" + file_name
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split("/")[-1]
                    self.animations[key].append(surf)
        return

    def animate(self, dt):
        self.frame_index += 7 * dt

        # cycle through the sprite images for each action
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]
        return

    def input(self):
        """Get player keyboard input and change sprite position"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_floor:
            self.direction.y = -self.jump_speed
        if keys[pygame.K_DOWN]:
            self.duck = True
        else:
            self.duck = False

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    # left collision
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    # right collision
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                    self.pos.x = self.rect.x

                else:
                    # bottom collision
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.on_floor = True
                    # top collision
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y
                    self.direction.y = 0
        if self.on_floor and not self.direction.y == 0:
            self.on_floor = False

    def move(self, dt):
        if self.duck and self.on_floor:
            self.direction.x = 0
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision("horizontal")
        # vertical movement and gravity
        self.direction.y += self.gravity
        self.pos.y += self.direction.y * dt
        # glue the player to the platform
        if self.moving_floor and self.moving_floor.direction.y > 0 and self.direction.y > 0:
            self.direction.y = 0
            self.rect.bottom = self.moving_floor.rect.top
            self.pos.y = self.rect.y
            self.on_floor = True

        self.rect.y = round(self.pos.y)
        self.collision("vertical")
        self.moving_floor = None

    def update(self, dt):
        self.old_rect = self.rect.copy()  # store previous frame for collision detection
        self.input()
        self.get_status()
        self.move(dt)
        self.check_contact()
        self.animate(dt)
