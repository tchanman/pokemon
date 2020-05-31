import pygame, easygui, pickle, sys, os
from datetime import datetime

pygame.init()

class Menu(object):
    def __init__(self, save_data=None):
        self.save_data = save_data

        self.img = pygame.image.load("./assets/menu/menu.png")
        self.arrow = pygame.image.load("./assets/menu/menu-arrow.png")
        
        self.is_running = False
        self.menu_result = {
            "notquitting": True,
            "saving": False,
            "loading": False,
            "load_data": None
        }

        self.selected_option = 60
        self.arrow_pos = [845,self.selected_option]
        
        self.fnt = pygame.font.SysFont("couriernew", 32, bold=1)
        self.menu_text = ""
        self.menu_text_surf = self.fnt.render(self.menu_text, 1, (0,0,0))
        self.textbox = pygame.image.load("./assets/menu/textbox.png")
    
    def render(self, screen, debug = False):
        screen.blit(self.img, (0,0))

        self.arrow_pos = [845,self.selected_option]
        screen.blit(self.arrow, self.arrow_pos)

        if self.menu_result["saving"]:
            self.menu_text = "Saving..."
            screen.blit(self.textbox, (0,0))
            screen.blit(self.menu_text_surf, (50,540))
        
    def handleMenu(self, key, screen, save_data):
        self.menu_result = {
            "notquitting": True,
            "saving": False,
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
                self.save(screen, save_data)
            elif self.selected_option == 260:
                self.menu_result["loading"] = True
                self.menu_result["load_data"] = self.load()
            elif self.selected_option == 310:
                print("Quitting game.")
                self.menu_result["notquitting"] = False
        
        if self.selected_option < 60:
            self.selected_option = 310
        if self.selected_option > 310:
            self.selected_option = 60

        return self.menu_result

    def save(self, screen, save_data):
        print("Saving game...")
        if self.save_data == None:
            self.save_data = {
                "save_iteration": 0
            }
        self.menu_result["saving"] = True

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
        pygame.mixer.Sound("./assets/sounds/sfx/SFX_SAVE.wav").play()
        self.menu_text = "Game saved."

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