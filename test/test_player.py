"""
test_player.py — Tests para las entradas del jugador y elección de la computadora.
Usa monkeypatch para simular entradas de teclado sin interacción real.
"""

import pytest
from src.player import obtener_eleccion_computadora
from src.config import OPCIONES


class TestEleccionComputadora:
    """Verifica que la computadora siempre elige una opción válida."""

    def test_eleccion_es_valida(self):
        eleccion = obtener_eleccion_computadora()
        assert eleccion in OPCIONES.values()

    def test_eleccion_es_string(self):
        eleccion = obtener_eleccion_computadora()
        assert isinstance(eleccion, str)

    def test_multiples_elecciones_son_validas(self):
        """Verifica 20 elecciones seguidas para cubrir aleatoriedad."""
        opciones_validas = set(OPCIONES.values())
        for _ in range(20):
            assert obtener_eleccion_computadora() in opciones_validas


class TestEleccionJugador:
    """Verifica la función obtener_eleccion_jugador con entradas simuladas."""

    @pytest.mark.parametrize("entrada, esperado", [
        ("1", "Piedra"),
        ("2", "Papel"),
        ("3", "Tijera"),
        ("4", "Lagarto"),
        ("5", "Spock"),
    ])
    def test_eleccion_valida(self, monkeypatch, entrada, esperado):
        from src.player import obtener_eleccion_jugador
        monkeypatch.setattr("builtins.input", lambda _: entrada)
        assert obtener_eleccion_jugador() == esperado

    def test_entrada_invalida_luego_valida(self, monkeypatch, capsys):
        """Simula entrada inválida seguida de una válida."""
        from src.player import obtener_eleccion_jugador
        entradas = iter(["abc", "9", "3"])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        resultado = obtener_eleccion_jugador()
        assert resultado == "Tijera"

    def test_entrada_vacia_luego_valida(self, monkeypatch):
        from src.player import obtener_eleccion_jugador
        entradas = iter(["", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        assert obtener_eleccion_jugador() == "Papel"


class TestPedirNumeroRondas:
    """Verifica la validación del número de rondas."""

    @pytest.mark.parametrize("entrada", ["1", "5", "10"])
    def test_numero_valido(self, monkeypatch, entrada):
        from src.player import pedir_numero_rondas
        monkeypatch.setattr("builtins.input", lambda _: entrada)
        assert pedir_numero_rondas() == int(entrada)

    def test_numero_fuera_de_rango_luego_valido(self, monkeypatch):
        from src.player import pedir_numero_rondas
        entradas = iter(["0", "11", "-1", "5"])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        assert pedir_numero_rondas() == 5

    def test_letra_luego_valido(self, monkeypatch):
        from src.player import pedir_numero_rondas
        entradas = iter(["abc", "3"])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        assert pedir_numero_rondas() == 3


class TestPedirOpcionMenu:
    """Verifica la validación genérica del menú."""

    def test_opcion_valida(self, monkeypatch):
        from src.player import pedir_opcion_menu
        monkeypatch.setattr("builtins.input", lambda _: "2")
        assert pedir_opcion_menu([1, 2, 3]) == 2

    def test_opcion_invalida_luego_valida(self, monkeypatch):
        from src.player import pedir_opcion_menu
        entradas = iter(["5", "abc", "1"])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        assert pedir_opcion_menu([1, 2, 3]) == 1