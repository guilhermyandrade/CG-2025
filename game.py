import sys
import pygame
from dvd import BouncingText
from config import standard_setup, standard_colors
#(
#    SCREEN_HEIGHT,
#    SCREEN_WIDTH,
#    FONT_SIZE,
#    FPS,
#    PRETO,
#    VERMELHO,
#    BRANCO,
#    VERDE,
#    AZUL,
#)


class Game:
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((
            standard_setup.SCREEN_WIDTH.value, 
            standard_setup.SCREEN_HEIGHT.value
        ))
        
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True


        self.text = BouncingText({    
            'text':          "DVD",
            'font_size':     standard_setup.FONT_SIZE.value,
            'initial_color': standard_colors.BRANCO.value,
            'screen_width':  standard_setup.SCREEN_WIDTH.value,
            'screen_height': standard_setup.SCREEN_HEIGHT.value
        })


    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_text_position(self):
        self.text.update()

    def render_text(self):
        self.screen.fill(standard_colors.PRETO.value)
        self.text.render(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.check_quit_event()
            self.update_text_position()
            self.render_text()
            self.clock.tick(standard_setup.FPS.value)
        pygame.quit()
        sys.exit()
