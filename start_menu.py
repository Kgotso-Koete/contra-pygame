import pygame, sys
from button import Button
from app import App
from settings import *


class StartMenu:
    """
    Create a screen that helps the player start the game after an intro
    reference: https://youtu.be/GMBqjxcKogA
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Menu")
        self.back_ground = pygame.image.load("./assets/graphics/menu/background.png")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # audio
        self.music = pygame.mixer.Sound("./assets/audio/leap.wav")
        self.music.play(loops=1)
        return

    def get_font(self, size):  
        return pygame.font.Font("./assets/graphics/menu/font.ttf", size)

    def play(self):
        self.music.stop()
        app = App()
        app.run()

    def options(self):
        while True:
            self.screen.fill((249, 131, 103))
            mouse_pos = pygame.mouse.get_pos()
            screen_header = self.get_font(45).render("Game options", True, "#d7fcd4")
            screen_header_rect = screen_header.get_rect(center=(640, 260))
            self.screen.blit(screen_header, screen_header_rect)

            go_back_text = Button(
                image=None,
                pos=(640, 460),
                text_input="BACK",
                font=self.get_font(75),
                base_color="#d7fcd4",
                hovering_color="Orange",
            )

            go_back_text.changeColor(mouse_pos)
            go_back_text.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if go_back_text.checkForInput(mouse_pos):
                        self.main_menu()

            pygame.display.update()

    def main_menu(self):
        while True:
            # self.screen.blit(self.back_ground, (0, 0))
            self.screen.fill((249, 131, 103))
            mouse_pos = pygame.mouse.get_pos()
            header_text = self.get_font(100).render("MAIN MENU", True, "#d7fcd4")
            header_text_rect = header_text.get_rect(center=(640, 100))

            play_button = Button(
                image=pygame.image.load("./assets/graphics/menu/play_rect.png"),
                pos=(640, 250),
                text_input="PLAY",
                font=self.get_font(75),
                base_color="#d7fcd4",
                hovering_color="White",
            )

            options_button = Button(
                image=pygame.image.load("./assets/graphics/menu/options_rect.png"),
                pos=(640, 400),
                text_input="OPTIONS",
                font=self.get_font(75),
                base_color="#d7fcd4",
                hovering_color="White",
            )

            quit_button = Button(
                image=pygame.image.load("./assets/graphics/menu/quit_rect.png"),
                pos=(640, 550),
                text_input="QUIT",
                font=self.get_font(75),
                base_color="#d7fcd4",
                hovering_color="White",
            )

            self.screen.blit(header_text, header_text_rect)

            for button in [play_button, options_button, quit_button]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(mouse_pos):
                        self.play()
                    if options_button.checkForInput(mouse_pos):
                        self.options()
                    if quit_button.checkForInput(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
