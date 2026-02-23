import BorrarTerminal

def manual(matriz, filas, columnas):
    i=0 
    while i<filas:
        j=0
        while j<columnas:
            print(matriz)
            temp= int(input(f"¿El segmento {i}, {j} esta sucio o limpio?\n0->Limpio\n1->Sucio\n"))
            if temp!=0 and temp!=1:
                print("Valor invalido")
                return
            matriz[i][j] = temp
            j=j+1
            BorrarTerminal.limpiar_terminal()
        i+=1 
    