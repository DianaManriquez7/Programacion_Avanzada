{}
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np

                 # 0 1 2 3 4 5 6 
Isla = np.matrix ('1 1 0 0 0 0 0 ;' #0
                 ' 0 0 0 1 1 0 0 ;' #1
                 ' 0 0 0 1 1 0 1 ;' #2
                 ' 0 1 0 0 0 0 1 ;' #3
                 ' 0 1 0 0 0 0 0' ) #4

# print(Isla)
#
NumIsla=0

#Dimensión de la matriz
R, C = np.shape(Isla) #Entrega el numero de renglones y columnas en su 
                      #respectiva variable segun la matriz
ORD=[] #Una lista para que me almacene las posiciones de 1

#Otra matriz con la misma cantidad de RxC que este llenas de 0 que representen false
#esto para rastrear las posiciones donde ya visitamos y hay un 1. (para no repetir posiciones)
Visitadas= np.zeros((R, C), dtype=bool) 

print (f'Tamaño de la matriz: Filas: {R} y Columnas: {C}')

#------------------------------------------------------------
# Direcciones
                # Arriba, Abajo, Izquierda, Derecha
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

# Función DFS para recorrer las posiciones conectadas, def es definir una funcion en este caso dfs 
# Busqueda de profundidad en una matriz (coordenadas) funcion recursiva
def dfs(i, j):
    # Marcar como visitada la posición actual
    Visitadas[i, j] = True
    ORD.append([i, j])  # Guardar la posición de los 1 en una lista

    # Recorrer en las 4 direcciones
    for d in direcciones:
        #fila,columna = i+d[0] es el desplazamiento en la fila (vertical), ya sea -1 (subir), +1 (bajar), o 0 (no moverse verticalmente). 
                        #d[1] es el desplazamiento en la columna (horizontal), ya sea -1 (ir a la izquierda), +1 (ir a la derecha), o 0 (no moverse horizontalmente).
        ni, nj = i + d[0], j + d[1] #Nuevas filas de desplazamiento (de las direcciones)
        
 # Verificar si ni y nj están dentro de los límites de la matriz, verifica que en la posicion de la Isla[ni, nj] contenga 1 
 #(Si la celda contiene un 0, no se continúa la búsqueda en esa dirección) y verifica que la posición (ni, nj) no ha sido visitada aún
 
        if 0 <= ni < R and 0 <= nj < C and Isla[ni, nj] == 1 and not Visitadas[ni, nj]:
            dfs(ni, nj)
#---------------------------------------------------------------------------------------
'''# Iterar sobre la matriz
for i in range(R):
    for j in range(C):
        # Si encontramos un 1 y no ha sido visitado, iniciar DFS
        if Isla[i, j] == 1 and not Visitadas[i, j]:
            dfs(i, j) #De forma recursiva para continuar explorando la isla desde la nueva posición (ni, nj)

# Imprimir las posiciones de las islas encontradas
print("Posiciones de los 1 en la isla:")
print(ORD)'''

# Iterar sobre la matriz para encontrar islas
for i in range(R):
    for j in range(C):
        # Si encontramos un 1 y no ha sido visitado, significa que hemos encontrado una nueva isla
        if Isla[i, j] == 1 and not Visitadas[i, j]:
            NumIsla += 1     # Incrementar el contador de islas
            dfs(i, j)          # Realizar DFS para visitar toda la isla

# Imprimir la cantidad de islas encontradas
print(f'Número de islas de 1s: {NumIsla}')



