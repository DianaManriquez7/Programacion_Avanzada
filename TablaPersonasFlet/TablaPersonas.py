
import flet as ft
import psycopg2

# Configuración de conexión a PostgreSQL
def conectar_db():
    return psycopg2.connect(
        dbname="PruebaBase",
        user="postgres",
        password="pollitopiopio7",  # Cambia "tu_password" a la contraseña de tu usuario
        host="localhost"
    )

# Configuración inicial de la tabla
def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
           CREATE TABLE IF NOT EXISTS personas (
               id SERIAL PRIMARY KEY,
               nombre VARCHAR(100) NOT NULL,
               edad INTEGER NOT NULL
           )
       """)
    conn.commit()
    conn.close()

crear_tabla()  # Crea la tabla al iniciar la aplicación

# Función principal de la aplicación en Flet
def main(page: ft.Page):
    # Función para actualizar la lista de personas
    def actualizar_lista():
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personas")
        registros = cursor.fetchall()
        lista_personas.controls.clear()
        for registro in registros:
            lista_personas.controls.append(
                ft.Text(f"ID: {registro[0]}, Nombre: {registro[1]}, Edad: {registro[2]}")
            )
        conn.close()
        page.update()

    # Función para agregar una persona
    def agregar_persona(e):
        nombre = nombre_input.value
        try:
            edad = int(edad_input.value)
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO personas (nombre, edad) VALUES (%s, %s)", (nombre, edad))
            conn.commit()
            conn.close()
            actualizar_lista()
            nombre_input.value = ""
            edad_input.value = ""
            resultado.value = "Persona agregada exitosamente."
        except ValueError:
            resultado.value = "Edad debe ser un número entero."
        page.update()

    # Función para eliminar una persona
    def eliminar_persona(e):
        try:
            persona_id = int(id_input.value)
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM personas WHERE id = %s", (persona_id,))
            conn.commit()
            conn.close()
            actualizar_lista()
            id_input.value = ""
            resultado.value = "Persona eliminada exitosamente."
        except ValueError:
            resultado.value = "ID debe ser un número entero."
        page.update()

    # Función para modificar una persona
    def modificar_persona(e):
        try:
            persona_id = int(id_input.value)
            nuevo_nombre = nombre_input.value
            nueva_edad = int(edad_input.value)
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE personas SET nombre = %s, edad = %s WHERE id = %s",
                           (nuevo_nombre, nueva_edad, persona_id))
            conn.commit()
            conn.close()
            actualizar_lista()
            id_input.value = ""
            nombre_input.value = ""
            edad_input.value = ""
            resultado.value = "Persona modificada exitosamente."
        except ValueError:
            resultado.value = "ID y edad deben ser números enteros."
        page.update()

    # Elementos de la interfaz
    id_input = ft.TextField(label="ID")
    nombre_input = ft.TextField(label="Nombre")
    edad_input = ft.TextField(label="Edad")
    resultado = ft.Text()
    lista_personas = ft.Column()

    # Interfaz de usuario
    page.add(
        ft.Text("Administración de Personas", style="headlineMedium"),
        id_input,
        nombre_input,
        edad_input,
        ft.Row([
            ft.ElevatedButton("Agregar", on_click=agregar_persona),
            ft.ElevatedButton("Eliminar", on_click=eliminar_persona),
            ft.ElevatedButton("Modificar", on_click=modificar_persona),
            ft.ElevatedButton("Consultar", on_click=actualizar_lista),
        ]),
        resultado,
        ft.Text("Lista de Personas:", style="headlineSmall"),
        lista_personas
    )

    # Cargar la lista inicial de personas
    actualizar_lista()

ft.app(target=main)