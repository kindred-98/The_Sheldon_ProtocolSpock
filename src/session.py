"""
session.py — Coordinación de una partida completa.
Orquesta player, game, ui e history en el orden correcto.
No contiene lógica del juego ni código de presentación propio.
"""

from src import game, ui, history
from src.player import (
    obtener_eleccion_jugador,
    obtener_eleccion_computadora,
    pedir_numero_rondas,
)


def jugar(historial: list) -> None:
    """Ejecuta una partida completa de principio a fin.

    Gestiona el bucle de rondas, actualiza el marcador,
    guarda la partida en el historial y muestra el resumen final.

    Args:
        historial: Lista compartida donde se añade el resultado
                   de la partida al terminar.
    """
    victorias, empates, derrotas = 0, 0, 0

    ui.mostrar_bienvenida()
    total_rondas = pedir_numero_rondas()

    for ronda in range(1, total_rondas + 1):
        ui.mostrar_cabecera_ronda(ronda, total_rondas)

        jugada_jugador = obtener_eleccion_jugador()
        jugada_pc = obtener_eleccion_computadora()

        ui.mostrar_elecciones(jugada_jugador, jugada_pc)

        resultado, mensaje = game.determinar_ganador(jugada_jugador, jugada_pc)
        ui.mostrar_resultado_ronda(resultado, mensaje)

        if resultado == "victoria":
            victorias += 1
        elif resultado == "empate":
            empates += 1
        else:
            derrotas += 1

        ui.mostrar_marcador(victorias, empates, derrotas)

        if ronda < total_rondas:
            input("\nPulsa Enter para la siguiente ronda...")

    ui.mostrar_resumen(victorias, empates, derrotas, total_rondas)
    history.guardar_partida(historial, victorias, empates, derrotas, total_rondas)
    input("\nPulsa Enter para volver al menú...")