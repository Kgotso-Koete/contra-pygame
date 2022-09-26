import os
from os import walk
import pygame
from settings import *
from pygame.math import Vector2 as vector

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPEED = 400
COOL_DOWN = 200


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, path, groups, shoot):
        super().__init__(groups)

        # load graphics
        self.import_assets(path)
        self.frame_index = 0
        self.status = "right"

        # image set up
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=pos)
        self.z = LAYERS["Level"]

        # float based movement
        self.direction = vector()
        self.pos = vector(self.rect.topleft)
        self.speed = SPEED

        # collision
        self.old_rec = self.rect.copy()

        # shoot setup
        self.shoot = shoot
        self.can_shoot = True
        self.shoot_time = None
        self.cooldown = COOL_DOWN

        # vertical movement
        self.duck = False

        return

    def shoot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            # check if time elapsed since last shoot trigger is more than cooldown period
            if (current_time - self.shoot_time) > self.cooldown:
                self.can_shoot = True

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
