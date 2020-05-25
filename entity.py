import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions, color=(255,0,0,100)):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos

        self.image = pygame.Surface(dimensions, flags=pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = pygame.Rect(pos[0],pos[1],dimensions[0],dimensions[1])