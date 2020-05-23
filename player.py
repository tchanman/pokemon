import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, pos):
        # character settings
        self.pos = pos
        self.char_w = 34
        self.char_h = 45
        
        super().__init__([self.char_w, self.char_h], False)
        
        self.vel = 2
        self.hitbox_offput = [self.char_w / 2 - 2, self.char_h / 2]
        self.hitbox.center = [self.pos[0] + self.hitbox_offput[0], self.pos[1] + self.hitbox_offput[1]]

        # moving_direction = [for, back, left, right]
        self.moving_direction = {"f":False,"b":False,"l":False,"r":False}
        self.canmove = {"f":True,"b":True,"l":True,"r":True}

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

        #left
        if keys[keydict[0]] and self.canmove["l"] and self.pos[0] > 0:
            self.pos[0] -= self.vel
            self.moving_direction["l"] = True
        #right
        elif keys[keydict[1]] and self.canmove["r"] and self.pos[0] < screen_size[0] - self.char_w:
            self.pos[0] += self.vel
            self.moving_direction["r"] = True
        #back
        elif keys[keydict[2]] and self.canmove["b"] and self.pos[1] > 0:
            self.pos[1] -= self.vel
            self.moving_direction["b"] = True
        #for
        elif keys[keydict[3]] and self.canmove["f"] and self.pos[1] < screen_size[1] - self.char_h:
            self.pos[1] += self.vel
            self.moving_direction["f"] = True
        else:
            self.moving_direction = self.moving_direction.fromkeys(self.moving_direction, 0)
            self.walkcount_x = 0
            self.walkcount_y = 0

    def render(self, screen):
        if self.walkcount_x + 1 >= self.WALK_INTERVAL:
            self.walkcount_x = 0
        if self.walkcount_y + 1 >= self.WALK_INTERVAL:
            self.walkcount_y = 0

        if self.moving_direction["l"]:
            screen.blit(self.walk_left[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_x += 1
        elif self.moving_direction["r"]:
            screen.blit(self.walk_right[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_x += 1 
        elif self.moving_direction["f"]:
            screen.blit(self.walk_for[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_y += 1
        elif self.moving_direction["b"]:
            screen.blit(self.walk_back[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.pos[0], self.pos[1]))
            self.walkcount_y += 1
        else:
            screen.blit(self.stand_for, (self.pos[0], self.pos[1]))
        
        self.hitbox.center = [self.pos[0] + self.hitbox_offput[0], self.pos[1] + self.hitbox_offput[1]]
        pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)