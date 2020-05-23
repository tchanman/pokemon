# import the pygame module, so you can use it
import sys, pygame
from player import Player

# Initialize game settings
pygame.init()
pygame.display.set_caption("Pokemon")

logo = pygame.image.load("./assets/pokeball.png")
pygame.display.set_icon(logo)

SCREEN_SIZE = (1080,720)
# SCREEN_BUFFER = (10,10)
SCREEN_COLOR = (255,0,0)
screen = pygame.display.set_mode(SCREEN_SIZE)
# screen.fill(SCREEN_COLOR)

# 60 frames per second
clock = pygame.time.Clock()
FPS = 60

bg = []

pl = Player(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, 30, 45)

def tick():
    pl.tick(SCREEN_SIZE)

def render():
    screen.fill((0,0,0))
    
    pl.render(screen)
    
    pygame.display.update()

gameRunning = True

# main loop
while gameRunning:
    clock.tick(FPS)

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    
    # update game state
    tick()
    render()
    
pygame.quit()