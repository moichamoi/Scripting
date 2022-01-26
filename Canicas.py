from os import pardir
import random, sys

cj = 10
c = 10

while (True):
    p = int(input("Cual es tu apuesta? "))
    if p <= cj and p > 0:
        res = str(input("Que escoges par o impar? "))
        a = random.randrange (0,c)
        
        if a == 0:
            a=1+a

        if a %2 == 0:
            r="par"
            print(r,a)
        else:
            r="impar"
            print(r,a)
        if res == "par" and r == "par" or res == "impar" and r == "impar":
            cj = cj + a
            c= c - a
            print ("Genial, ganaste ", a ," canica(s)")
            print ("Tienes ", cj, " canica(s)")
        elif res == "impar" and r == "par" or res == "par" and r == "impar":
            cj = cj - p
            c = c + p
            print ("fallaste, perdiste ", p ," canica(s)")
            print ("Te quedan ", cj, " canica(s)")
        
        if c < 1 or cj < 1:
            break 
    else:
        print ("Favor de ingresar un numero valido")

if cj == 20:
    print ("Genial ganaste *matan al rival*")
elif c == 20:
    print ("Perdiste *Te matan*")