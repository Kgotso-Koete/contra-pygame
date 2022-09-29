import os

WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080

LAYERS = {
    "BG": 0,
    "BG Detail": 1,
    "Level": 2,
    "FG Detail Bottom": 3,
    "FG Detail Top": 4,
}

# absolute path of the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# change base directory to use relative path
BASE_DIR = "./"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
DATA_DIR = os.path.join(ASSETS_DIR, "data")
GRAPHICS_DIR = os.path.join(ASSETS_DIR, "graphics")
