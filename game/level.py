import pygame

class Level(object):
    def __init__(self, bg, music_path, walls, exit_zones, poke_zone):
        self.bg = bg
        self.music_path = music_path
        
        self.walls = walls
        self.wall_group = pygame.sprite.Group()
        for wall in walls:
            self.wall_group.add(wall)

        self.exit_zones = exit_zones
        self.exit_group = pygame.sprite.Group()
        for exitzone in exit_zones:
            self.exit_group.add(exitzone)

        self.poke_zone = poke_zone
        self.pokezone_group = pygame.sprite.Group()
        if poke_zone.hasPokemon:
            for pokezone in poke_zone.ent_list:
                self.pokezone_group.add(pokezone)

    def render(self, screen, debug=False):
        screen.blit(self.bg, (0,0))
        if debug:
            self.wall_group.draw(screen)
            self.exit_group.draw(screen)
            self.pokezone_group.draw(screen)