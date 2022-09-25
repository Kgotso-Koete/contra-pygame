import pygame, sys
from settings import *
from pytmx.util_pygame import load_pygame
from tile import Tile, CollisionTile, MovingPlatform
from player import Player
from all_sprites import AllSprites


class Main:
    """Game class that runs the game's loops"""

    def __init__(self):
        """Initialize pygame variables"""
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Contra")
        self.clock = pygame.time.Clock()

        # groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.platform_sprites = pygame.sprite.Group()
        self.setup()
        return

    def load_map_layer(self, layer_name, tile_type):
        for x, y, surf in self.tmx_map.get_layer_by_name(layer_name).tiles():
            pos = (x * 64, y * 64)
            if tile_type == "standard":
                groups = self.all_sprites
                z = LAYERS[layer_name]
                Tile(pos, surf, groups, z)
            elif tile_type == "collision":
                groups = [self.all_sprites, self.collision_sprites]
                CollisionTile(pos, surf, groups)

    def load_player(self):
        for obj in self.tmx_map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                path = "./assets/graphics/player/"
                pos = (obj.x, obj.y)
                groups = self.all_sprites
                self.player = Player(pos, groups, path, self.collision_sprites)

    def load_moving_platforms(self):
        self.platform_border_rects = []

        for obj in self.tmx_map.get_layer_by_name("Platforms"):
            if obj.name == "Platform":
                pos = (obj.x, obj.y)
                surf = obj.image
                groups = [self.all_sprites, self.collision_sprites, self.platform_sprites]
                MovingPlatform(pos, surf, groups)
            else:  # boarder
                border_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.platform_border_rects.append(border_rect)

        return

    def platform_collisions(self):
        for platform in self.platform_sprites.sprites():
            for border in self.platform_border_rects:
                if platform.rect.colliderect(border):
                    # if platform is moving up
                    if platform.direction.y < 0:
                        platform.rect.top = border.bottom  # change rectangle position
                        platform.pos.y = platform.rect.y  # change tile position
                        platform.direction.y = 1  # change platform direction
                    # if platform is moving down
                    else:
                        platform.rect.bottom = border.top  # change rectangle position
                        platform.pos.y = platform.rect.y  # change tile position
                        platform.direction.y = -1  # change platform direction
            # check if the player is colliding below the platform
            if platform.rect.colliderect(self.player.rect) and self.player.rect.centery > platform.rect.centery:
                platform.rect.bottom = self.player.rect.top
                platform.pos.y = platform.rect.y
                platform.direction.y = -1

    def setup(self):
        self.tmx_map = load_pygame("./assets/data/map.tmx")
        # render tiles

        # render collision tiles
        self.load_map_layer("Level", "collision")  # render level separately for collision mechanics
        layers = ["BG", "BG Detail", "FG Detail Bottom", "FG Detail Top"]
        for layer in layers:
            self.load_map_layer(layer, "standard")

        # render player position in tiles
        self.load_player()
        # render moving platforms that have collision detection
        self.load_moving_platforms()
        return

    def run(self):
        """Run the main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.display_surface.fill((249, 131, 103))

            self.platform_collisions()
            self.all_sprites.update(dt)
            self.all_sprites.custom_draw(self.player)
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
