"""
test_game.py — Tests para la lógica pura del juego.
Verifica todas las combinaciones ganadoras, derrotas y empates.
"""

import pytest
from src.game import determinar_ganador


class TestEmpates:
    """Verifica que dos elecciones iguales siempre resultan en empate."""

    @pytest.mark.parametrize("opcion", ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"])
    def test_empate_misma_opcion(self, opcion):
        resultado, _ = determinar_ganador(opcion, opcion)
        assert resultado == "empate"

    def test_empate_mensaje(self):
        _, mensaje = determinar_ganador("Piedra", "Piedra")
        assert "Empate" in mensaje


class TestVictorias:
    """Verifica las 10 combinaciones ganadoras con sus motivos correctos."""

    @pytest.mark.parametrize("jugador, computadora, motivo_esperado", [
        ("Piedra",  "Tijera",  "aplasta"),
        ("Piedra",  "Lagarto", "aplasta"),
        ("Papel",   "Piedra",  "cubre"),
        ("Papel",   "Spock",   "desautoriza"),
        ("Tijera",  "Papel",   "corta"),
        ("Tijera",  "Lagarto", "decapita"),
        ("Lagarto", "Papel",   "come"),
        ("Lagarto", "Spock",   "envenena"),
        ("Spock",   "Tijera",  "destroza"),
        ("Spock",   "Piedra",  "vaporiza"),
    ])
    def test_victoria(self, jugador, computadora, motivo_esperado):
        resultado, mensaje = determinar_ganador(jugador, computadora)
        assert resultado == "victoria"
        assert motivo_esperado in mensaje

    def test_victoria_formato_mensaje(self):
        resultado, mensaje = determinar_ganador("Piedra", "Tijera")
        assert "Piedra" in mensaje
        assert "Tijera" in mensaje


class TestDerrotas:
    """Verifica las 10 combinaciones perdedoras."""

    @pytest.mark.parametrize("jugador, computadora", [
        ("Tijera",  "Piedra"),
        ("Lagarto", "Piedra"),
        ("Piedra",  "Papel"),
        ("Spock",   "Papel"),
        ("Papel",   "Tijera"),
        ("Lagarto", "Tijera"),
        ("Papel",   "Lagarto"),
        ("Spock",   "Lagarto"),
        ("Tijera",  "Spock"),
        ("Piedra",  "Spock"),
    ])
    def test_derrota(self, jugador, computadora):
        resultado, _ = determinar_ganador(jugador, computadora)
        assert resultado == "derrota"

    def test_derrota_mensaje_contiene_computadora(self):
        _, mensaje = determinar_ganador("Tijera", "Piedra")
        assert "Piedra" in mensaje


class TestRetornos:
    """Verifica que determinar_ganador siempre devuelve una tupla válida."""

    def test_devuelve_tupla(self):
        resultado = determinar_ganador("Piedra", "Tijera")
        assert isinstance(resultado, tuple)
        assert len(resultado) == 2

    def test_resultado_es_string_valido(self):
        resultado, _ = determinar_ganador("Piedra", "Tijera")
        assert resultado in ("victoria", "derrota", "empate")

    def test_mensaje_es_string(self):
        _, mensaje = determinar_ganador("Piedra", "Tijera")
        assert isinstance(mensaje, str)
        assert len(mensaje) > 0