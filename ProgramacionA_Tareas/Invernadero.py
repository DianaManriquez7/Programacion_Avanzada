# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:56:55 2024

@author: Diana Manríquez
"""
'''
 Temperatura=input('Introduce un valor de temperatura: ')
 if Temperatura > 30:
     print('Se va a cocer tu plantaaaaa')
 elif Temperatura < 5:
     print('Pobre la va a dar hipotermia')
     
 Humedad=input('Introduce un valor para la humedad: ')
 if Humedad > 30:
     print('Se va a cocer tu plantaaaaa')
 elif Humedad < 5:
     print('Pobre la va a dar hipotermia')
     
 Luz=input('Introduce un porsentaje de Luz: ')
 if Luz > 30:
     print('Se va a cocer tu plantaaaaa')
 elif Luz < 5:
     print('Pobre la va a dar hipotermia')

class Invernadero:
    def init (self, Temperatura, Humedad, Luz ):
        self.Temperatura = Temperatura
        self.Humedad = Humedad
        self.Luz = Luz
'''
import json
import os


class SensorTemperatura:
    def __init__ (self, TempControl, TemperaturaActual, Tmax, Tmin):
       self.TempControl = TempControl  #Datos que solo son de la clase
       self.TemperaturaActual = TemperaturaActual
       self.Tmax = Tmax
       self.Tmin = Tmin
       
    def Temp(self):  #Metodo
        if self.TemperaturaActual > self.Tmax:
            self.TemperaturaActual -= self.TempControl
        elif self.TemperaturaActual < self.Tmin:
            self.TemperaturaActual += self.TempControl
            
        return self.TemperaturaActual
    def obtener_temperatura(self):
        # Retorna las posiciones actuales de las articulaciones
        return {
            "TempeActual": self.TempeActual
        }


class SensorHumedad:
    def __init__ (self, HumControl, HumActual, Valvula, Hmax, Hmin): #Constructor
        self.HumControl = HumControl   #Riego
        self.HumActual = HumActual
        self.Valvula = Valvula
        self.Hmax = Hmax
        self.Hmin = Hmin
    def Hum(self):
        if self.HumActual > self.Hmax:
            self.HumActual -= self.HumControl
            self.Valvula = False
        elif self.HumActual < self.Hmin:
            self.HumActual += self.HumControl
            self.Valvula = True
            
class SensorLuz:
    def __init__ (self, LuzControl, LuzActual, venti, Lmax, Lmin):
        self.LuzControl = LuzControl
        self.LuzActual = LuzActual
        self.venti = venti
        self.Lmax = Lmax
        self.Lmin = Lmin
    def Luzz(self):
        if self.LuzActual > self.Lmax:
            self.LuzActual -= self.LuzControl
            self.venti = True
        elif self.LuzActual < self.Lmin:
            self.LuzActual += self.LuzControl
            self.venti = False
            
#Para temperatura
SensorT= SensorTemperatura(1,10,30,15) #Objeto
Temperatura=SensorT.Temp()   #Metodo con el objeto
print(Temperatura)

#Para humedad
SensorH= SensorHumedad(1,10,100,0) #Objeto
Humedad=SensorH.Hum()   #Metodo con el objeto
print(Humedad)

#Para Luz
SensorL= SensorLuz(1,10,30,15) #Objeto
Luz=SensorL.Luzz()   #Metodo con el objeto
print(Humedad)


class ManejoArchivo:
               
    def __init__(self, archivo):
        self.archivo = archivo
        # Crear archivo si no existe
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump([], f)

    def alta(self, datos):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Añadir nuevos datos
        registros.append(datos)
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def baja(self, indice):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Eliminar por índice
        if 0 <= indice < len(registros):
            registros.pop(indice)
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def modificar(self, indice, nuevos_datos):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Modificar el registro por índice
        if 0 <= indice < len(registros):
            registros[indice] = nuevos_datos
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def consultar(self):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        return registros

def mostrar_menu():
    print("\n Menú Invernadero:")
    print("1. Alta (Guardar nueva posición)")
    print("2. Baja (Eliminar una posición por índice)")
    print("3. Modificación (Modificar una posición por índice)")
    print("4. Consultas (Mostrar todas las posiciones guardadas)")
    print("5. Salir")
    return input("Seleccione una opción: ")


def main():
    Temperatura=SensorT.Temp()
    archivo = ManejoArchivo("Temperatura.json")
    

    while True:
        opcion = mostrar_menu()

        if opcion == "1":  # Alta
            # Captura nuevas posiciones de las articulaciones
            try:
                TempActual = float(input("Temperatura Actual: "))
                SensorTemperatura.Temp([TempActual])
                archivo.alta(Temperatura.Temp())
                print("Teperatura Actual guardada.")
                
                HumeActual = float(input("Temperatura Actual: "))
                SensorHumedad.Hum([HumeActual])
                archivo.alta(Humedad.Hum())
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        elif opcion == "2":  # Baja
            try:
                indice = int(input("Ingrese el índice de la posición que desea eliminar: "))
                archivo.baja(indice)
                print("Posición eliminada exitosamente.")
            except ValueError:
                print("Error: Ingrese un índice válido.")
            except IndexError:
                print("Error: Índice fuera de rango.")

        elif opcion == "3":  # Modificación
            try:
                indice = int(input("Ingrese el índice de la posición que desea modificar: "))
                pos_hombro = float(input("Nuevo ángulo del hombro: "))
                pos_codo = float(input("Nuevo ángulo del codo: "))
                pos_muneca = float(input("Nuevo ángulo de la muñeca: "))
                pos_pinza = float(input("Nuevo ángulo de la pinza: "))
                brazo.mover_a_posicion([pos_hombro, pos_codo, pos_muneca, pos_pinza])
                archivo.modificar(indice, brazo.obtener_posiciones())
                print("Posición modificada exitosamente.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            except IndexError:
                print("Error: Índice fuera de rango.")

        elif opcion == "4":  # Consultas
            posiciones = archivo.consultar()
            if posiciones:
                for i, pos in enumerate(posiciones):
                    print(f"Posición {i}: Hombro={pos['hombro']}, Codo={pos['codo']}, Muñeca={pos['muneca']}, Pinza={pos['pinza']}")
            else:
                print("No hay posiciones guardadas.")

        elif opcion == "5":  # Salir
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción del menú.")
