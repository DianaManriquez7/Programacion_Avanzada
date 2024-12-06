import flet as ft
import ft
import page
import asyncio
import random

from flet_core import page


# Función principal que define la interfaz de la app
def main(page: ft.Page):
    # Título de la ventana
    page.title = "Game Flet"



    texto = ft.Text(
        "Presiona la letra...\n"
        "A: para que sea automatico\n" 
        "M: para que sea manual\n"
        "P: para pausar el juego\n"
        "Q: para quitar el juego",
        size=24,
        color="blue",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.LEFT
    )
    # Agregar el widget de texto a la página
    page.add(texto)


    # Campo de texto donde el usuario puede escribir
    text_field = ft.TextField(label="Escribe la letra")

    # Label para mostrar el resultado
    result = ft.Text(value="")

    # Función que se ejecuta al hacer clic en el botón
    def button_clicked(e):
        result.value = f"Has escrito: {text_field.value}"  # Actualizar el texto
        page.update()  # Actualizar la página para mostrar los cambios

    # Botón que ejecuta la función cuando se hace clic
    button = ft.ElevatedButton(text="Mostrar texto", on_click=button_clicked)

    # Añadir los elementos a la página
    page.add(text_field, button, result)


# Colores y variables de juego
BLANCO = ft.colors.WHITE
NEGRO = ft.colors.BLACK
ANCHO, ALTO = 800, 400



# Variables del jugador, bala, nave, fondo, etc.
jugador = None
bala = None
bala2 = None
fondo = None
nave = None
menu = None

# Variables de salto
salto = False
salto_altura = 15  # Velocidad inicial de salto
gravedad = 1
en_suelo = True

################################
# Variables de desplazamiento
izquierda = True
derecha = False
desplazamiento_vel = 10
################################

# Variables de pausa y menú
pausa = False
#fuente = pygame.font.SysFont('Arial', 24)
menu_activo = True
modo_auto = False  # Indica si el modo de juego es automático

# Lista para guardar los datos de velocidad, distancia y salto (target)
datos_modelo = []

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Cargar las imágenes
jugador_frames = [
    ft.image.load('assets/sprites/mono_frame_1.png',width=32, height=48, left=50,top=ALTO-100),
    ft.image.load('assets/sprites/mono_frame_2.png',width=32, height=48, left=50,top=ALTO-100),
    ft.image.load('assets/sprites/mono_frame_3.png',width=32, height=48, left=50,top=ALTO-100),
    ft.image.load('assets/sprites/mono_frame_4.png',width=32, height=48, left=50,top=ALTO-100)
]

# Variables para la animación del jugador
current_frame = 0
frame_speed = 10  # Cuántos frames antes de cambiar a la siguiente imagen
frame_count = 0

jugador_img=jugador_frames[current_frame]
page.add(jugador_img)

def animar_jugador():
    global current_frame, frame_count
    frame_count += 1
    if frame_count >= frame_speed:
        current_frame = (current_frame + 1) % len(jugador_frames)
        frame_count = 0
        jugador_img.src = jugador_frames[current_frame].src  # Cambia la imagen actual
        page.update()

bala_img = ft.image.load('assets/sprites/purple_ball.png',
     left=ANCHO - 50,
     top=ALTO - 90,
     width=16,
     height=16)
bala2_img = ft.image.load('assets/sprites/purple_ball.png',
    left=ANCHO - 750,
    top=ALTO - 400,
    width=16,
    height=16)

nave_img = ft.image.load('assets/game/ufo.png',
    left=ANCHO - 100,
    top=ALTO - 100,
    width=64,
    height=64)
page.add(nave_img)

# Crear el rectángulo del menú (como una imagen de fondo o contenedor)
menu_rect = ft.Container(
    width=270,
    height=180,
    left=ANCHO // 2 - 135,
    top=ALTO // 2 - 90,
    bgcolor=ft.colors.BLACK,
    border_radius=10)

# Agregar todos los elementos a la página
def main(page: ft.Page):
    page.add(jugador, bala, bala2, nave, menu_rect)

ft.app(target=main)

# Variables para la bala
velocidad_bala = -10  # Velocidad de la bala hacia la izquierda
bala_disparada = False

# Variables para la bala2
velocidad_bala2 = -10  # Velocidad de la bala hacia la izquierda
bala2_disparada = False

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Variables para el fondo en movimiento
fondo_x1 = 0
fondo_x2 = ANCHO

