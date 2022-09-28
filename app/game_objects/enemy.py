import pygame
from settings import *
from pygame.math import Vector2 as vector
from app.game_objects.shared.entity import Entity

COOL_DOWN = 1000
ENTITY_TO_OBJ_MARGIN = 80


class Enemy(Entity):
    def __init__(self, pos, path, groups, shoot, player, collision_sprites):
        super().__init__(pos, path, groups, shoot)
        self.player = player

        # put player on top of floor tiles by checking for collisions
        for sprite in collision_sprites.sprites():
            if sprite.rect.collidepoint(self.rect.midbottom):
                self.rect.bottom = sprite.rect.top

        self.cooldown = COOL_DOWN
        return

    def get_status(self):
        # ensure that enemy always faces the
        if self.player.rect.centerx < self.rect.centerx:
            self.status = "left"
        else:
            self.status = "right"
        return

    def check_fire(self):
        enemy_pos = vector(self.rect.center)
        player_pos = vector(self.player.rect.center)
        distance = (player_pos - enemy_pos).magnitude()
        # check if player is in horizontal eye range
        same_y = True if (self.rect.top - 20) < self.player.pos.y < (self.rect.bottom + 20) else False
        if distance < 600 and same_y and self.can_shoot:
            bullet_direction = vector(1, 0) if self.status == "right" else vector(-1, 0)
            y_offset = vector(0, -16)
            pos = self.rect.center + bullet_direction * ENTITY_TO_OBJ_MARGIN
            entity = self
            self.shoot(pos + y_offset, bullet_direction, entity)

            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            self.shoot_sound.play()
        return

    def update(self, dt):
        self.get_status()
        self.animate(dt)
        self.blink()

        # timer
        self.shoot_timer()
        self.invul_timer()
        self.check_fire()

        # death
        self.check_death()
        return
