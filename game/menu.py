import pygame, easygui, pickle, sys, os
from datetime import datetime

pygame.init()

class Menu(object):
    def __init__(self, save_data=None):
        self.img = pygame.image.load("./assets/menu/menu.png")
        self.arrow = pygame.image.load("./assets/menu/menu-arrow.png")
        self.is_running = False
        self.selected_option = 60

        self.arrow_pos = [845,self.selected_option]
        self.save_data = save_data
    
    def render(self, screen, debug = False):
        screen.blit(self.img, (0,0))

        self.arrow_pos = [845,self.selected_option]
        screen.blit(self.arrow, self.arrow_pos)
        
    def handleMenu(self, key, save_data):
        menuResult = {
            "notquitting": True,
            "loading": False,
            "load_data": None
        }
        if key == pygame.K_UP:
            self.selected_option -= 50
        elif key == pygame.K_DOWN:
            self.selected_option += 50
        elif key == pygame.K_RETURN:
            pygame.mixer.Sound("./assets/sounds/sfx/SFX_PRESS_AB.wav").play()
            if self.selected_option == 60:
                self.pokedex()
            elif self.selected_option == 110:
                self.pokemon()
            elif self.selected_option == 160:
                self.bag()
            elif self.selected_option == 210:
                self.save(save_data)
            elif self.selected_option == 260:
                menuResult["loading"] = True
                menuResult["load_data"] = self.load()
            elif self.selected_option == 310:
                print("Quitting game.")
                menuResult["notquitting"] = False
        
        if self.selected_option < 60:
            self.selected_option = 310
        if self.selected_option > 310:
            self.selected_option = 60

        return menuResult

    def save(self, save_data):
        
        if self.save_data == None:
            self.save_data = {
                "save_iteration": 0
            }

        self.save_data["level"] = save_data["level"]
        self.save_data["pos"] = save_data["pos"]
        self.save_data["last_dir"] = save_data["last_dir"]
        self.save_data["save_iteration"] += 1

        date_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        gamedir = os.path.dirname(__file__)
        homedir = os.path.dirname(gamedir)
        savepath = 'saves\pokesave' + date_string + '.dat'
        savefile = os.path.join(homedir, savepath)

        pickle.dump(self.save_data, open(savefile, "wb"))

    def load(self):
        print("Loading save...")

        gamedir = os.path.dirname(__file__)
        homedir = os.path.dirname(gamedir)
        savedir = os.path.join(homedir, 'saves/')

        path = easygui.fileopenbox(default=savedir, filetypes="*.dat")

        try:
            self.save_data = pickle.load(open(path, "rb"))
        except:
            print("A problem occured while loading this file.")
            return None
        else:
            print("Save file successfully loaded from " + path)
            return self.save_data

    def pokedex(self):
        print("Opening pokedex.")

    def pokemon(self):
        print("Opening pokemon.")

    def bag(self):
        print("Opening bag.")

    def options(self):
        print("Opening options.")