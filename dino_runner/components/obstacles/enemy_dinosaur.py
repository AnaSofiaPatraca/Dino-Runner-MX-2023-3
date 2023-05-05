import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ENEMY_DINO
from dino_runner.utils.constants import SCREEN_WIDTH 

class EnemyDinosaur(Obstacle):
    Y_POS_ENEMY_DINO = 310

    def __init__(self):
        self.image = ENEMY_DINO
        super().__init__(self.image)
        if self.image == ENEMY_DINO:
            self.rect.y = self. Y_POS_ENEMY_DINO