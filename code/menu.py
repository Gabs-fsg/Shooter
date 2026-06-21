from idlelib.multicall import MC_OPTION

from pygame.font import Font
import pygame.image
from pygame.surface import Surface

from code.const import W_WIDTH, C_PURPLE, M_OPTION, C_WHITE # importando constantes


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menubg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/menubg.ogg') #carrega a musica
        pygame.mixer.music.play(-1) #musica toca em loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_tx(80,"Crystal",C_PURPLE, ((W_WIDTH/2),70))
            self.menu_tx(80, "Run", C_PURPLE, ((W_WIDTH / 2), 150))

            for i in range(len(M_OPTION)):
                self.menu_tx(20, M_OPTION[i], C_WHITE, ((W_WIDTH / 2), 230+30*i))


            pygame.display.flip()

            # Checagem de todos os eventos
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                   pygame.quit() # Fecha janela
                   quit() # Finaliza pygame

    def menu_tx(self, tx_size: int, tx: str, tx_color: tuple, tx_center_pos: tuple):
        tx_font: Font = pygame.font.Font("./asset/neonix.ttf", tx_size)
        tx_surf: Surface = tx_font.render(tx, True, tx_color).convert_alpha()
        tx_rect = tx_surf.get_rect(center=tx_center_pos)
        self.window.blit(tx_surf, tx_rect)