# Agrega estas imágenes de fondo al inicio
fondo1 = ft.Image(src="assets/game/fondo2.png", left=fondo_x1, top=0, width=ANCHO, height=ALTO)
fondo2 = ft.Image(src="assets/game/fondo2.png", left=fondo_x2, top=0, width=ANCHO, height=ALTO)
page.add(fondo1, fondo2)

def mover_fondos():
    global fondo_x1, fondo_x2
    fondo_x1 -= 1
    fondo_x2 -= 1

    # Si una de las imágenes se sale de la pantalla, reiniciar posición
    if fondo_x1 <= -ANCHO:
        fondo_x1 = ANCHO
    if fondo_x2 <= -ANCHO:
        fondo_x2 = ANCHO

    # Actualizar posición de las imágenes en la pantalla
    fondo1.left = fondo_x1
    fondo2.left = fondo_x2
    page.update()



# Función para disparar la bala
def disparar_bala():
    global bala_disparada, velocidad_bala
    if bala_disparada:
        bala_img.left += velocidad_bala
        #para reiniciar la posición de la bala
        if bala_img.left < 0:  # Si la bala sale de la pantalla, reiniciar posición
            bala_img.left = ANCHO - 50
            bala_disparada = False
        page.update()



#############################
# Función para disparar la bala2
def disparar_bala2():
    global bala2_disparada, velocidad_bala2
    if bala2_disparada:
        bala2_img.left += velocidad_bala2
        # para reiniciar la posición de la bala
        if bala2_img.left < 0:  # Si la bala sale de la pantalla, reiniciar posición
            bala2_img.left = ANCHO - 750
            bala2_disparada = False
        page.update()



# Función para manejar el salto
def manejar_salto():
    global jugador, salto, salto_altura, gravedad, en_suelo

    if salto:
        jugador.y -= salto_altura  # Mover al jugador hacia arriba
        salto_altura -= gravedad  # Aplicar gravedad (reduce la velocidad del salto)

        # Si el jugador llega al suelo, detener el salto
        if jugador.y >= ALTO - 100:
            jugador.y = ALTO - 100
            salto = False
            salto_altura = 15  # Restablecer la velocidad de salto
            en_suelo = True


#######################################
# Funcion para dezplazamiento
def manejar_desplazamiento():
    global jugador, derecha, izquierda, derecha, desplazamiento_vel

    if izquierda:
        jugador.x -= desplazamiento_vel
    if jugador.x <= 50:
        jugador.x = 50

    if derecha:
        jugador.x += desplazamiento_vel
    if jugador.x >= 100:
        jugador.x = 100


###################################


# Función para actualizar el juego
def update():
    global bala, bala2, velocidad_bala, velocidad_bala2, current_frame, frame_count, fondo_x1, fondo_x2

    # Mover el fondo
    fondo_x1 -= 1
    fondo_x2 -= 1

    # Si el primer fondo sale de la pantalla, lo movemos detrás del segundo
    if fondo_x1 <= -ANCHO:
        fondo_x1 = ANCHO

    # Si el segundo fondo sale de la pantalla, lo movemos detrás del primero
    if fondo_x2 <= -ANCHO:
        fondo_x2 = ANCHO

    # Dibujar los fondos
    pantalla.blit(fondo_img, (fondo_x1, 0))
    pantalla.blit(fondo_img, (fondo_x2, 0))

    # Animación del jugador
    def animar_jugador():
        global current_frame, frame_count
        frame_count += 1
        if frame_count >= frame_speed:
            current_frame = (current_frame + 1) % len(jugador_frames)
            frame_count = 0
            jugador_img.src = jugador_frames[current_frame].src  # Cambia la imagen actual
            page.update()

    def verificar_colision(jugador_img, bala_img):
        jugador_rect = (jugador_img.left, jugador_img.top, jugador_img.width, jugador_img.height)
        bala_rect = (bala_img.left, bala_img.top, bala_img.width, bala_img.height)

        # Verificar si los rectángulos se superponen
        return not (
                jugador_rect[0] > bala_rect[0] + bala_rect[2] or
                jugador_rect[0] + jugador_rect[2] < bala_rect[0] or
                jugador_rect[1] > bala_rect[1] + bala_rect[3] or
                jugador_rect[1] + jugador_rect[3] < bala_rect[1]
        )

    def detectar_colision():
        if verificar_colision(jugador_img, bala_img):
            print("Colisión detectada!")
            reiniciar_juego()  # O cualquier otra acción tras la colisión


