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
