"""
history.py — Gestión del historial de partidas en memoria.
Los datos se pierden al cerrar el programa (sin persistencia en ficheros).
"""

from datetime import datetime


def crear_historial() -> list:
    """Crea y devuelve una lista vacía para almacenar el historial.

    Returns:
        Lista vacía que actuará como historial de la sesión.
    """
    return []


def guardar_partida(
    historial: list,
    victorias: int,
    empates: int,
    derrotas: int,
    total_rondas: int,
) -> None:
    """Añade el resultado de una partida al historial.

    Args:
        historial: Lista donde se almacenan las partidas.
        victorias: Número de rondas ganadas.
        empates: Número de rondas empatadas.
        derrotas: Número de rondas perdidas.
        total_rondas: Total de rondas jugadas en la partida.
    """
    if victorias > derrotas:
        resultado_final = "victoria"
    elif derrotas > victorias:
        resultado_final = "derrota"
    else:
        resultado_final = "empate"

    partida = {
        "fecha_hora":      datetime.now().strftime("%d/%m/%Y %H:%M"),
        "total_rondas":    total_rondas,
        "victorias":       victorias,
        "empates":         empates,
        "derrotas":        derrotas,
        "resultado_final": resultado_final,
    }
    historial.append(partida)


def obtener_historial(historial: list) -> list:
    """Devuelve una copia del historial de partidas.

    Returns:
        Lista de diccionarios con los datos de cada partida.
    """
    return list(historial)


def obtener_estadisticas(historial: list) -> dict:
    """Calcula estadísticas acumuladas de todas las partidas jugadas.

    Args:
        historial: Lista de partidas guardadas.

    Returns:
        Diccionario con totales y porcentaje de victorias.
        Devuelve ceros si no se ha jugado ninguna partida.
    """
    if not historial:
        return {
            "partidas_jugadas": 0,
            "victorias_totales": 0,
            "derrotas_totales": 0,
            "empates_totales": 0,
            "porcentaje_victorias": 0.0,
        }

    partidas = len(historial)
    victorias = sum(p["victorias"] for p in historial)
    derrotas  = sum(p["derrotas"]  for p in historial)
    empates   = sum(p["empates"]   for p in historial)
    total_rondas = sum(p["total_rondas"] for p in historial)

    porcentaje = (victorias / total_rondas * 100) if total_rondas > 0 else 0.0

    return {
        "partidas_jugadas":    partidas,
        "victorias_totales":   victorias,
        "derrotas_totales":    derrotas,
        "empates_totales":     empates,
        "porcentaje_victorias": round(porcentaje, 1),
    }