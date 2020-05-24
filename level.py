import pygame
from entity import Entity

class Level(object):
    def __init__(self, bg, walls, exits):
        self.bg = bg
        self.walls = walls
        self.exits = exits
        self.wall_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()

        for wall in self.walls:
            self.wall_group.add(wall)
        
        for exit in self.exits:
            self.exit_group.add(exit)

    def render(self, screen, debug=False):
        screen.blit(self.bg, (0,0))
        if debug:
            self.wall_group.draw(screen)
            self.exit_group.draw(screen)