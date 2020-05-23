import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, pos):
        # character settings
        self.pos = pos
        self.char_w = 34
        self.char_h = 45
        
        super().__init__(pos, [self.char_w, self.char_h], False)
        
        self.vel = 2

        self.moving_left = False
        self.moving_right = False
        self.moving_for = False
        self.moving_back = False
        
        self.walkcount_x = 0
        self.walkcount_y = 0
        
        # sprite animations
        self.WALK_INTERVAL = 30
        self.WALK_PER_FRAME = self.WALK_INTERVAL / 2

        self.walk_right = [pygame.image.load("./assets/sprites/char/right_2.png"), pygame.image.load("./assets/sprites/char/right_3.png")]
        self.walk_left = [pygame.image.load("./assets/sprites/char/left_2.png"), pygame.image.load("./assets/sprites/char/left_3.png")]
        self.walk_for = [pygame.image.load("./assets/sprites/char/for_2.png"), pygame.image.load("./assets/sprites/char/for_3.png")]
        self.walk_back = [pygame.image.load("./assets/sprites/char/back_2.png"), pygame.image.load("./assets/sprites/char/back_3.png")]

        self.stand_right = pygame.image.load("./assets/sprites/char/right_1.png")
        self.stand_left = pygame.image.load("./assets/sprites/char/left_1.png")
        self.stand_for = pygame.image.load("./assets/sprites/char/for_1.png")
        self.stand_back = pygame.image.load("./assets/sprites/char/back_1.png")
    
    def tick(self, screen_size, keydict):
        keys = pygame.key.get_pressed()

        if keys[keydict[0]] and self.pos[0] > 0:
            self.pos[0] -= self.vel
            self.moving_for = False
            self.moving_back = False
            self.moving_left = True
            self.moving_right = False
        elif keys[keydict[1]] and self.pos[0] < screen_size[0] - self.char_w:
            self.pos[0] += self.vel
            self.moving_for = False
            self.moving_back = False
            self.moving_left = False
            self.moving_right = True
        elif keys[keydict[2]] and self.pos[1] > 0:
            self.pos[1] -= self.vel
            self.moving_for = False
            self.moving_back = True
            self.moving_left = False
            self.moving_right = False
        elif keys[keydict[3]] and self.pos[1] < screen_size[1] - self.char_h:
            self.pos[1] += self.vel
            self.moving_for = True
            self.moving_back = False
            self.moving_left = False
            self.moving_right = False
        else:
            self.moving_for = False
            self.moving_back = False
            self.moving_left = False
            self.moving_right = False
            self.walkcount_x = 0
            self.walkcount_y = 0

    def render(self, screen):
        if self.walkcount_x + 1 >= self.WALK_INTERVAL:
            self.walkcount_x = 0
        if self.walkcount_y + 1 >= self.WALK_INTERVAL:
            self.walkcount_y = 0

        if self.moving_left:
            screen.blit(self.walk_left[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_x += 1
        elif self.moving_right:
            screen.blit(self.walk_right[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_x += 1 
        elif self.moving_for:
            screen.blit(self.walk_for[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_y += 1
        elif self.moving_back:
            screen.blit(self.walk_back[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_y += 1
        else:
            screen.blit(self.stand_for, (self.pos[0], self.pos[1]))
        
        self.hitbox.center = self.pos
        pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)