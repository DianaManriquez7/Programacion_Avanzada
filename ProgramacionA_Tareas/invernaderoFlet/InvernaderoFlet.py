import psycopg2
import flet as ft
import json
import os


class SensorTemperatura:
    def __init__(self, TemperaturaActual, Tmax, Tmin):
        # Datos que solo son de la clase
        self.TemperaturaActual = TemperaturaActual
        self.Tmax = Tmax
        self.Tmin = Tmin

    def Actualizar_Temp(self, NuevaTemp):  # Metodo
        self.TemperaturaActual = NuevaTemp


class SensorHumedad:
    def __init__(self, HumActual, Valvula, Hmax, Hmin):  # Constructor
        # Riego
        self.HumActual = HumActual
        self.Valvula = Valvula
        self.Hmax = Hmax
        self.Hmin = Hmin

    def Actualizar_Hum(self, NuevaHum):
        self.HumActual = NuevaHum


class SensorLuz:
    def __init__(self, LuzEstado):
        self.LuzEstado = LuzEstado

    def Actualizar_Luz(self, NuevoLuz):
        self.LuzEstado = NuevoLuz


class Invernadero:
    def __init__(self):
        self.SenTemp = SensorTemperatura(0,35,5)  # Temperatura inicial
        self.SenHum = SensorHumedad(0,False,80,10)
        self.SensLuz = SensorLuz(False)
        #self.Valvula(False)

    def ControlInv(self):
        # Para sensor de temperartura
        if self.SenTemp.TemperaturaActual < self.SenTemp.Tmin:
            print("Aumentando temperatura")
            self.SenTemp.Actualizar_Temp(self.SenTemp.TemperaturaActual + 1)

        elif self.SenTemp.TemperaturaActual > self.SenTemp.Tmax:
            print("Disminuyendo temperatura")
            self.SenTemp.Actualizar_Temp(self.SenTemp.TemperaturaActual - 1)

        # Para sensor de Humedad
        if self.SenHum.HumActual < self.SenHum.Hmin:
            print("Activar riego")
            self.SenHum.Actualizar_Hum(self.SenHum.HumActualActualActual + 1)
            self.Valvula = True

        elif self.SenTemp.HumActual > self.SenHum.Hmax:
            print("Desactivando el riego")
            self.SenHum.Actualizar_Hum(self.SenHum.HumActual - 1)
            self.Valvula = False

        # Para Luz
        if self.SenTemp.TemperaturaActual > self.SenTemp.Tmax and self.SensLuz.LuzEstado == False:
            print("Luz Activada")
            self.SensLuz.Actualizacion_Luz(True)

        elif self.SenTemp.TemperaturaActual < self.SenTemp.Tmin and self.SensLuz.LuzEstado == True:
            print("Luz Desactivada")
            self.SensLuz.Actualizacion_Luz(False)



    def obtener_datos(self):
            return {
                "Temperatura": self.SenTemp.TemperaturaActual,
                "Humedad": self.SenHum.HumActual,
                "Luz": self.SensLuz.LuzEstado,
                "Valvula": self.SenHum.Valvula
            }


# Altas,Bajas,Modificaciones,Consultas
class ManejoArchivos:
    def __init__(self, archivo):
        self.archivo = archivo
        # Crear archivo si no existe
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump([], f)

    def alta(self, datoss):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Añadir nuevos datos
        registros.append(datoss)
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
            return json.load(f)



