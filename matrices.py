
fi=int(input("¿Cuantas filas tiene la primera matriz? "))
col1=int(input("¿Cuantas columnas tiene la primera matriz? "))
col2=int(input("¿Cuantas columnas tiene la segunda matriz? "))

A=[]
for i in range (fi):
    A.append([0]*col1)
    print(A[i])



B=[]
for i in range (col1):
    B.append([0]*col2)

print ("Para tu Primera matriz: ")
for i in range (fi):
    for j in range (col1):
        A[i][j]=float(input("Cual es el numero en la posicion (%d,%d): " % (i,j)))

print ("Para tu Segunda matriz: ")
for i in range (col1):
    for j in range (col2):
        B[i][j]=float(input("Cual es el numero en la posicion (%d,%d): " % (i,j)))


C=[]
for i in range (fi):
    C.append([0]*col2)


for i in range (fi):
    for j in range (col2):
        for k in range (col1):
            C[i][j] += A[i][k] * B[k][j]

for i in range (fi):
    print(C[i])
