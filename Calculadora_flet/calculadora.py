import flet as ft

def main(page: ft.Page):
    # Variables para almacenar los valores y la operación
    current_input = ""
    operator = ""
    first_number = None
    result_text = ft.Text(value="0", size=32)  # Pantalla de la calculadora

    # Función para actualizar la pantalla de la calculadora
    def update_display(value):
        result_text.value = value
        page.update()

    # Función que se llama cuando se presiona un número o un punto decimal
    def number_click(e):
        nonlocal current_input
        current_input += e.control.data
        update_display(current_input)

    # Función que se llama cuando se selecciona una operación (+, -, *, /)
    def operator_click(e):
        nonlocal current_input, operator, first_number
        if current_input:
            first_number = float(current_input)
            operator = e.control.data
            current_input = ""
            update_display(operator)

    # Función que se llama cuando se presiona "=" para obtener el resultado
    def calculate(e):
        nonlocal current_input, operator, first_number
        if first_number is not None and current_input:
            second_number = float(current_input)
            result = None
            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                if second_number != 0:
                    result = first_number / second_number
                else:
                    result = "Error"
            update_display(str(result))
            # Resetear los valores
            first_number = result if isinstance(result, (int, float)) else None
            current_input = ""

    # Función para el botón de "Clear" que resetea la calculadora
    def clear(e):
        nonlocal current_input, operator, first_number
        current_input = ""
        operator = ""
        first_number = None
        update_display("0")

    # Layout de la calculadora
    page.add(result_text)  # Pantalla de la calculadora

    # Filas de botones
    botones = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    for fila in botones:
        row = ft.Row()
        for boton in fila:
            if boton.isdigit() or boton == ".":
                button = ft.ElevatedButton(text=boton, data=boton, on_click=number_click, width=80, height=80)
            elif boton in ["+", "-", "*", "/"]:
                button = ft.ElevatedButton(text=boton, data=boton, on_click=operator_click, width=80, height=80)
            elif boton == "=":
                button = ft.ElevatedButton(text=boton, on_click=calculate, width=80, height=80)
            row.controls.append(button)
        page.add(row)

    # Botón de limpiar
    page.add(ft.ElevatedButton(text="Clear", on_click=clear, width=320, height=80))

ft.app(target=main)