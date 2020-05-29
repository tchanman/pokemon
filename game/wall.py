import pygame
from game.entity import Entity

class Wall(Entity):
    def __init__(self, pos, dimensions):
        self.color = (255, 0, 0, 100)
        super().__init__( pos, dimensions, self.color)