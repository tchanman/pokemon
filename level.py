import pygame
from entity import Entity
from exitzone import ExitZone

class Level(object):
    def __init__(self, bg, walls, exit_zones):
        self.bg = bg
        self.walls = walls
        #self.exitbunds = exitbunds #tuple (Entity, (xchange,ychange on spawn), levelto (int))
        self.exit_zones = exit_zones
        self.wall_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        #self.exit_dict = {}

        for wall in self.walls:
            self.wall_group.add(wall)
        
        for zone in exit_zones:
            self.exit_group.add(zone.exit_ent)
        
        # for bund in self.exitbunds:
        #     exitent = bund[0] #the actual exit entity
        #     spawn_change = bund[1]
        #     levelto = bund[2]
        #     self.exit_group.add(exitent)
        #     self.exit_dict[exitent] = (spawn_change,levelto]
        # for zone in self.exitzones:
        #     self.exit_group.add(zone.exit_ent) #add all exit entitites



    def render(self, screen, debug=False):
        screen.blit(self.bg, (0,0))
        if debug:
            self.wall_group.draw(screen)
            self.exit_group.draw(screen)