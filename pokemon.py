import pygame
from entity import Entity

class Pokemon(Entity):
    def __init__(self, id, name, poketype, evlevel, sprite, stats, moves):
        self.id = id
        self.name = name
        self.poketype = poketype
        self.evlevel = evlevel
        self.sprite = sprite
        
        self.stats = stats
        self.moves = moves