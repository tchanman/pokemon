import pygame
from game.entity import Entity

pygame.init()

class Player(Entity):
    def __init__(self, pos):
        # character settings
        self.CHAR_W = 30
        self.CHAR_H = 45
        
        super().__init__(pos, [self.CHAR_W, self.CHAR_H])
        
        self.dx = 0
        self.dy = 0
        self.VELOCITY = 2

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

        self.last_dir = "f"
        self.settled_sprite = self.stand_for

        self.hasRunningShoes = True
    
    def tick(self, screen_size, keydict, wall_group, zone_group):
        keys = pygame.key.get_pressed()
        
        self.rect.x += self.dx
        self.check_collision(wall_group, zone_group, "x")
        
        self.rect.y += self.dy
        self.check_collision(wall_group, zone_group, "y")

        #left
        if keys[keydict[0]] and self.rect.x > 0:
            self.dx = -1*self.VELOCITY
            self.dy = 0
            self.last_dir = "l"
        #right
        elif keys[keydict[1]] and self.rect.x < screen_size[0] - self.CHAR_W:
            self.dx = self.VELOCITY
            self.dy = 0
            self.last_dir = "r"
        #back
        elif keys[keydict[2]] and self.rect.y > 0:
            self.dy = -1*self.VELOCITY
            self.dx = 0
            self.last_dir = "b"
        #for
        elif keys[keydict[3]] and self.rect.y < screen_size[1] - self.CHAR_H:
            self.dy = self.VELOCITY
            self.dx = 0
            self.last_dir = "f"
        else:
            self.dx = 0
            self.dy = 0
            self.last_dir = "standing"
            self.walkcount_x = 0
            self.walkcount_y = 0

        if self.hasRunningShoes:
            if keys[keydict[4]]:
                self.WALK_INTERVAL = 24
                self.VELOCITY = 5
            else:
                self.WALK_INTERVAL = 30
                self.VELOCITY = 2

    def render(self, screen, debug):
        if self.walkcount_x + 1 >= self.WALK_INTERVAL:
            self.walkcount_x = 0
        if self.walkcount_y + 1 >= self.WALK_INTERVAL:
            self.walkcount_y = 0

        if self.last_dir == "l":
            screen.blit(self.walk_left[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.rect.x, self.rect.y))
            self.walkcount_x += 1
            self.settled_sprite = self.stand_left
        elif self.last_dir == "r":
            screen.blit(self.walk_right[int(self.walkcount_x // self.WALK_PER_FRAME)], (self.rect.x, self.rect.y))
            self.walkcount_x += 1 
            self.settled_sprite = self.stand_right
        elif self.last_dir == "f":
            screen.blit(self.walk_for[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.rect.x, self.rect.y))
            self.walkcount_y += 1
            self.settled_sprite = self.stand_for
        elif self.last_dir == "b":
            screen.blit(self.walk_back[int(self.walkcount_y // self.WALK_PER_FRAME)], (self.rect.x, self.rect.y))
            self.walkcount_y += 1
            self.settled_sprite = self.stand_back
        else:
            screen.blit(self.settled_sprite, (self.rect.x, self.rect.y))

        if debug:
            pygame.draw.rect(screen, (255,0,0), self.rect, 2)
    
    def set_position(self, x,y):
        self.rect.x = x
        self.rect.y = y

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def set_last_dir(self, direction):
        self.last_dir = direction

    def get_last_dir(self):
        return self.last_dir
    
    def change_level(self, exitzone):
        spc = exitzone.spawn_change
        rel_spawn = exitzone.rel_spawn
        isInside = exitzone.isInside

        if isInside:
            exit_noise = pygame.mixer.Sound("./assets/sounds/SFX_GO_OUTSIDE.wav")
        else:
            exit_noise = pygame.mixer.Sound("./assets/sounds/SFX_GO_INSIDE.wav")
        exit_noise.play()

        if rel_spawn:
            x,y = self.get_position()
            self.set_position(x + spc[0], y + spc[1])
        else:
            self.set_position(spc[0], spc[1])


    def check_collision(self, wall_group, zone_group, direction):
        wall_hit_list = pygame.sprite.spritecollide(self, wall_group, False)
        zone_hit_list = pygame.sprite.spritecollide(self, zone_group, False)
        
        for wall in wall_hit_list:
            if direction == "x":
                if self.dx > 0:
                    self.rect.right = wall.rect.left
                else:
                    self.rect.left = wall.rect.right
            elif direction =="y":
                if self.dy > 0:
                    self.rect.bottom = wall.rect.top
                else:
                    self.rect.top = wall.rect.bottom

        for zone in zone_hit_list:
            print("Stepping on grass!")