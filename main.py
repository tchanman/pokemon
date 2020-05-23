import pygame
from entity import Entity
from player import Player
from level import Level

# Initialize game settings
pygame.init()
pygame.display.set_caption("Pokemon")

logo = pygame.image.load("./assets/pokeball.png")
pygame.display.set_icon(logo)

SCREEN_SIZE = (1080,720)
SCREEN_COLOR = (255,255,255)

screen = pygame.display.set_mode(SCREEN_SIZE)
# screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN, pygame.RESIZABLE)

# 60 frames per second
clock = pygame.time.Clock()
FPS = 60

# player
pl = Player([SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2])
keydict = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

player_group = pygame.sprite.Group()
player_group.add(pl)

# level selection
level_list = {
    "hometown": Level(pygame.image.load("./assets/bgs/hometown.png"), [
        Entity([430,75], False),
        Entity([220, 645], False),
        #Entity([0, 720], [1080 ,320], False)
    ]),
    # "level1": Level(pygame.image.load("./assets/bgs/level1.png"), [
    #     Entity([0,0], [100, 75], False)
    # ])
}

level = 1
bg = level_list["hometown"]

def tick():
    global bg
    if level == 1:
        bg = level_list["hometown"]
    elif level == 2:
        bg = level_list["level1"]
    
    pl.tick(SCREEN_SIZE, keydict)

def render():

    bg.render(screen)
    pl.render(screen)
    
    pygame.display.update()

def isPtInBox(ptx,pty,x1,y1,x2,y2):
    if ptx >= x1 and ptx <= x2 and pty >= y1 and pty <= y2:
        return True
    return False

gameRunning = True

# main loop
while gameRunning:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Quitting game.")
                gameRunning = False
        if event.type == pygame.QUIT:
            gameRunning = False

    hit = pygame.sprite.spritecollide(pl, bg.wall_group, False)
    if hit:
        pl.vel = 0
    else:
        pl.vel = 2

    # update game state
    tick()
    render()
    clock.tick(FPS)

pygame.quit()