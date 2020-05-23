import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, dimensions, isTransparent):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface(dimensions, flags=pygame.SRCALPHA)
        if isTransparent:
            self.image.fill((0,0,0,0))
        else:
            self.image.fill((255,0,0,50))
        self.rect = self.image.get_rect()

        self.hitbox = self.rect
    
    #returns tuple in form of (x1,y1,x2,y2)
    def get_rect(self):
        dimensions = self.pos
        return dimensions