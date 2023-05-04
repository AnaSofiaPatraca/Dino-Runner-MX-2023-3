import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = 'freesansbold.ttf'
black_color = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22) 
    text = font.render("Points: " + str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return text, text_rect

def get_central_messager(message, widht=SCREEN_WIDTH // 2, heigth=SCREEN_HEIGHT // 2 ):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect_center = (widht, heigth)
    return text, text_rect