################################
# Función para guardar datos del modelo en modo manual
def guardar_datos():
    global jugador, bala, bala2, velocidad_bala, velocidad_bala2, salto
    distancia = abs(jugador.x - bala.x)
    distancia2 = abs(jugador.x - bala2.y)
    salto_hecho = 1 if salto else 0  # 1 si saltó, 0 si no saltó
    # Guardar velocidad de la bala, distancia al jugador y si saltó o no
    datos_modelo.append((velocidad_bala, velocidad_bala2, distancia, distancia2, salto_hecho))


# Función para pausar el juego y guardar los datos
def pausa_juego():
    global pausa
    pausa = not pausa
    if pausa:
        print("Juego pausado. Datos registrados hasta ahora:", datos_modelo)
    else:
        print("Juego reanudado.")


# Función para mostrar el menú y seleccionar el modo de juego
def mostrar_menu():
    global menu_activo, modo_auto
    pantalla.fill(NEGRO)
    texto = fuente.render("Presiona 'A' para Auto, 'M' para Manual, o 'Q' para Salir", True, BLANCO)
    pantalla.blit(texto, (w // 4, h // 2))
    pygame.display.flip()

    while menu_activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    modo_auto = True
                    menu_activo = False
                elif evento.key == pygame.K_m:
                    modo_auto = False
                    menu_activo = False
                elif evento.key == pygame.K_q:
                    print("Juego terminado. Datos recopilados:", datos_modelo)
                    pygame.quit()
                    exit()


# Función para reiniciar el juego tras la colisión
def reiniciar_juego():
    global menu_activo, jugador, bala, bala2, nave, bala_disparada, bala2_disparada, salto, en_suelo
    menu_activo = True  # Activar de nuevo el menú
    jugador.x, jugador.y = 50, ALTO - 100  # Reiniciar posición del jugador
    bala.x = ANCHO - 50  # Reiniciar posición de la bala
    bala2.y = ANCHO - 750
    nave.x, nave.y = w - 100, h - 100  # Reiniciar posición de la nave

    bala_disparada = False
    bala2_disparada = False
    salto = False
    en_suelo = True

    # Mostrar los datos recopilados hasta el momento
    print("Datos recopilados para el modelo: ", datos_modelo)
    mostrar_menu()  # Mostrar el menú de nuevo para seleccionar modo


async def main(page: ft.Page):
    page.window_width = ANCHO
    page.window_height = ALTO
    page.bgcolor = NEGRO



def main():
    global salto, en_suelo, bala_disparada, bala2_disparada, izquierda, derecha

    reloj = pygame.time.Clock()
    mostrar_menu()  # Mostrar el menú al inicio
    correr = True

    while correr:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                correr = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and en_suelo and not pausa:  # Detectar la tecla espacio para saltar
                    salto = True
                    en_suelo = False

                if evento.key == pygame.K_p:  # Presiona 'p' para pausar el juego
                    pausa_juego()
                if evento.key == pygame.K_q:  # Presiona 'q' para terminar el juego
                    print("Juego terminado. Datos recopilados:", datos_modelo)
                    pygame.quit()
                    exit()
                # Detectar teclas izquierda y derecha para comenzar a mover el jugador
                if evento.key == pygame.K_LEFT:
                    izquierda = True
                if evento.key == pygame.K_RIGHT:
                    derecha = True

                # Detectar cuando se sueltan las teclas izquierda y derecha
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    izquierda = False
                if evento.key == pygame.K_RIGHT:
                    derecha = False

            #######################################################
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    izquierda = False

                if evento.key == pygame.K_RIGHT:
                    derecha = False
        ########################################################

        if not pausa:
            # Modo manual: el jugador controla el salto
            if not modo_auto:
                if salto:
                    manejar_salto()
                # Guardar los datos si estamos en modo manual
                guardar_datos()

            manejar_desplazamiento()

            # Actualizar el juego
            if not bala_disparada:
                disparar_bala()
            update()

            #######################################
            # Actualizar el juego
            if not bala2_disparada:
                disparar_bala2()
            update()

            # Actualizar la pantalla
        pygame.display.flip()
        reloj.tick(30)  # Limitar el juego a 30 FPS

    pygame.quit()


if __name__ == "__main__":
    main()

# Ejecutar la app
ft.app(target=main)