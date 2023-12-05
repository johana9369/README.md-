import os
import random
import readchar
from typing import List, Tuple
from readchar import readkey, key  
#escriba el combre
nombre = input('escriba su nombre: ')
print(f'bienvenido a tu juego {nombre:}')

#crear los muros del laberionto
def muros_laberintos(pared_laberinto, end):
     #filas  para crear las paredes del laberinto
    filas = pared_laberinto.strip().split('\n')    
    #separo las filas con \n
    while len(filas) < end + 1:
        filas.append("#" * (end + 1 - len(filas)))
    #numero de filas incrementando en n+1
    for i in range(len(filas)):
        while len(filas[i]) < end + 1:
            filas[i] += '#'
    #suma de las partes del laberinto
    laberinto_partes = '\n'.join(filas)
    return laberinto_partes
    #matriz inicial
def matriz(pared_laberinto):
    #crear con la funcion flas la pared de laberinto
    filas = pared_laberinto.strip().split('\n')
    
    laberinto = [list(fila) for fila in filas]
    return laberinto

def mostrar_laberinto_limpiar(laberinto):
    os.system('cls' if os.name == 'nt' else 'clear')  
    for fila in laberinto:
        print(''.join(fila))

def main_loop(mapa, inicio, fin):
    # Desempaquetar las coordenadas de inicio
    px, py = inicio

    # Bucle principal: continúa hasta que las coordenadas actuales sean iguales a las coordenadas de destino
    while (px, py) != fin:
        # Colocar el objeto en la posición actual en el mapa
        mapa[py][px] = '☻'

        # Mostrar el laberinto actualizado en la consola
        mostrar_laberinto_limpiar(mapa)

        # Leer la tecla presionada por el usuario
        teclado = readkey()

        # Calcular las nuevas coordenadas basándose en la tecla presionada
        nueva_px, nueva_py = px, py

        if teclado == key.UP and py > 0 and mapa[py - 1][px] != '#':
            nueva_py -= 1
        elif teclado == key.DOWN and py < len(mapa) - 1 and mapa[py + 1][px] != '#':
            nueva_py += 1
        elif teclado == key.LEFT and px > 0 and mapa[py][px - 1] != '#':
            nueva_px -= 1
        elif teclado == key.RIGHT and px < len(mapa[0]) - 1 and mapa[py][px + 1] != '#':
            nueva_px += 1

        # Limpiar la posición anterior del objeto en el mapa
        mapa[py][px] = ' '

        # Actualizar las coordenadas actuales con las nuevas
        px, py = nueva_px, nueva_py

if __name__ == "__main__":
    
    laberinto_generado = """
..#############################
..#.......#.#.#...............#
#.#.#.#####.#.#.#####.#.#.#####
#...#...#.....#.#.....#.#.#...#
#####.#.#.###.#.#.#####.###.#.#
#.#...#.....#...#.#...#.....#.#
#.#.#########.#######.#####.###
#.#.#.....#.#.....#...#...#...#
#.#.###.###.#.#####.###.#.#.###
#.......#...........#...#.#...#
#.#.###.#.#######.###.#######.#
#.#.#.#.#.....#.....#.....#...#
###.#.###.#####.###.#.#########
#.......#.....#.#...#.........#
#.#.###.#.#.###.#####.#########
#.#.#...#.#...#.#.....#.......#
#.###.#########.#.###.#.#.#####
#...#.#.....#...#.#.#...#.....#
###.###.#.###.#####.#.#####.#.#
#.#.#...#...........#.#.#...#.#
#.#.#########.###.###.#.#######
#...#...#.......#.....#...#...#
#####.#####.###.#########.#.###
#.....#...#.#...#.#...#...#.#.#
#####.###.#####.#.#.#.#.#.#.#.#
#...#...#.....#.....#.#.#.....#
#.#.#.#.#.#####.###.###.#.###.#
#.#...#...........#.#.#.#.#...#
###.#.#.###.#.###.###.#.#####.#
#...#.#.#...#.#.............#..
##############################.

"""
    end = 20
    
    laberinto_partes = muros_laberintos(laberinto_generado, end)
    
    mapa = matriz(laberinto_partes.strip())

    inicio  = (0, 0)
    fin = (end, end)

    main_loop(mapa, inicio, fin)

    print(f" {nombre} finalizo el laberinto")