"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

# importa herramientas para mezclar los números y trabajar con los dibujos
from random import *
from turtle import *

# importa la función que permite encontrar archivos del juego
from freegames import path

# carga la imagen del carro que aparece detrás de las tarjetas
car = path('car.gif')

# MODIFICACIÓN:
# Se reemplazan los números por símbolos visuales
# para facilitar la memorización de las parejas.

tiles = [
    '🍎','🍌','🍇','🍉',
    '🍒','🍓','🥝','🍍',
    '🐶','🐱','🐭','🐹',
    '🦊','🐻','🐼','🐨',
    '⚽','🏀','🏈','🎾',
    '🎲','🎯','🎸','🎹',
    '🚗','🚙','🚲','✈️',
    '🚀','⛵','🚁','🚂'
] * 2

# guarda la tarjeta que se seleccionó primero
state = {'mark': None}

# indica que todas las tarjetas empiezan ocultas
hide = [True] * 64

# guarda la cantidad de veces que el jugador ha hecho clic
taps = 0


def square(x, y):
    # dibuja un cuadro blanco con borde negro en la posición indicada
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()

    # repite cuatro veces para formar los lados del cuadro
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    # convierte las coordenadas de la pantalla en la posición de una tarjeta
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    # convierte el número de una tarjeta en sus coordenadas dentro del tablero
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    # permite contar los clics desde cualquier parte del juego
    global taps

    # suma uno cada vez que el jugador hace clic
    taps += 1

    # actualiza el número de taps en la ventana del juego
    title('Memory - Taps: ' + str(taps))

    # si todas las tarjetas ya fueron descubiertas, no permite seguir jugando
    if all(not hidden for hidden in hide):
        return

    # actualiza las tarjetas cuando el jugador hace clic
    """Update mark and hidden tiles based on tap."""

    # identifica qué tarjeta seleccionó el jugador
    spot = index(x, y)

    # obtiene la tarjeta que se había seleccionado anteriormente
    mark = state['mark']

    # si no hay una tarjeta seleccionada, si se repite la misma o si no coinciden los números, guarda la nueva selección
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot

    # si los números coinciden, deja visibles las dos tarjetas
    else:
        hide[spot] = False
        hide[mark] = False

        # limpia la selección para poder buscar otra pareja
        state['mark'] = None


def draw():
    # se encarga de dibujar y actualizar todo lo que aparece en el juego
    """Draw image and tiles."""
    clear()
    goto(0, 0)

    # muestra la imagen del carro en el centro del tablero
    shape(car)
    stamp()

    # recorre las 64 tarjetas para revisar cuáles siguen ocultas
    for count in range(64):

        # si la tarjeta está oculta, dibuja su cuadro blanco
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # obtiene la tarjeta que está seleccionada actualmente
    mark = state['mark']

    # si hay una tarjeta seleccionada y todavía está oculta, muestra su número
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
# MODIFICACION:
# Se centra el contenido de la tarjeta para mejorar
# la presentacion visual del juego.

goto(x + 25, y + 10)
color('black')

write(
    tiles[mark],
    align='center',
    #Cambio
    font=('Arial', 20, 'normal')
)

    # revisa si todas las tarjetas ya fueron descubiertas
if all(not hidden for hidden in hide):
        up()
        goto(-85, 0)
        color('green')

        # muestra un mensaje cuando el jugador encuentra todas las parejas
        write('ganaste!', font=('Arial', 24, 'bold'))

        # muestra el total de clics que necesitó el jugador
        goto(-85, -30)
        write('taps: ' + str(taps), font=('Arial', 16, 'normal'))

    # actualiza la pantalla para mostrar los cambios
    update()

    # vuelve a ejecutar draw después de 100 milisegundos
    ontimer(draw, 100)


# mezcla los números para que las parejas aparezcan en diferentes lugares
shuffle(tiles)

# configura el tamaño y la posición de la ventana del juego
setup(420, 420, 370, 0)

# agrega la imagen del carro para poder utilizarla en el juego
addshape(car)

# oculta la tortuga que se utiliza para dibujar
hideturtle()

# desactiva las actualizaciones automáticas para controlar cuándo se dibuja
tracer(False)

# permite que el jugador seleccione las tarjetas haciendo clic
onscreenclick(tap)

# inicia el dibujo y la actualización del juego
draw()

# mantiene abierta la ventana hasta que se cierre el juego
done()
