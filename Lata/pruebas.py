import pygame
from pygame.locals import *
 
pygame.init()
 
pantalla = pygame.display.set_mode((1920,1080),0,32)
imagen = pygame.image.load("vacio.png")
 
x = 10
y = 10
i = 0
 
reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed()
 
    if pulsada[K_w]:
        i += 1
    if pulsada[K_s]:
        i -= 1


    if i == 0:
        imagen = pygame.image.load("vacio.png")
    if i == 1:
        imagen = pygame.image.load("mediovacio.png")
    if i == 2:
        imagen = pygame.image.load("llenito.png")
    if i == 3:
        imagen = pygame.image.load("mitad.png")
    if i == 4:
        imagen = pygame.image.load("mas mitad.png")
    if i == 5:
        imagen = pygame.image.load("lleno.png")

    
    reloj.tick(25)
    pantalla.fill((0,0,0))
    pantalla.blit(imagen,(x,y))
    pygame.display.update()