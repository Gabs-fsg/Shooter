import pygame

from code.const import ENTITY_SPEED, W_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.velocity_y = 0
        self.gravity = ENTITY_SPEED[self.name]
        self.jump_strength = -ENTITY_SPEED[self.name]*10
        self.on_ground = True

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        # pula
        if pressed_key[pygame.K_UP] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False
        # aplica gravidade
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Checa se voltou ao chao
        if self.rect.bottom >= 290:  #y=290
            self.rect.bottom = 290
            self.velocity_y = 0
            self.on_ground = True
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < W_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
