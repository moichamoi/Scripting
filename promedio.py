x = int(input("Cuantas calificaciones vas a ingresar? "))

s = 0
c = 1

while (c <= x):
    print ("Cual es la calificacion no.", c )
    cal = float(input())
    s=s+cal
    c+=1

prom = (s/x)
print (prom)