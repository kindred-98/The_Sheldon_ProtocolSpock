"""
game.py — Lógica pura del juego.
No imprime nada. Solo recibe datos y devuelve resultados.
Esto permite testear la lógica sin depender de la terminal.
"""

from src.config import REGLAS


def determinar_ganador(jugador: str, computadora: str) -> tuple[str, str]:
    """Compara dos elecciones y devuelve el resultado y el motivo.

    Args:
        jugador: Elección del jugador (ej. "Piedra").
        computadora: Elección de la computadora (ej. "Tijera").

    Returns:
        Tupla (resultado, mensaje) donde resultado es
        'victoria', 'derrota' o 'empate', y mensaje describe
        por qué (ej. "Piedra aplasta a Tijera").
    """
    if jugador == computadora:
        return "empate", "Empate. Ninguno gana."

    if computadora in REGLAS[jugador]:
        motivo = REGLAS[jugador][computadora]
        return "victoria", f"{jugador} {motivo} a {computadora}."

    motivo = REGLAS[computadora][jugador]
    return "derrota", f"{computadora} {motivo} a {jugador}."