import os

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

LAYERS = {
    "BG": 0,
    "BG Detail": 1,
    "Level": 2,
    "FG Detail Bottom": 3,
    "FG Detail Top": 4,
}


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
DATA_DIR = os.path.join(ASSETS_DIR, "data")
GRAPHICS_DIR = os.path.join(ASSETS_DIR, "graphics")