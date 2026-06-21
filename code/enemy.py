import random

from code.const import W_WIDTH, ENTITY_SPEED, W_HEIGHT
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # posição inicial: topo da tela em x aleatório
        random_x = random.randint(0, W_WIDTH)  # ajuste para largura da janela
        super().__init__(name, (random_x, 0))
        self.speed = ENTITY_SPEED[self.name]

    def move(self, ):
        # movimento para baixo
        self.rect.y += self.speed
        # se sair da tela pela parte inferior, "desaparece"
        if self.rect.top > W_HEIGHT:
            #resetar para o topo em nova posição aleatória
            self.rect.x = random.randint(-10, W_WIDTH)
            self.rect.y = 0

