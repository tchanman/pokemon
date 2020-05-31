import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions, color=(255,0,0,100)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(dimensions, flags=pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]