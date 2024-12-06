import flet as ft
import json
import os


class SensorTemperatura:
    def __init__(self, temperatura_actual, tmax, tmin):
        self.temperatura_actual = temperatura_actual
        self.tmax = tmax
        self.tmin = tmin

    def actualizar_temp(self, nueva_temp):
        self.temperatura_actual = nueva_temp


class SensorHumedad:
    def __init__(self, humedad_actual, valvula, hmax, hmin):
        self.humedad_actual = humedad_actual
        self.valvula = valvula  # True = Encendida, False = Apagada
        self.hmax = hmax
        self.hmin = hmin

    def actualizar_humedad(self, nueva_humedad):
        self.humedad_actual = nueva_humedad


class SensorLuz:
    def __init__(self, luz_estado):
        self.luz_estado = luz_estado  # True = Encendida, False = Apagada

    def actualizar_luz(self, nuevo_estado):
        self.luz_estado = nuevo_estado


class Invernadero:
    def __init__(self):
        self.sen_temp = SensorTemperatura(0, 32, 15)
        self.sen_hum = SensorHumedad(0, False, 80, 20)
        self.sen_luz = SensorLuz(False)

    def control_automatico(self):
        # Control de temperatura
        if self.sen_temp.temperatura_actual < self.sen_temp.tmin:
            print("Aumentando temperatura...")
            self.sen_temp.actualizar_temp(self.sen_temp.temperatura_actual + 1)
        elif self.sen_temp.temperatura_actual > self.sen_temp.tmax:
            print("Disminuyendo temperatura...")
            self.sen_temp.actualizar_temp(self.sen_temp.temperatura_actual - 1)

        # Control de humedad
        if self.sen_hum.humedad_actual < self.sen_hum.hmin:
            print("Activando riego...")
            self.sen_hum.valvula = True
            self.sen_hum.actualizar_humedad(self.sen_hum.humedad_actual + 1)
        elif self.sen_hum.humedad_actual > self.sen_hum.hmax:
            print("Desactivando riego...")
            self.sen_hum.valvula = False
            self.sen_hum.actualizar_humedad(self.sen_hum.humedad_actual - 1)

        # Control de luz
        if not self.sen_luz.luz_estado and self.sen_temp.temperatura_actual < self.sen_temp.tmin:
            print("Encendiendo luz...")
            self.sen_luz.actualizar_luz(True)
        elif self.sen_luz.luz_estado and self.sen_temp.temperatura_actual > self.sen_temp.tmax:
            print("Apagando luz...")
            self.sen_luz.actualizar_luz(False)

    def obtener_datos(self):
        return {
            "Temperatura": self.sen_temp.temperatura_actual,
            "Humedad": self.sen_hum.humedad_actual,
            "Valvula": self.sen_hum.valvula,
            "Luz": self.sen_luz.luz_estado
        }


class ManejoArchivos:
    def __init__(self, archivo):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump([], f)

    def alta(self, datos):
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        registros.append(datos)
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def baja(self, indice):
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        if 0 <= indice < len(registros):
            registros.pop(indice)
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def modificar(self, indice, nuevos_datos):
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        if 0 <= indice < len(registros):
            registros[indice] = nuevos_datos
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def consultar(self):
        with open(self.archivo, 'r') as f:
            return json.load(f)


def main(page: ft.Page):
    invernadero = Invernadero()
    archivo = ManejoArchivos("invernadero.json")

    def mostrar_datos():
        datos = archivo.consultar()
        lista_datos.controls.clear()
        if datos:
            for i, dat in enumerate(datos):
                lista_datos.controls.append(
                    ft.Text(
                        f"Registro {i}: Temperatura={dat['Temperatura']}°C, "
                        f"Humedad={dat['Humedad']}%, Valvula={'Encendida' if dat['Valvula'] else 'Apagada'}, "
                        f"Luz={'Encendida' if dat['Luz'] else 'Apagada'}"
                    )
                )
        else:
            lista_datos.controls.append(ft.Text("No hay datos guardados."))
        page.update()

    def limpiar_campos():
        temperatura.value = ""
        humedad.value = ""
        luz.value = ""

    def alta_click(e):
        try:
            temp = float(temperatura.value)
            hum = float(humedad.value)
            luz_estado = luz.value.lower() == "encendida"
            invernadero.sen_temp.actualizar_temp(temp)
            invernadero.sen_hum.actualizar_humedad(hum)
            invernadero.sen_luz.actualizar_luz(luz_estado)
            archivo.alta(invernadero.obtener_datos())
            resultado.value = "Datos guardados correctamente."
            mostrar_datos()
        except ValueError:
            resultado.value = "Error: Ingrese valores válidos."
        page.update()

    temperatura = ft.TextField(label="Temperatura (°C)")
    humedad = ft.TextField(label="Humedad (%)")
    luz = ft.TextField(label="Luz (Encendida/Apagada)")

    resultado = ft.Text()
    lista_datos = ft.Column(scroll="adaptive")

    page.add(
        ft.Text("Control del Invernadero", style="headlineMedium"),
        ft.Row([
            ft.ElevatedButton("Guardar Datos", on_click=alta_click)
        ]),
        temperatura,
        humedad,
        luz,
        resultado,
        ft.Text("Registros Guardados:", style="headlineSmall"),
        lista_datos
    )

    mostrar_datos()


ft.app(target=main)
