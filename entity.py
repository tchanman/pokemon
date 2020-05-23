import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions, isTransparent):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface(dimensions, flags=pygame.SRCALPHA)
        if isTransparent:
            self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()

        self.rect.center = pos
        self.hitbox = self.rect