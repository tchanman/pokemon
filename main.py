# Imported packages
import pygame

# Imported classes
from entity import Entity
from player import Player
from level import Level
from exitzone import ExitZone
from pokezone import PokeZone
from menu import Menu

# Imported variables
from level_list import level_list

# ============= GAME =============

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

# Debug mode on
DEBUG = True

# player
pl = Player([SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2])
keydict = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

player_group = pygame.sprite.Group()
player_group.add(pl)

level = "hometown"
bg = level_list[level]

save_data = {
    "level": level,
    "pos": pl.get_position,
    "save_iteration": 0
}

menu = Menu(save_data)
gameRunning = True


def tick():
    global bg, level, level_list, menu
    if not menu.is_running:
        pl.tick(SCREEN_SIZE, keydict)
    
    wallcolliding = pygame.sprite.spritecollide(pl, bg.wall_group, False)
    if wallcolliding:
        pl.restrict_movement(bg.wall_group)
    else:
        pl.allow_movement()
    
    for pokezone in bg.pokezone_group:
        grasscolliding = pygame.sprite.collid_rect(pl, pokezone.area_ent)
        if grasscolliding:
            level = pokezone.battle_type

    for exitzone in bg.exit_zones:
        exiting = pygame.sprite.collide_rect(pl, exitzone.exit_ent)
        if exiting:
            # print(pl.pos)
            level = exitzone.level_to
            pl.change_pos_on_level(exitzone.spawn_change, exitzone.rel_spawn)

    bg = level_list[level]

def render():

    bg.render(screen, DEBUG)
    pl.render(screen, DEBUG)
    if menu.is_running:
        menu.render(screen, DEBUG)
    
    pygame.display.update()

def open_menu():
    global menu
    
    if menu.is_running:
        print("Closing menu")
        menu.is_running = False
    else:
        print("Opening menu")
        menu.is_running = True

# main loop
while gameRunning:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m: # open menu
                open_menu()
        if menu.is_running:
            if event.type == pygame.KEYDOWN:
                gameRunning = menu.handleMenu(event.key)
        if event.type == pygame.QUIT: # quit game with x in corner
            print("Quitting game.")
            gameRunning = False

    if DEBUG:
        debug_fps = pygame.font.SysFont("Arial", 16).render(str(int(clock.get_fps())), 0, pygame.Color("white"))
        debug_mouse_pos = pygame.mouse.get_pos()

        screen.blit(debug_fps, (0,0))
        # screen.blit(debug_mouse_pos, (0,50))

    # update game state
    tick()
    render()
    clock.tick(FPS)

pygame.quit()