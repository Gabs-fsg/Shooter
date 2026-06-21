import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))

    def run(self):
        while True:
            # trata eventos da janela para nao travar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # atualiza e desenha entidades
            for ent in self.entity_list:
                ent.move()  # se tiver movimento
                self.window.blit(ent.surf, ent.rect)

            pygame.display.flip()

