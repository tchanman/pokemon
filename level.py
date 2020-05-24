import pygame
from entity import Entity

class Level(object):
    def __init__(self, bg, walls):
        self.bg = bg
        self.walls = walls
        self.wall_group = pygame.sprite.Group()

        for wall in self.walls:
            self.wall_group.add(wall)

    def render(self, screen):
        screen.blit(self.bg, (0,0))
        self.wall_group.draw(screen)