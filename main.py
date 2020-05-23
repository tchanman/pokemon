import pygame
from entity import Entity
from player import Player
import background

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

pl = Player([SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2])
keydict = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

player_group = pygame.sprite.Group()
player_group.add(pl)

wall = Entity([0,0], [720, 100], False)
wall_group = pygame.sprite.Group()
wall_group.add(wall)

bg = pygame.image.load("./assets/bgs/hometown.png")

def tick():
    pl.tick(SCREEN_SIZE, keydict)
    # bg.tick(SCREEN_SIZE)

def render():
    screen.blit(bg, (0,0))

    pl.render(screen)
    # bg.render(screen)
    
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
    
    hit = pygame.sprite.spritecollide(pl, wall_group, True)
    if hit:
        print("collision!")

    # update game state
    tick()
    render()
    clock.tick(FPS)

pygame.quit()