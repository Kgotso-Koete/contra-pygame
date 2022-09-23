import os
from os import walk
import pygame
from settings import *
from pygame.math import Vector2 as vector


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path):
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
        self.speed = 400

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
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self, dt):
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
