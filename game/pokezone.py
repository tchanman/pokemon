import pygame

class PokeZone(object):
    def __init__(self, hasPokemon=False, battle_type=None, pokedict=None, ent_list=None):
        self.hasPokemon = hasPokemon
        self.battle_type = battle_type
        self.pokedict = pokedict
        self.ent_list = ent_list

    def handleGrass(self):
        print("handling grass")