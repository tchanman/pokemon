# Imported packages
import pygame

# Imported classes
from game.entity import Entity
from game.player import Player
from game.level import Level
from game.exitzone import ExitZone
from game.pokezone import PokeZone
from game.menu import Menu

# Imported variables
from game.level_list import level_list

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
DEBUG_FONT = pygame.font.SysFont("arial", 16)

menu = Menu()

# player
pl = Player([SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2])
keydict = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

player_group = pygame.sprite.Group()
player_group.add(pl)

level = "hometown"
bg = level_list[level]

save_data = {
    "level": level,
    "pos": pl.get_position(),
    "save_iteration": 0
}


def tick():
    global bg, level, level_list, save_data
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
            level = exitzone.level_to
            pl.change_pos_on_level(exitzone.spawn_change, exitzone.rel_spawn)

    bg = level_list[level]

def render():
    bg.render(screen, DEBUG)
    pl.render(screen, DEBUG)
    if menu.is_running:
        menu.render(screen, DEBUG)

    if DEBUG:
        debugFPS = "FPS: " + str(int(clock.get_fps()))
        debugFPS_surf = DEBUG_FONT.render(debugFPS, 1, (255,255,255))
        
        debug_mouse_pos = "Mouse Position: " + str(pygame.mouse.get_pos())
        debugMousePos_surf = DEBUG_FONT.render(debug_mouse_pos, 1, (255,255,255))

        debug_player_pos = "Player Position: (" + str(int(pl.get_position()[0])) + ", " + str(int(pl.get_position()[1])) + ")"
        debugPlayerPos_surf = DEBUG_FONT.render(debug_player_pos, 1, (255,255,255))

        debug_player_rect = "Player Rect: " + str(pl.get_rect())
        debugPlayerRect_surf = DEBUG_FONT.render(debug_player_rect, 1, (255,255,255))

        screen.blit(debugFPS_surf, (5,5))
        screen.blit(debugMousePos_surf, (5,30))
        screen.blit(debugPlayerPos_surf, (5,55))
        screen.blit(debugPlayerRect_surf, (5,80))
    
    pygame.display.update()

def open_menu():
    
    if menu.is_running:
        print("Closing menu")
        menu.is_running = False
    else:
        print("Opening menu")
        update_save_data()
        menu.is_running = True

def update_save_data():
    print("Updating current data...")
    global save_data, level

    save_data["level"] = level
    save_data["pos"] = pl.get_position()
    save_data["last_dir"] = pl.get_last_dir()

def check_save_data(load_data):
    print("Checking save data...")
    global save_data, level

    try:
        if save_data["save_iteration"] != load_data["save_iteration"]:
            level = load_data["level"]
            pos = load_data["pos"]
            last_dir = load_data["last_dir"]

            pl.set_position(pos[0], pos[1])
            pl.set_last_dir(last_dir)

            update_save_data()
            print("Game save loaded.")
    except TypeError as error:
        print("No save found.")


gameRunning = True

# main loop
while gameRunning:

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_m: # open menu
                open_menu()
        if menu.is_running:
            if event.type == pygame.KEYUP:
                menuResult = menu.handleMenu(event.key, save_data)
                gameRunning = menuResult["notquitting"]
                if menuResult["loading"]:
                    check_save_data(menuResult["load_data"])
        if event.type == pygame.QUIT: # quit game with x in corner
            print("Quitting game.")
            gameRunning = False

    # update game state
    tick()
    render()
    clock.tick(FPS)

pygame.quit()