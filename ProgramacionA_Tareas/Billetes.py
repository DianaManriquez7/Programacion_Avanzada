# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:09:49 2024

@author: PC
"""
'''
Max=100
billete50=50
billete20=20
moneda10=10
moneda5=5
moneda1=1

N=0 #Inicializar
M=0
for i in range(Max):
    if N<=100:
       N=moneda1+i

print(N)

    
print(M)
    '''

""" 
    ##Cambio de las monedad
def descomponer_dinero(cantidad):
    # Lista de billetes y monedas disponibles, de mayor a menor valor
    denominaciones = [100, 50, 20, 10, 5, 2, 1]
    
    # Almacenar cuántos billetes/monedas de cada denominación se necesitan
    resultado = {}
    
    # Recorremos cada denominación
    for denominacion in denominaciones:
        # Calculamos cuántos billetes/monedas de esta denominación podemos usar
        if cantidad >= denominacion:
            cantidad_de_denominacion = cantidad // denominacion  # División entera
            resultado[denominacion] = cantidad_de_denominacion   # Guardamos el resultado
            cantidad = cantidad % denominacion  # Restamos esa cantidad
    
    return resultado


cantidad = 350  # Monto a descomponer
resultado = descomponer_dinero(cantidad)

# Imprimir el resultado
print(f"La descomposición de {cantidad} es:")
for denominacion, cantidad in resultado.items():
    print(f"{cantidad} billetes/monedas de {denominacion} pesos")
"""
#######################################################################################################################
#Combinaciones posibles de monedas y billetes
def calcular_combinaciones(total, BilleMone):
    def buscar_combinaciones(restante, indice):
        if restante == 0:
            return [[]]
        if restante < 0 or indice >= len(BilleMone):
            return []

        Billete_Monedas_actual = BilleMone[indice]
        incluir_actual = buscar_combinaciones(restante - Billete_Monedas_actual, indice)
        excluir_actual = buscar_combinaciones(restante, indice + 1)

        return [[Billete_Monedas_actual] + combinacion for combinacion in incluir_actual] + excluir_actual

    return buscar_combinaciones(total, 0)

def mostrar_combinaciones(lista_combinaciones):
    for i, combinacion in enumerate(lista_combinaciones, 1):
        resumen = {denominacion: combinacion.count(denominacion) for denominacion in set(combinacion)}
        print(f"Combinación {i}:")
        for denominacion, cantidad in resumen.items():
            print(f"{cantidad} monedas de {denominacion} pesos")
        print()

# Ejecución
Billete_Moneda = [50, 20, 10, 5, 1]
cantidadBM = int(input("Ingrese la cantidad: "))

posibles_combinaciones = calcular_combinaciones(cantidadBM, Billete_Moneda)
print(f"Se encontraron {len(posibles_combinaciones)} combinaciones posibles.")
mostrar_combinaciones(posibles_combinaciones)
