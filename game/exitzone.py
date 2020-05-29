import pygame
from game.entity import Entity

class ExitZone(Entity):
    def __init__(self, pos, dimensions, spawn_change, level_to, rel_spawn, isInside=False):
        self.color = (0, 255, 0, 100)
        super().__init__(pos, dimensions, self.color)

        self.spawn_change = spawn_change
        self.level_to = level_to
        self.rel_spawn = rel_spawn #bool if spawn change is rel, if false it's absolute
        self.isInside = isInside