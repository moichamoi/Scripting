import json
f=open("./hola.json",)
inicio = json.load(f)
print(str(inicio["historia"][0]["part1"]))
opc=int(input("Opcion 1 o 2: "))

if opc == 1:
    print(str(inicio["historia"][1]["vec"]))
    h=1
elif opc == 2:
    print (str(inicio["historia"][2]["5min"]))
    h=2

f=open("./hola2.json")
inicio  = json.load(f)


if h == 2:
    opc=int(input("Opcion 1 o 2 o 3: "))
    if opc == 1:
        print(str(inicio["opciones"][0]["opc1"]))
        opc=int(input("Opcion 1 o 2 o 3: "))
        if opc == 1:
            print(str(inicio["opciones"][1]["foto"]))
        elif opc == 2:
            print(str(inicio["opciones"][1]["reloj"]))
        elif opc == 3:
            print(str(inicio["opciones"][1]["diario"]))
    elif opc == 2:
        print(str(inicio["opciones"][3]["cap"]))
    elif opc == 3:
        print(str(inicio["opciones"][4]["boc"]))

print(str(inicio["opciones"][2]["opc2"]))
f=open("./opcion.json")
inicio  = json.load(f)
opc=int(input("Opcion 1 o 2: "))
if opc == 1:
    print(str(inicio["op"][0]["hab"]))
elif opc == 2:
    print(str(inicio["op"][1]["con"]))