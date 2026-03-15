"""
player.py — Gestión de elecciones del jugador y la computadora.
Maneja toda la entrada de usuario y la generación aleatoria para la IA.
"""

import random
from src.config import OPCIONES, EMOJIS, MIN_RONDAS, MAX_RONDAS


def obtener_eleccion_jugador() -> str:
    """Muestra el menú y devuelve la elección del jugador como string.

    Valida que la entrada sea un número entre 1 y 5.
    Repite la pregunta hasta recibir una entrada válida.

    Returns:
        Nombre de la elección (ej. "Piedra").
    """
    print("\nElige tu jugada:")
    for numero, nombre in OPCIONES.items():
        print(f"  {numero}. {EMOJIS[nombre]} {nombre}")

    while True:
        try:
            eleccion = int(input("\nTu elección (1-5): "))
            if eleccion in OPCIONES:
                return OPCIONES[eleccion]
            print("❌ Opción no válida. Introduce un número del 1 al 5.")
        except ValueError:
            print("❌ Entrada inválida. Debes introducir un número.")


def obtener_eleccion_computadora() -> str:
    """Genera y devuelve una elección aleatoria para la computadora.

    Returns:
        Nombre de la elección (ej. "Spock").
    """
    return random.choice(list(OPCIONES.values()))


def pedir_numero_rondas() -> int:
    """Solicita al jugador cuántas rondas quiere jugar.

    Valida que sea un entero entre MIN_RONDAS y MAX_RONDAS.

    Returns:
        Número de rondas como entero positivo.
    """
    while True:
        try:
            rondas = int(input(f"\n¿Cuántas rondas quieres jugar? ({MIN_RONDAS}-{MAX_RONDAS}): "))
            if MIN_RONDAS <= rondas <= MAX_RONDAS:
                return rondas
            print(f"❌ Introduce un número entre {MIN_RONDAS} y {MAX_RONDAS}.")
        except ValueError:
            print("❌ Entrada inválida. Debes introducir un número.")


def pedir_opcion_menu(opciones_validas: list) -> int:
    """Solicita al jugador una opción del menú principal.

    Args:
        opciones_validas: Lista de enteros aceptados (ej. [1, 2, 3]).

    Returns:
        Entero correspondiente a la opción elegida.
    """
    rango = f"1-{max(opciones_validas)}"
    while True:
        try:
            opcion = int(input(f"Tu elección ({rango}): "))
            if opcion in opciones_validas:
                return opcion
            print(f"❌ Opción no válida. Elige entre {opciones_validas}.")
        except ValueError:
            print("❌ Entrada inválida. Debes introducir un número.")