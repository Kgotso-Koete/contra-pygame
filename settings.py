import pygame, sys, os
from app.utils.paths import resource_path

pygame.init()
info = pygame.display.Info()
print(info)
WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h

LAYERS = {
    "BG": 0,
    "BG Detail": 1,
    "Level": 2,
    "FG Detail Bottom": 3,
    "FG Detail Top": 4,
}

# absolute path of the base directory
BASE_DIR = resource_path(".")
# change base directory to use relative path
BASE_DIR = "./"
ASSETS_DIR = resource_path("assets")
AUDIO_DIR = resource_path("assets/audio")
DATA_DIR = resource_path("assets/data")
GRAPHICS_DIR = resource_path("assets/graphics")
