import random
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH

class Bird(Obstacle):
    Y_POS_BIRD = [100, 250, 300]
    X_POS_BIRD = SCREEN_WIDTH

    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = random.choice(self.Y_POS_BIRD)
        self.step_index = 0

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        super().update(game_speed, player)
       # self.fly()

        if self.step_index >= 10:
            self.step_index = 1

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.rect = self.image.get_rect()
        self.step_index += 1