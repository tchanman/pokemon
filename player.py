import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, pos):
        # character settings
        self.pos = pos
        self.char_w = 30
        self.char_h = 45
        
        super().__init__(pos, [self.char_w, self.char_h], False)
        
        self.vel = 4
        self.rect_offput = [self.char_w / 2, self.char_h / 2]
        self.rect.center = [self.pos[0] + self.rect_offput[0], self.pos[1] + self.rect_offput[1]]

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
            self.moving_direction["r"] = False
            self.moving_direction["f"] = False
            self.moving_direction["b"] = False
        #right
        elif keys[keydict[1]] and self.canmove["r"] and self.pos[0] < screen_size[0] - self.char_w:
            self.pos[0] += self.vel
            self.moving_direction["l"] = False
            self.moving_direction["r"] = True
            self.moving_direction["f"] = False
            self.moving_direction["b"] = False
        #back
        elif keys[keydict[2]] and self.canmove["b"] and self.pos[1] > 0:
            self.pos[1] -= self.vel
            self.moving_direction["l"] = False
            self.moving_direction["r"] = False
            self.moving_direction["f"] = False
            self.moving_direction["b"] = True
        #for
        elif keys[keydict[3]] and self.canmove["f"] and self.pos[1] < screen_size[1] - self.char_h:
            self.pos[1] += self.vel
            self.moving_direction["l"] = False
            self.moving_direction["r"] = False
            self.moving_direction["f"] = True
            self.moving_direction["b"] = False
        else:
            self.moving_direction["l"] = False
            self.moving_direction["r"] = False
            self.moving_direction["f"] = False
            self.moving_direction["b"] = False
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
        
        self.rect.center = [self.pos[0] + self.rect_offput[0], self.pos[1] + self.rect_offput[1]]
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)


    def restrict_movement(self, wallgroup):
        self.allow_movement()
        for wall in wallgroup:
            w1 = wall.rect.topleft
            w2 = wall.rect.bottomright
            tl = self.in_box(self.rect.topleft, w1, w2)
            tr = self.in_box(self.rect.topright, w1, w2)
            bl = self.in_box(self.rect.bottomleft, w1, w2)
            br = self.in_box(self.rect.bottomright, w1, w2)
            
            if tl and tr and bl and not br:
                self.canmove['b'] = False
                self.canmove['l'] = False
            elif tl and tr and br and not bl:
                self.canmove['b'] = False
                self.canmove['r'] = False
            elif bl and br and tl and not tr:
                self.canmove['f'] = False
                self.canmove['l'] = False
            elif bl and br and tr and not tl:
                self.canmove['f'] = False
                self.canmove['r'] = False
            
            if tl and tr and not bl and not br:
                self.canmove['b'] = False
            elif bl and br and not tl and not tr:
                self.canmove['f'] = False
            elif tl and bl and not tr and not br:
                self.canmove['l'] = False
            elif tr and br and not tl and not bl:
                self.canmove['r'] = False
            
            elif tl and not tr and not bl and not br:
                self.canmove['b'] = False
                self.canmove['l'] = False
            elif bl and not tl and not tr and not br:
                self.canmove['f'] = False
                self.canmove['l'] = False
            elif tr and not tl and not bl and not br:
                self.canmove['r'] = False
                self.canmove['b'] = False
            elif br and not tl and not tr and not bl:
                self.canmove['r'] = False
                self.canmove['f'] = False
            print(self.canmove)

    def allow_movement(self):
        self.canmove['l'] = True
        self.canmove['r'] = True
        self.canmove['b'] = True
        self.canmove['f'] = True

    def in_box(self, ptcoords,boxtl,boxbr):
        if ptcoords[0] >= boxtl[0] and ptcoords[0] <= boxbr[0] and ptcoords[1] >= boxtl[1] and ptcoords[1] <= boxbr[1]:
            return True
        return False