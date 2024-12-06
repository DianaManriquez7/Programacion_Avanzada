import flet as ft

   def main(page: ft.Page):
       input_temp = ft.TextField(label="Temperatura")
       result_text = ft.Text(size=24)

       def convert_to_fahrenheit(e):
           try:
               celsius = float(input_temp.value)
               fahrenheit = celsius * 9/5 + 32
               result_text.value = f"{celsius}°C = {fahrenheit:.2f}°F"
           except ValueError:
               result_text.value = "Ingresa un valor numérico válido."
           page.update()

       def convert_to_celsius(e):
           try:
               fahrenheit = float(input_temp.value)
               celsius = (fahrenheit - 32) * 5/9
               result_text.value = f"{fahrenheit}°F = {celsius:.2f}°C"
           except ValueError:
               result_text.value = "Ingresa un valor numérico válido."
           page.update()

       page.add(
           input_temp,
           ft.Row([
               ft.ElevatedButton("Convertir a °F", on_click=convert_to_fahrenheit),
               ft.ElevatedButton("Convertir a °C", on_click=convert_to_celsius),
           ]),
           result_text
       )

   ft.app(target=main, view=ft.WEB_BROWSER)