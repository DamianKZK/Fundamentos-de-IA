import os

def limpiar_terminal():
    # 'nt' es el nombre interno para Windows, 'posix' para Linux/Mac
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')