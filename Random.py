import random
def Random1(matriz, filas, columnas):
    i=0 
    while i<filas:
        j=0
        while j<columnas:
            temp= random.randint(0, 1)
            matriz[i][j] = temp
            j=j+1
        i+=1 
