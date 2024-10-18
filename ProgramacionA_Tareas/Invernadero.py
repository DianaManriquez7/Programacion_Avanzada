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
class SensorTemperatura:
    def init (self, TempControl, TemperaturaActual, Tmax, Tmin):
       self.TemperaturaControl = TempControl
       self.TemperaturaActual = TemperaturaActual
       self.Tmax = Tmax
       self.Tmin = Tmin
       
    def Temp(self):
        if self.TemperaturaActual > self.Tmax:
            self.TemperaturaActual -= self.TempControl
        elif self.Temperatura < self.Tmin:
            self.TemperaturaActual += self.TempControl

class SensorHumedad:
    def init (self, HumControl, HumActual, Valvula, Hmax, Hmin):
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
    def init (self, LuzControl, LuzActual, venti, Lmax, Lmin):
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