import pygame

class ExitZone(object):
    def __init__(self, exit_ent, spawn_change, level_to, rel_spawn):
        self.exit_ent = exit_ent
        self.spawn_change = spawn_change
        self.level_to = level_to
        self.rel_spawn = rel_spawn #bool if spawn change is rel, if false it's absolute