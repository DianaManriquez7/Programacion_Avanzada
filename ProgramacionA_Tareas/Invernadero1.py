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
    def __init__ (self, TemperaturaActual, Tmax, Tmin):
    #Datos que solo son de la clase
       self.TemperaturaActual = TemperaturaActual
       self.Tmax = Tmax
       self.Tmin = Tmin
       
    def Actualizar_Temp(self, NuevaTemp):  #Metodo
        self.TemperaturaActual = NuevaTemp
            


class SensorHumedad:
    def __init__ (self, HumActual, Valvula, Hmax, Hmin): #Constructor
    #Riego
        self.HumActual = HumActual
        self.Valvula = Valvula
        self.Hmax = Hmax
        self.Hmin = Hmin
        
    def Actualizacion_Hum(self, NuevaHum):
        self.HumActual=NuevaHum
            
class SensorLuz:
    def __init__ (self, LuzEstado):
        self.LuzEstado = LuzEstado
        
    def Actualizacion_Luz(self, NuevoLuz):
        self.LuzEstado=NuevoLuz
        
            
class Invernadero:
    def __init__(self):
        self.SenTemp=SensorTemperatura(16)#Temperatura inicial
        self.SenHum=SensorHumedad(30)
        self.SensLuz=SensorLuz(False)
        self.Valvula(False)
        
    def ControlInv(self):
        #Para sensor de temperartura
        if self.SenTemp.TemperaturaActual < self.SenTemp.Tmin:
            print("Subiendo temperatura")
            self.SenTemp.Actualizar_Temp(self.SenTemp.TemperaturaActual + 1)

        elif self.SenTemp.TemperaturaActual > self.SenTemp.Tmax:
            print("Disminuyendo temperatura")
            self.SenTemp.Actualizar_Temp(self.SenTemp.TemperaturaActual - 1)
        
        #Para sensor de Humedad
        if self.SenHum.HumActual < self.SenHum.Hmin:
            print("Activar riego")
            self.SenHum.Actualizar_Hum(self.SenHum.HumActualActualActual + 1)
            self.Valvula=True

        elif self.SenTemp.HumActual > self.SenHum.Hmax:
            print("Desactivando el riego")
            self.SenHum.Actualizar_Hum(self.SenHum.HumActual - 1)
            self.Valvula=False
        
        #Para Luz
        if self.SenTemp.TemperaturaActual > self.SenTemp.Tmax and self.SensLuz.LuzEstado==False:
            print("Luz Activada")
            self.SensLuz==True
            
        elif self.SenTemp.TemperaturaActual < self.SenTemp.Tmin and self.SensLuz.LuzEstado==True:
            print("Luz Desactivada")
            self.SensLuz==False
       
        return{  
        "Temperatura":self.SenTemp.TemperaturaActual,
        "Humedad":self.SenHum.HumActual,
        "Luz":self.SensLuz.LuzEstado
        }
#Altas,Bajas,Modificaciones,Consultas
class ManejoArchivos:
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

#Menu del invernadero
def mostrar_menu():
    print("\nMenú del Invernader:")
    print("1. Alta (Guardar nuevos datos)")
    print("2. Baja (Eliminar un dato por índice)")
    print("3. Modificación (Modificar un dato por índice)")
    print("4. Consultas (Mostrar todos los datos guardados)")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    Invernadero_1 = Invernadero()
    archivo = ManejoArchivos("Dato.json")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":  # Alta
            # Captura nuevas posiciones de las articulaciones
            try:
                Temper = float(input("Temperatura: "))
                Humed = float(input("Humedad (%): "))
                Luzzz = input("Estado de la Luz: ")
                
                Invernadero_1.SenTemp.Actualizar_Temp(Temper)
                Invernadero_1.SenHum.Actualizar_Hum(Humed)
                Invernadero_1.SensLuz.Actualizar_Luz(Luzzz)
                
                archivo.alta(Invernadero())
                print("Datos guardados exitosamente.")
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        elif opcion == "2":  # Baja
            try:
                indice = int(input("Ingrese el índice de la posición que desea eliminar: "))
                archivo.baja(indice)
                print("Dato eliminado exitosamente.")
            except ValueError:
                print("Error: Ingrese un índice válido.")
            except IndexError:
                print("Error: Índice fuera de rango.")

        elif opcion == "3":  # Modificación
            try:
                indice = int(input("Ingrese el índice de la posición que desea modificar: "))
                temper=float(input("Nueva Temperatura: "))
                humed=float(input("Nueva Humedad(%): "))
                luzzz=input("Nuevo estado de la Luz: ")
                
                Invernadero_1.SenTemp.Actualizar_Temp(temper)
                Invernadero_1.SenHum.Actualizar_Hum(humed)
                Invernadero_1.SensLuz.Actualizar_Luz(luzzz)
                print("Datos modificados exitosamente.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            except IndexError:
                print("Error: Índice fuera de rango.")

        elif opcion == "4":  # Consultas
            Datos = archivo.consultar()
            if Datos:
                for i, dato in enumerate(Datos):
                    print(f"Datos {i}: Temperatura(°C) = {dato['Temperatura']}, Humedad(%) = {dato['Humedad']}, Luz(estado)={dato['Luz']})
            else:
                print("No hay datos guardados.")

        elif opcion == "5":  # Salir
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción del menú.")







