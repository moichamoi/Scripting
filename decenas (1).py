numeros = [int(x) for x in input("Ingresa tus numeros separados con un espacio: ").split(' ')]
num2= [
    [],[],[],[],[] 
    ]


for i in numeros:
    for e,j in enumerate(num2):
        if i<= e*10 and i >e*10-10:
            num2[e].append(i)
for u in (num2):
    if len(u) >3:
        for o in range(0,2):
            print (u[o])
    else:
        print(u)
