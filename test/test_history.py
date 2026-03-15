"""
test_history.py — Tests para el historial de partidas en memoria.
"""

import pytest
from src.history import (
    crear_historial,
    guardar_partida,
    obtener_historial,
    obtener_estadisticas,
)


@pytest.fixture
def historial_vacio():
    """Devuelve un historial vacío para cada test."""
    return crear_historial()


@pytest.fixture
def historial_con_partidas():
    """Devuelve un historial con tres partidas de ejemplo."""
    h = crear_historial()
    guardar_partida(h, victorias=3, empates=0, derrotas=2, total_rondas=5)
    guardar_partida(h, victorias=1, empates=1, derrotas=3, total_rondas=5)
    guardar_partida(h, victorias=2, empates=2, derrotas=2, total_rondas=6)
    return h


class TestCrearHistorial:

    def test_devuelve_lista(self, historial_vacio):
        assert isinstance(historial_vacio, list)

    def test_lista_vacia(self, historial_vacio):
        assert len(historial_vacio) == 0


class TestGuardarPartida:

    def test_añade_una_partida(self, historial_vacio):
        guardar_partida(historial_vacio, 3, 0, 2, 5)
        assert len(historial_vacio) == 1

    def test_estructura_partida(self, historial_vacio):
        guardar_partida(historial_vacio, 3, 0, 2, 5)
        partida = historial_vacio[0]
        assert "fecha_hora"      in partida
        assert "total_rondas"    in partida
        assert "victorias"       in partida
        assert "empates"         in partida
        assert "derrotas"        in partida
        assert "resultado_final" in partida

    @pytest.mark.parametrize("victorias, derrotas, esperado", [
        (3, 1, "victoria"),
        (1, 3, "derrota"),
        (2, 2, "empate"),
    ])
    def test_resultado_final(self, historial_vacio, victorias, derrotas, esperado):
        guardar_partida(historial_vacio, victorias, 0, derrotas, 4)
        assert historial_vacio[0]["resultado_final"] == esperado

    def test_datos_guardados_correctamente(self, historial_vacio):
        guardar_partida(historial_vacio, 3, 1, 1, 5)
        p = historial_vacio[0]
        assert p["victorias"]    == 3
        assert p["empates"]      == 1
        assert p["derrotas"]     == 1
        assert p["total_rondas"] == 5


class TestObtenerHistorial:

    def test_devuelve_copia(self, historial_con_partidas):
        copia = obtener_historial(historial_con_partidas)
        assert copia is not historial_con_partidas

    def test_contenido_igual(self, historial_con_partidas):
        copia = obtener_historial(historial_con_partidas)
        assert copia == historial_con_partidas

    def test_historial_vacio(self, historial_vacio):
        assert obtener_historial(historial_vacio) == []


class TestObtenerEstadisticas:

    def test_historial_vacio_devuelve_ceros(self, historial_vacio):
        stats = obtener_estadisticas(historial_vacio)
        assert stats["partidas_jugadas"]    == 0
        assert stats["victorias_totales"]   == 0
        assert stats["porcentaje_victorias"] == 0.0

    def test_partidas_jugadas(self, historial_con_partidas):
        stats = obtener_estadisticas(historial_con_partidas)
        assert stats["partidas_jugadas"] == 3

    def test_victorias_totales(self, historial_con_partidas):
        stats = obtener_estadisticas(historial_con_partidas)
        assert stats["victorias_totales"] == 6  # 3+1+2

    def test_derrotas_totales(self, historial_con_partidas):
        stats = obtener_estadisticas(historial_con_partidas)
        assert stats["derrotas_totales"] == 7   # 2+3+2

    def test_empates_totales(self, historial_con_partidas):
        stats = obtener_estadisticas(historial_con_partidas)
        assert stats["empates_totales"] == 3    # 0+1+2

    def test_porcentaje_victorias(self, historial_con_partidas):
        stats = obtener_estadisticas(historial_con_partidas)
        # 6 victorias de 16 rondas totales = 37.5%
        assert stats["porcentaje_victorias"] == 37.5