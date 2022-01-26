import sys
import pygame
import math
pygame.init()


while 1:
    res = int(input("Que figura quieres? Cuadrado [1]  Circulo [2]  Cruz [3]  "))

    size = width, height = 1920, 1080
    speed = [0,4]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("coche.png")
    ballrect = ball.get_rect()

    

    if res == 1:
        c = 0
        while 1 :


            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            ballrect = ballrect.move(speed)
        

            if ballrect.bottom > height: 
                speed = [4,0]

            if ballrect.right > width:
                speed = [0,-4]

            if ballrect.top < 0:
                speed = [-4,0]

            if ballrect.left < 0:
                speed = [0,4]
                if ballrect.bottom > height: 
                    speed = [4,0]
                    c = c + 1
        
            if c == 5:
                break
            screen.fill(black)
            screen.blit(ball, ballrect)
            pygame.display.flip()
            

            

    elif res == 2:
        c = 0
        angulo = 0
        rad = 200

        while 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            if angulo > 15:
                break

            ballrect = ballrect.move(speed)
        
            ballrect.x = rad * math.cos(angulo) + width/2-100
            ballrect.y = rad * math.sin(angulo) + height/2-100
            angulo += 0.006
            
        

            screen.fill(black)
            screen.blit(ball, ballrect)
            pygame.display.flip()
            

    elif res == 3:
        c = 0
        ballrect.x = width
        ballrect.y = height

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            ballrect = ballrect.move(speed)
            

            if ballrect.bottom > height: 
                speed = [0,4]

            if ballrect.bottom > height:
                ballrect.x = 0
                ballrect.y = height/2-100
                speed = [4,0]

            if ballrect.right > width:
                ballrect.x = width/2-100
                ballrect.y = 0
                speed = [0,4]
                c = c + 1

            if c == 5:
                break
            
            
            screen.fill(black)
            screen.blit(ball, ballrect)
            pygame.display.flip()
            
        
