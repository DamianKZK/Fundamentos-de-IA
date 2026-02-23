import numpy as np
import Manual
import Random
import Limpiar

filas = int(input("Ingrese las filas de su matriz:"))
columnas = int(input("Ingrese las columnas de su matriz:"))
matriz = np.zeros((filas,columnas))
print(matriz)

op = int(input("¿Como desea inicializar su matriz?\n1->Manual\n2->Random\n"))
match op:
    case 1:Manual.manual(matriz, filas, columnas)
    case 2:Random.Random1(matriz, filas, columnas)
limp = int(input("¿Desea empezar a aspirar?\n1->Si\n2->No\n"))
if limp==1:
    Limpiar.limpiar(matriz, filas, columnas)
else:
    print("Saliendo...")
