import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions, isTransparent):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos

        self.image = pygame.Surface(dimensions, flags=pygame.SRCALPHA)
        if isTransparent:
            self.image.fill((0,0,0,0))
        else:
            self.image.fill((255,0,0,50))
        self.rect = pygame.Rect(pos[0],pos[1],dimensions[0],dimensions[1])

        self.hitbox = self.rect