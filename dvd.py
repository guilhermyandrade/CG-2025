import pygame
import random

pygame.mixer.init()

pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.play(loops=-1, start=0.0)

"""
Contém os atributos e comportamentos básicos para renderizar e desenhar texto na tela, além de armazenar posição e dimensões.
"""

class MoveText:

    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(
            center=(screen_width / 2, screen_height / 2)
        )

        self.speed_x = self._get_initial_speed()
        self.speed_y = self._get_initial_speed()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.sound_effect = pygame.mixer.Sound("sound_effect.mp3")


    def _get_initial_speed(self):
        return random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def render(self, screen):
        screen.blit(self.text_surf, self.rect)

    def change_color(self):
        self.color_random = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        self.color = self.color_random
        self.text_surf = self.font.render(self.text, True, self.color)


    def play_sound_effect(self):
        self.sound_effect.play(loops=0)


"""
Implementa colisão do eixo horizontal com as bordas laterais e muda de cor.
"""
class HorizontalBounce(MoveText):

    def __init__(self, move_text):
        self.move_text = move_text

    def update(self):
        if ( self.move_text.rect.left <= 0 ) or ( self.move_text.rect.right >= self.move_text.screen_width ):
            self.move_text.speed_x = -self.move_text.speed_x
            self.move_text.change_color()
            self.move_text.play_sound_effect()


"""
Implementa colisão vertical com as bordas superior e inferior e muda de cor.
"""
class VerticalBounce(MoveText):

    def __init__(self, move_text):
        self.move_text = move_text

    def update(self):
        if ( self.move_text.rect.top <= 0 ) or (self.move_text.rect.bottom >= self.move_text.screen_height):
            self.move_text.speed_y = -self.move_text.speed_y
            self.move_text.change_color()
            self.move_text.play_sound_effect()


"""
Lida com as colisões do texto com as bordas.
"""
class BounceHandler:

    def __init__(self, Params):
        self.move_text = MoveText(**Params)
        self.vertical_bounce = VerticalBounce(self.move_text)
        self.horizontal_bounce = HorizontalBounce(self.move_text)

    def _handle_boundary_collision(self):
        self.vertical_bounce.update()
        self.horizontal_bounce.update()

    def update(self):
        self._handle_boundary_collision()
        self.move_text.update()

    def render(self, screen):
        self.move_text.render(screen)


"""
Instancia o objeto "bouncing text" (texto é refletido ao bater na borda).
"""
class BouncingText:

    def __init__(self, Params):
        self.bounce_handler = BounceHandler(Params)

    def update(self):
        self.bounce_handler.update()

    def render(self, screen):
        self.bounce_handler.render(screen)
