import pygame
from entity import Entity
from player import Player
from level import Level
from exitzone import ExitZone

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
        Entity([0,0], [430,75]),
        Entity([0,0], [220, 720]),
        Entity([0, 720-160], [1080, 720]),
        Entity([1080-224, 0], [224, 720]),
        Entity([1080-434,0], [434,75]),
        #Entity([315,50], [30,170]),
    ],[
        ExitZone( Entity([430, 0], [220, 5], color=(0,255,0,50)), (0,670) , "route1", True), #exit to route 1
        ExitZone( Entity([360, 170], [35, 5], color=(0,255,0,50)), (500,500) , "oakslab", False)
    ]),
    "route1": Level(pygame.image.load("./assets/bgs/route1.png"), [
        Entity([0,0], [100, 75])
    ], [
        ExitZone( Entity([430, 715], [220, 720], color=(0,255,0,50)), (0,-670) , "hometown", True) #exit to hometown
    ]),
    "oakslab": Level(pygame.image.load("./assets/bgs/oakslab.png"), [
        Entity([0,0], [100, 75])
    ], [
        ExitZone( Entity([430, 715], [220, 720], color=(0,255,0,50)), (360,180) , "hometown", False) #exit to hometown
    ])
}

level = "hometown"
bg = level_list["hometown"]

def tick():
    global bg, level
    pl.tick(SCREEN_SIZE, keydict)

    colliding = pygame.sprite.spritecollide(pl, bg.wall_group, False)
    if colliding:
        pl.restrict_movement(bg.wall_group)
    else:
        pl.allow_movement()
    
    # exiting = pygame.sprite.spritecollide(pl, bg.exit_group, False)
    # if exiting:
    #     level += 1
    # for exitent in bg.exit_group:
    #     exiting = pygame.sprite.collide_rect(pl, exitent)
    #     if exiting:
    #         print(bg.exit_dict[exitent])
    for exitzone in bg.exit_zones:
        exiting = pygame.sprite.collide_rect(pl, exitzone.exit_ent)
        if exiting:
            print(pl.pos)
            level = exitzone.level_to
            pl.change_pos_on_level(exitzone.spawn_change, exitzone.rel_spawn)

    bg = level_list[level]

def render():

    bg.render(screen, debug=True)
    pl.render(screen)
    
    pygame.display.update()

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

    # update game state
    tick()
    render()
    clock.tick(FPS)

pygame.quit()