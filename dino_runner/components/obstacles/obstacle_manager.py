import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.enemy_dinosaur import EnemyDinosaur

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            choice = random.choice([0, 1, 2])
            if choice == 0:
                self.obstacles.append(Cactus())
            elif choice == 1:
                self.obstacles.append(Bird())
            elif choice == 2:
                self.obstacles.append(EnemyDinosaur())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

            
            #self.obstacles.append(Bird() and Cactus())
        #for obstacle in self.obstacles:
         #   if obstacle.rect.x < -obstacle.rect.width:
          #      self.obstacles.remove(obstacle)
           # obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []