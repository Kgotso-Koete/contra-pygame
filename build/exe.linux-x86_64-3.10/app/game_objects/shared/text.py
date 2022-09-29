import pygame
from pygame.locals import *


class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.display_surface = pygame.display.get_surface()

        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color("white")
        self.set_font()
        self.render()
        return

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)
        return

    def render(self):
        """Render the text into an image."""
        self.image = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        return

    def draw(self):
        """Draw the text image to the screen."""
        self.display_surface.blit(self.image, self.rect)
        return
