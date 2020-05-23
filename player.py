import pygame

class Player(object):
    def __init__(self, char_x, char_y, char_w, char_h):
        # character settings
        self.char_x = char_x
        self.char_y = char_y
        self.char_w = char_w
        self.char_h = char_h
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

    def tick(self, screen_size):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.char_x > 0:
            self.char_x -= self.vel
            self.moving_for = False
            self.moving_back = False
            self.moving_left = True
            self.moving_right = False
        elif keys[pygame.K_RIGHT] and self.char_x < screen_size[0] - self.char_w:
            self.char_x += self.vel
            self.moving_for = False
            self.moving_back = False
            self.moving_left = False
            self.moving_right = True
        elif keys[pygame.K_UP] and self.char_y > 0:
            self.char_y -= self.vel
            self.moving_for = False
            self.moving_back = True
            self.moving_left = False
            self.moving_right = False
        elif keys[pygame.K_DOWN] and self.char_y < screen_size[1] - self.char_h:
            self.char_y += self.vel
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
            screen.blit(self.walk_left[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.char_x, self.char_y))
            self.walkcount_x += 1
        elif self.moving_right:
            screen.blit(self.walk_right[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.char_x, self.char_y))
            self.walkcount_x += 1 
        elif self.moving_for:
            screen.blit(self.walk_for[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.char_x, self.char_y))
            self.walkcount_y += 1
        elif self.moving_back:
            screen.blit(self.walk_back[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.char_x, self.char_y))
            self.walkcount_y += 1
        else:
            screen.blit(self.stand_for, (self.char_x, self.char_y))