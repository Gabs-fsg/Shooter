import random

import pygame
from pygame.font import Font
from pygame.surface import Surface

from code.const import C_WHITE, W_HEIGHT, EVENT_ENEMY, SPAWN_TIME
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.entity_list.append(EntityFactory.get_entity('player'))
        self.entity_list.append(EntityFactory.get_entity('enemy1'))
        self.entity_list.append(EntityFactory.get_entity('enemy2'))
        self.timeout = 20000  # 20segundos
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.ogg')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # para definir quantos fps o jogo vai rodar
        while True:
            clock.tick(60)
            # trata eventos da janela para nao travar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # atualiza e desenha entidades
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            # textos impressos na tela
            self.lvl_tx(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.lvl_tx(14, f'fps:{clock.get_fps():.0f}', C_WHITE, (10, W_HEIGHT - 35))
            self.lvl_tx(14, f'entidades:{len(self.entity_list)}', C_WHITE, (10, W_HEIGHT - 20))
            pygame.display.flip()


    def lvl_tx(self, tx_size: int, tx: str, tx_color: tuple, tx_pos: tuple):
        tx_font: Font = pygame.font.Font("./asset/neonix.ttf", tx_size)
        tx_surf: Surface = tx_font.render(tx, True, tx_color).convert_alpha()
        tx_rect = tx_surf.get_rect(left=tx_pos[0], top=tx_pos[1])
        self.window.blit(tx_surf, tx_rect)
