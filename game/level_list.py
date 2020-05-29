import pygame
from game.level import Level
from game.entity import Entity
from game.exitzone import ExitZone
from game.pokezone import PokeZone

pygame.init()
# level selection
# TREE WIDTH = 65 + 5, 75 + 5
level_list = {
    "hometown": Level(
        pygame.image.load("./assets/bgs/hometown.png"),
        pygame.mixer.Sound("./assets/sounds/SFX_SAFARI_ZONE_PA.wav"),
        [
            Entity([0,0], [430,75]), # level walls
            Entity([0,0], [220, 720]),
            Entity([0, 560], [1080, 720]),
            Entity([1080-224, 0], [224, 720]),
            Entity([1080-434,0], [434,75]),
            
            Entity([315,90], [140,80]), # topleft house
            Entity([315,90], [35,110]),
            Entity([400,90], [55,110]),

            Entity([620,90], [140,80]), # topright house
            Entity([620,90], [35,110]),
            Entity([705,90], [55,110]),

            Entity([620,310], [140,80]), # bottomright house
            Entity([620,310], [35,110]),
            Entity([705,310], [55,110]),

            Entity([300,310], [180,80]), # oakslab
            Entity([300,310], [65,110]),
            Entity([415,310], [65,110]),
        ], [
            ExitZone([430, 0], [220, 5], (0,670), "route1", True), # exit to route 1
            # ExitZone([360, 180], [35, 5], (527,570) , "oakslab", False), # topleft house
            ExitZone([375, 400], [35, 5], (527,570) , "oakslab", False), # oakslab house
        ], [
            # PokeZone()
    ]),
    "route1": Level(
        pygame.image.load("./assets/bgs/route1.png"), 
        None,
        [
            Entity([0,0], [150, 720]), # left side
            Entity([0,0], [360, 75]),
            Entity([0,0], [220, 155]),
            Entity([0,240], [220, 155]),
            Entity([0,285], [285, 75]),
            Entity([0,480], [220, 155]),
            Entity([0,560], [430, 160]),

            Entity([925,0], [1080-925, 720]), # right side
            Entity([575,0], [1080-575, 75]),
            Entity([715,0], [1080-715, 155]),
            Entity([855,0], [1080-855, 235]),
            Entity([855,480], [1080-855, 720-480]),
            Entity([645,480], [65, 720-480]),
            Entity([645,560], [1080-645, 160]),

            Entity([575,185], [65, 155]), # middle trees
            Entity([510,225], [130, 75]),
        ], [
            ExitZone([430, 715], [215, 5], (0,-670) , "hometown", True), # exit to hometown
            # ExitZone([360, 0], [215, 5], (0,670) , "hometown", True) # exit to route2
        ], [
            # PokeZone()
    ]),
    "oakslab": Level(
        pygame.image.load("./assets/bgs/oakslab.png"), 
        None,
        [
            Entity([0,0], [295, 720]), # level walls
            Entity([0,0], [1080, 190]),
            Entity([0,605],[515,115]),
            Entity([1080-510,605],[510,115]),
            Entity([790,0],[295,720])
        ], [
            ExitZone([515, 620], [54, 100], (375,410) , "hometown", False, True) # exit to hometown
        ], [
        # PokeZone()
    ])
}