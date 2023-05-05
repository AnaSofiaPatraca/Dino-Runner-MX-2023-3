import random
import pygame
from dino_runner.utils.constants import HEART, SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.power_ups.power_up import PowerUp

class HeartColor(PowerUp):
    COLOR_RED = (255, 0, 0)
    COLOR_GREEN = (0, 255, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_YELLOW = (255, 255, 0)
    COLOR_CIAN = (0, 255, 255)
    COLOR_MAGENTA = (255, 150, 255)
    COLOR_LIST = []


 #   COLOR_LIST: [
  #      ROJO == (255, 0, 0),
   #     VERDE == (0, 255, 0),
    #    AZUL == (0, 0, 255),
     #   AMARILLO == (255, 255, 0),
      #  CIAN == (0, 255, 255),
       # MAGENTA == (255, 150, 255
   # ]

    def __init__(self):
        self.image = HEART
        self.screen_type = type
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        super().__init__(self.image, self.screen.fill)
        self.COLOR_LIST.extend(self.COLOR_RED + self.COLOR_GREEN + self.COLOR_BLUE + self.COLOR_YELLOW + self.COLOR_CIAN + self.COLOR_MAGENTA)
        self.screen_color = random.choice(self.COLOR_LIST)
        if self.screen_color in self.COLOR_RED:
            self.screen = self.COLOR_RED
        elif self.screen_color in COLOR_GREEN:
            self.screen = self.COLOR_GREEN
        elif self.screen_color in COLOR_BLUE:
            self.screen = self.COLOR_BLUE
        elif self.screen_color in COLOR_YELLOW:
            self.screen = self.COLOR_YELLOW
        elif self.screen_color in COLOR_CIAN:
            self.screen= self.COLOR_CIAN
        elif self.screen_color in COLOR_MAGENTA:
            self.screen = self.COLOR_MAGENTA

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if not player.shield:
                self.start_time = pygame.time.get_ticks()
                self.time_up = self.start_time + self.POWER_UP_DURATION
                self.used = True