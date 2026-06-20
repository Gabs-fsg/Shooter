import pygame

print('Iniciando setup...')
pygame.init()
screen = pygame.display.set_mode((800, 600))
print('Finalizando setup...')

print('Iniciando loop...')
while True:
    # Checagem de todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Saindo...')
            pygame.quit() # Fecha janela
            quit() # Finaliza pygame


