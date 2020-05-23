# import the pygame module, so you can use it
import sys, pygame

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

# Character Settings
char_w = 30
char_h = 45

char_x = SCREEN_SIZE[0]/2
char_y = SCREEN_SIZE[1]/2
vel = 2

moving_left = False
moving_right = False
moving_for = False
moving_back = False
walkcount_x = 0
walkcount_y = 0

WALK_PER_FRAME = 30

walk_right = [pygame.image.load("./assets/sprites/char/right_2.png"), pygame.image.load("./assets/sprites/char/right_3.png")]
walk_left = [pygame.image.load("./assets/sprites/char/left_2.png"), pygame.image.load("./assets/sprites/char/left_3.png")]
walk_for = [pygame.image.load("./assets/sprites/char/for_2.png"), pygame.image.load("./assets/sprites/char/for_3.png")]
walk_back = [pygame.image.load("./assets/sprites/char/back_2.png"), pygame.image.load("./assets/sprites/char/back_3.png")]

stand_right = pygame.image.load("./assets/sprites/char/right_1.png")
stand_left = pygame.image.load("./assets/sprites/char/left_1.png")
stand_for = pygame.image.load("./assets/sprites/char/for_1.png")
stand_back = pygame.image.load("./assets/sprites/char/back_1.png")

bg = []

def tick():
    global char_x, char_y, vel, moving_left, moving_right, moving_for, moving_back
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and char_x > 0:
        char_x -= vel
        moving_for = False
        moving_back = False
        moving_left = True
        moving_right = False
    elif keys[pygame.K_RIGHT] and char_x < SCREEN_SIZE[0] - char_w:
        char_x += vel
        moving_for = False
        moving_back = False
        moving_left = False
        moving_right = True
    elif keys[pygame.K_UP] and char_y > 0:
        char_y -= vel
        moving_for = False
        moving_back = True
        moving_left = False
        moving_right = False
    elif keys[pygame.K_DOWN] and char_y < SCREEN_SIZE[1] - char_h:
        char_y += vel
        moving_for = True
        moving_back = False
        moving_left = False
        moving_right = False
    else:
        moving_for = False
        moving_back = False
        moving_left = False
        moving_right = False
        walkcount_x = 0
        walkcount_y = 0

def render():
    global walkcount_x, walkcount_y
    screen.fill((0,0,0))
    
    if walkcount_x + 1 >= FPS:
        walkcount_x = 0
    if walkcount_y + 1 >= FPS:
        walkcount_y = 0

    if moving_left:
        screen.blit(walk_left[walkcount_x // WALK_PER_FRAME], (char_x, char_y))
        walkcount_x += 1
    elif moving_right:
        screen.blit(walk_right[walkcount_x // WALK_PER_FRAME], (char_x, char_y))
        walkcount_x += 1 
    elif moving_for:
        screen.blit(walk_for[walkcount_y // WALK_PER_FRAME], (char_x, char_y))
        walkcount_y += 1
    elif moving_back:
        screen.blit(walk_back[walkcount_y // WALK_PER_FRAME], (char_x, char_y))
        walkcount_y += 1
    else:
        screen.blit(stand_for, (char_x, char_y))
    
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