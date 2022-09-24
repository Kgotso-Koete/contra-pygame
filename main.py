import pygame, sys
from settings import *
from pytmx.util_pygame import load_pygame
from tile import Tile, CollisionTile
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
        self.setup()
        return

    def load_map_layer(self, layer_name, tile_type):
        for x, y, surf in self.tmx_map.get_layer_by_name(layer_name).tiles():
            if tile_type == "standard":
                Tile((x * 64, y * 64), surf, self.all_sprites, LAYERS[layer_name])
            elif tile_type == "collision":
                CollisionTile((x * 64, y * 64), surf, [self.all_sprites, self.collision_sprites])

    def setup(self):
        self.tmx_map = load_pygame("./assets/data/map.tmx")
        # render tiles

        # render collision tiles
        self.load_map_layer("Level", "collision")  # render level separately for collision mechanics
        layers = ["BG", "BG Detail", "FG Detail Bottom", "FG Detail Top"]
        for layer in layers:
            self.load_map_layer(layer, "standard")

        # render tiles
        for obj in self.tmx_map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                player_graphics = "./assets/graphics/player/"
                self.player = Player((obj.x, obj.y), self.all_sprites, player_graphics, self.collision_sprites)
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

            self.all_sprites.update(dt)
            self.all_sprites.custom_draw(self.player)
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()
