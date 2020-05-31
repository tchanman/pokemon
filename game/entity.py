import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions, color=(255,0,0,100)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(dimensions, flags=pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect.x, self.rect.y