import pygame

class PokeZone(object):
    def __init__(self, zone_ent, pokedict, battle_type, spawn_rate=0):
        self.zone_ent = zone_ent
        self.pokedict = pokedict
        self.battle_type = battle_type
        self.spawn_rate = spawn_rate