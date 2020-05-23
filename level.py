import pygame
from entity import Entity

class Level(object):
    def __init__(self, bg, walls):
        self.bg = bg
        self.walls = walls
        self.wall_group = pygame.sprite.Group()

        for wall in self.walls:
            self.wall_group.add(wall)

    # def update_level(level):
    #     self.bg = level.bg
    #     self.walls = level.walls

    #     #remove walls from old level
    #     self.wall_group.empty()
    #     #add walls from new level
    #     for wall in self.walls:
    #         self.wall_group.add(wall)

    # def tick(self, flags):
    #     if flags[0]:
    #         self.update_level(hometown)
    #     elif flags[1]:
    #         pass

    def render(self, screen):
        screen.blit(self.bg, (0,0))
        self.wall_group.draw(screen)