from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, name:str, position:tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png') #caminho generico para poder carregar tanto player, quanto bg e inimigos
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) #posicao generica também
        self.speed = 0

    @abstractmethod #decorator
    def move(self, ):
        pass
