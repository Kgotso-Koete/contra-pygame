import os
from os import walk
import pygame
from settings import *
from pygame.math import Vector2 as vector
from math import sin

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SPEED = 400
COOL_DOWN = 200
HEALTH = 3
INVULNERABILITY_DURATION = 500


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
        self.mask = pygame.mask.from_surface(self.image)

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

        # health
        self.health = HEALTH
        self.is_vulnerable = True
        self.hit_time = None
        self.invul_duration = INVULNERABILITY_DURATION

        # audio
        hit_sound_path = os.path.join(AUDIO_DIR, "hit.wav")
        self.hit_sound = pygame.mixer.Sound(hit_sound_path)
        shoot_sound_path = os.path.join(AUDIO_DIR, "bullet.wav")
        self.shoot_sound = pygame.mixer.Sound(shoot_sound_path)
        self.hit_sound.set_volume(0.2)
        self.shoot_sound.set_volume(0.2)

        return

    def import_assets(self, path):
        relative_path = os.path.relpath(path)
        relative_folder = "./" + relative_path
        self.animations = {}

        # create keys in animations named after each folder with an action
        for index, folder in enumerate(walk(relative_folder)):

            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                file_list = folder[2]
                file_list_sorted = sorted(file_list, key=lambda file_string: int(file_string.split(".")[0]))

                for file_name in file_list_sorted:
                    path = os.path.join(folder[0], file_name)
                    surf = pygame.image.load(path).convert_alpha()
                    keys = os.path.normpath(path).split(os.path.sep)  # split path into components
                    key = keys[-2]
                    self.animations[key].append(surf)
        return

    def shoot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            # check if time elapsed since last shoot trigger is more than cooldown period
            if (current_time - self.shoot_time) > self.cooldown:
                self.can_shoot = True
        return

    def invul_timer(self):
        if not self.is_vulnerable:
            current_time = pygame.time.get_ticks()
            # check if time elapsed since last time entity received damage is more than invulnerability period
            if (current_time - self.hit_time) > self.invul_duration:
                self.is_vulnerable = True
        return

    def damage(self):
        if self.is_vulnerable:
            self.health -= 1
            self.is_vulnerable = False
            self.hit_time = pygame.time.get_ticks()
            self.hit_sound.play()

        return

    def check_death(self):
        if self.health <= 0:
            self.kill()
        return

    def blink(self):
        if not self.is_vulnerable:
            if self.wave_value():
                mask = pygame.mask.from_surface(self.image)
                white_surf = mask.to_surface()
                white_surf.set_colorkey((0, 0, 0))
                self.image = white_surf

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        return True if value >= 0 else False

    def animate(self, dt):
        self.frame_index += 7 * dt

        # cycle through the sprite images for each action
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]
        self.mask = pygame.mask.from_surface(self.image)
        return
