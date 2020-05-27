import pygame, easygui, pickle, sys, os

class Menu(object):
    def __init__(self, save_data):
        self.img = pygame.image.load("./assets/menu/menu.png")
        self.arrow = pygame.image.load("./assets/menu/menu-arrow.png")
        self.is_running = False
        self.selected_option = 60

        self.arrow_pos = [845,self.selected_option]
        self.save_data = save_data

    def handleMenu(self,key):

        if key == pygame.K_UP:
            self.selected_option -= 50
        elif key == pygame.K_DOWN:
            self.selected_option += 50
        elif key == pygame.K_RETURN:
            if self.selected_option == 60:
                self.pokedex()
            elif self.selected_option == 110:
                self.pokemon()
            elif self.selected_option == 160:
                self.bag()
            elif self.selected_option == 210:
                self.save()
            elif self.selected_option == 260:
                self.options()
            elif self.selected_option == 310:
                print("Quitting game.")
                return False
        
        if self.selected_option < 60:
            self.selected_option = 310
        if self.selected_option > 310:
            self.selected_option = 60

        print(self.selected_option)
        return True

    def render(self, screen, debug = False):
        screen.blit(self.img, (0,0))

        self.arrow_pos = [845,self.selected_option]
        screen.blit(self.arrow, self.arrow_pos)

    def save(self):
        print("Saving game state.")

        self.save_data["save_iteration"] += 1

        homedir = os.path.dirname(__file__)
        savepath = 'saves\pokesave' + str(self.save_data["save_iteration"]) + '.dat'
        savefile = os.path.join(homedir, savepath)

        pickle.dump(self.save_data, open(savefile, "wb"))

    def load(self):
        print("Loading save...")

        homedir = os.path.dirname(__file__)
        savedir = os.path.join(dirname, 'saves')

        path = easygui.fileopenbox(default=savedir, filetypes="*.dat")

        try:
            self.save_data = pickle.load(open(path, "rb"))
        except:
            print("A problem occured while loading this file.")
        else:
            print("Save file successfully loaded from " + path)

    def pokedex(self):
        print("Opening pokedex.")

    def pokemon(self):
        print("Opening pokemon.")

    def bag(self):
        print("Opening bag.")

    def options(self):
        print("Opening options.")