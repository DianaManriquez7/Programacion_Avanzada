# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:06:23 2024

@author: PC
"""

class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2


    def sumar(self):
        self.res_suma= self.numero1+self.numero2
        return self.res_suma

    def multiplicar(self):
        return self.numero1 * self.numero2

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
mi_calculadora = Calculadora(5, 10)
resultado_suma = mi_calculadora.sumar()
resultado_multiplicacion = mi_calculadora.multiplicar()
print(resultado_suma)
print(resultado_multiplicacion)