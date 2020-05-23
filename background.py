import pygame
from entity import Entity

class Levels(object):
    def __init__(self):
        self.hometown = pygame.image.load("./assets/bgs/hometown.png")

wall = Entity([0,0], [100,100], False)

wall_group = pygame.sprite.Group()
wall_group.add(wall)