def main(page: ft.Page):
    page.add(ft.Text("Control Invernadero"))
    invernadero = Invernadero()
    archivo = ManejoArchivos("datosTHL.json")

    def mostrar_datos():
        datos = archivo.consultar()
        #lista_datos = ft.Column()
        lista_datos.controls.clear()

        if datos:
            for i, dat in enumerate(datos):
                lista_datos.controls.append(
                    ft.Text(
                        f"Registro {i}: Temperatura={dat['Temperatura']}°C, "
                        f"Humedad={dat['Humedad']}% "
                        f"Luz={'Encendida' if dat['Luz'] else 'Apagada'}"
                    )
                )
            else:
                lista_datos.controls.append(ft.Text("No hay datos guardadas."))
        #limpiar_campos()
        page.update()

    # Función para limpiar campos de texto
    def limpiar_campos():

        Temperatura.value = ""
        Humedad.value = ""
        Luz.value = ""
        indice_baja.value = ""
        indice_modificar.value = ""

    # Funciones de alta, baja y modificación
    def alta_click(e):
        try:
            dat_temperatura = float(Temperatura.value)
            dat_humedad = float(Humedad.value)
            dat_luz = Luz.value.lower() == "encendida"


            invernadero.SenTemp.Actualizar_Temp(dat_temperatura)
            invernadero.SenHum.Actualizar_Hum(dat_humedad)
            invernadero.SensLuz.Actualizar_Luz(dat_luz)

            archivo.alta(invernadero.obtener_datos())
            resultado.value = "Dato guardado exitosamente."
            mostrar_datos()
        except ValueError:
            resultado.value = "Error: Ingrese valores numéricos válidos."
        page.update()



    def baja_click(e):
        try:
            indice = int(indice_baja.value)
            archivo.baja(indice)
            resultado.value = "Dato eliminado exitosamente."
            mostrar_datos()
        except ValueError:
            resultado.value = "Error: Ingrese un índice válido."
        page.update()

    def modificar_click(e):
        try:
            indice = int(indice_modificar.value)
            dat_temperatura = float(Temperatura.value)
            dat_humedad = float(Humedad.value)
            dat_luz = float(Luz.value)

            invernadero.SenTemp.Actualizar_Temp(dat_temperatura)
            invernadero.SenHum.Actualizar_Hum(dat_humedad)
            invernadero.SensLuz.Actualizar_Luz(dat_luz)

            nuevo_dato = {
                "Temperatura": dat_temperatura,
                "Humedad": dat_humedad,
                "Luz": dat_luz,
                "Valvula": False  # Puedes añadir control de la válvula si es necesario
            }
            archivo.modificar(indice, nuevo_dato)

            invernadero.modificar([dat_temperatura, dat_humedad, dat_luz])
            archivo.modificar(indice, invernadero.obtener_datos())
            resultado.value = "Dato modificado exitosamente."
            mostrar_datos()
        except ValueError:
            resultado.value = "Error: Ingrese valores numéricos válidos."
        page.update()

    # Elementos de la interfaz
    Temperatura = ft.TextField(label="Temperatura °C")
    Humedad = ft.TextField(label="Humedad %")
    Luz = ft.TextField(label="Luz (Encendida/Apagada)")

    indice_baja = ft.TextField(label="Índice para eliminar")
    indice_modificar = ft.TextField(label="Índice para modificar")
    resultado = ft.Text()

    # Contenedor con scroll para las posiciones guardadas
    lista_datos = ft.Column(scroll="adaptive")

    # Menú de opciones
    def cambiar_vista(menu_item):
        container_opciones.controls.clear()
        resultado.value = ""
        if menu_item == "Alta":
            container_opciones.controls.extend(
                [Temperatura, Humedad, Luz, ft.ElevatedButton("Guardar datos", on_click=alta_click)]
            )
        elif menu_item == "Baja":
            container_opciones.controls.extend(
                [indice_baja, ft.ElevatedButton("Eliminar Dato", on_click=baja_click)]
            )
        elif menu_item == "Modificación":
            container_opciones.controls.extend(
                [indice_modificar, Temperatura, Humedad, Luz,
                 ft.ElevatedButton("Modificar Dato", on_click=modificar_click)]
            )
        elif menu_item == "Consultas":
            mostrar_datos()
        page.update()

    # Contenedor para los menús y opciones
    container_opciones = ft.Column()
    # Interfaz principal
    page.add(
        ft.Text("Control de Invernadero", style="headlineMedium"),
        ft.Row([ft.ElevatedButton("Guardar Datos", on_click=alta_click),
                ft.ElevatedButton(text="Alta", on_click=lambda e: cambiar_vista("Alta")),
                ft.ElevatedButton(text="Baja", on_click=lambda e: cambiar_vista("Baja")),
                ft.ElevatedButton(text="Modificación", on_click=lambda e: cambiar_vista("Modificación")),
                ft.ElevatedButton(text="Consultas", on_click=lambda e: cambiar_vista("Consultas"))]),
        container_opciones,

        Temperatura,
        Humedad,
        Luz,
        resultado,
        ft.Text("Datos Guardadas:", style="headlineSmall"),
        lista_datos
    )

    # Inicializa con la lista de datos guardados
    mostrar_datos()


##########################################################

'''
    # Menu del invernadero
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
                    temper = float(input("Nueva Temperatura: "))
                    humed = float(input("Nueva Humedad(%): "))
                    luzzz = input("Nuevo estado de la Luz: ")

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
                        print(
                            f"Datos {i}: Temperatura(°C) = {dato['Temperatura']}, Humedad(%) = {dato['Humedad']}, Luz(estado) = {dato['Luz']}")
                else:
                    print("No hay datos guardados.")

            elif opcion == "5":  # Salir
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida. Por favor seleccione una opción del menú.")
'''

ft.app(target=main)

