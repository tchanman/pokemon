import pygame
from game.entity import Entity

class PokeZone(Entity):
    def __init__(self, pos, dimensions, pokedict, battle_type):
        self.color = (255, 0, 0, 100)
        super().__init__(pos, dimensions, self.color)

        self.pokedict = pokedict
        self.battle_type = battle_type