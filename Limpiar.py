import BorrarTerminal

def limpiar(matriz, filas, columnas):
    i=0 
    while i<filas:
        j=0
        while j<columnas:
            print(matriz)
            if matriz[i][j]==1:
                matriz[i][j] = 0
            j=j+1
            input("Presione cualquier tecla para continuar...")
            BorrarTerminal.limpiar_terminal()
        i+=1 
    print("Limpieza completada")
    print(matriz)