import pygame

class Level(object):
    def __init__(self, bg, music, walls, exit_zones, poke_zones):
        self.bg = bg
        self.music = music
        self.walls = walls
        self.exit_zones = exit_zones
        self.poke_zones = poke_zones

        self.wall_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.pokezone_group = pygame.sprite.Group()

        for wall in self.walls:
            self.wall_group.add(wall)
        
        for exitzone in self.exit_zones:
            self.exit_group.add(exitzone)
        
        for pokezone in self.poke_zones:
            self.pokezone_group.add(pokezone)

    def render(self, screen, debug=False):
        screen.blit(self.bg, (0,0))
        if debug:
            self.wall_group.draw(screen)
            self.exit_group.draw(screen)
            self.pokezone_group.draw(screen)