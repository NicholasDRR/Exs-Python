import pygame
from pygame.locals import *
from sys import exit

pygame.init() # Inicialiando o pygame

largura = 640
altura = 480
x = largura / 2 - 25
y = 0
relogio = pygame.time.Clock()
# Definindo display
tela = pygame.display.set_mode((largura, altura))  
pygame.display.set_caption('Jogo teste') # Título da aba

# Criando loop pra rodar o jogo
while True:
    relogio.tick(100)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    #x += 1
    if y >= altura:
        y = 0
    y += 1
    #pygame.draw.circle(tela, (0,0,255), (300, 260), 40) 
    #pygame.draw.line(tela, (255,255,0), (390, 0), (390, 600), 5)
    
    pygame.display.update()