import pygame
from game.level import Level
from game.entity import Entity
from game.exitzone import ExitZone

# level selection
# TREE WIDTH = 65 + 5, 75 + 5
level_list = {
    "hometown": Level(pygame.image.load("./assets/bgs/hometown.png"), [
        Entity([0,0], [430,75]), # level walls
        Entity([0,0], [220, 720]),
        Entity([0, 560], [1080, 720]),
        Entity([1080-224, 0], [224, 720]),
        Entity([1080-434,0], [434,75]),
        
        Entity([315,90], [140,80]), # topleft house
        Entity([315,90], [40,120]),
        Entity([395,90], [60,120]),

        Entity([620,90], [140,80]), # topright house
        Entity([620,90], [40,120]),
        Entity([700,90], [60,120]),

        Entity([620,310], [140,80]), # bottomright house
        Entity([620,310], [40,120]),
        Entity([700,310], [60,120]),

        Entity([300,310], [180,80]), # oakslab
        Entity([300,310], [70,120]),
        Entity([410,310], [70,120]),
    ],[
        ExitZone( Entity([430, 0], [220, 5], color=(0,255,0,50)), (0,670) , "route1", True), # exit to route 1
        ExitZone( Entity([360, 180], [35, 5], color=(0,255,0,50)), (527,570) , "oakslab", False), # topleft house
        ExitZone( Entity([375, 400], [35, 5], color=(0,255,0,50)), (527,570) , "oakslab", False), # oakslab house
    ], [

    ]),
    "route1": Level(pygame.image.load("./assets/bgs/route1.png"), [
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
        ExitZone( Entity([430, 715], [215, 5], color=(0,255,0,50)), (0,-670) , "hometown", True), # exit to hometown
        ExitZone( Entity([360, 0], [215, 5], color=(0,255,0,50)), (0,670) , "hometown", True) # exit to route2
    ], [

    ]),
    "oakslab": Level(pygame.image.load("./assets/bgs/oakslab.png"), [
        Entity([0,0], [295, 720]), # level walls
        Entity([0,0], [1080, 190]),
        Entity([0,605],[515,115]),
        Entity([1080-510,605],[510,115]),
        Entity([790,0],[295,720])
    ], [
        ExitZone( Entity([515, 620], [54, 100], color=(0,255,0,50)), (375,410) , "hometown", False) # exit to hometown
    ], [

    ])
}