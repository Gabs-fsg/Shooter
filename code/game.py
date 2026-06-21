import pygame

from code.const import W_WIDTH, W_HEIGHT, M_OPTION
from code.level import Level
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == M_OPTION[0]:
                lvl = Level(self.window,'level1')
                lvl.run()
            elif menu_return == M_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass




