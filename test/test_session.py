"""
test_session.py — Tests para la coordinación de la sesión de juego.
Usa mocks para aislar session.py de sus dependencias externas.
"""

import pytest
from unittest.mock import patch, call
from src.session import jugar
from src.history import crear_historial


@pytest.fixture
def historial():
    return crear_historial()


class TestJugar:
    """Verifica que jugar() coordina correctamente todos los módulos."""

    def test_guarda_partida_en_historial(self, historial):
        """Una partida completada debe añadirse al historial."""
        with patch("src.session.pedir_numero_rondas", return_value=1), \
             patch("src.session.obtener_eleccion_jugador", return_value="Piedra"), \
             patch("src.session.obtener_eleccion_computadora", return_value="Tijera"), \
             patch("src.session.ui"), \
             patch("src.session.history.guardar_partida") as mock_guardar, \
             patch("builtins.input", return_value=""):
            jugar(historial)
            assert mock_guardar.called

    def test_llama_mostrar_bienvenida(self, historial):
        """La bienvenida debe mostrarse al inicio de cada partida."""
        with patch("src.session.pedir_numero_rondas", return_value=1), \
             patch("src.session.obtener_eleccion_jugador", return_value="Spock"), \
             patch("src.session.obtener_eleccion_computadora", return_value="Spock"), \
             patch("src.session.ui") as mock_ui, \
             patch("src.session.history.guardar_partida"), \
             patch("builtins.input", return_value=""):
            jugar(historial)
            mock_ui.mostrar_bienvenida.assert_called_once()

    def test_llama_mostrar_resumen(self, historial):
        """El resumen debe mostrarse al final de cada partida."""
        with patch("src.session.pedir_numero_rondas", return_value=1), \
             patch("src.session.obtener_eleccion_jugador", return_value="Papel"), \
             patch("src.session.obtener_eleccion_computadora", return_value="Piedra"), \
             patch("src.session.ui") as mock_ui, \
             patch("src.session.history.guardar_partida"), \
             patch("builtins.input", return_value=""):
            jugar(historial)
            mock_ui.mostrar_resumen.assert_called_once()

    def test_numero_correcto_de_rondas(self, historial):
        """El marcador debe mostrarse tantas veces como rondas haya."""
        with patch("src.session.pedir_numero_rondas", return_value=3), \
             patch("src.session.obtener_eleccion_jugador", return_value="Piedra"), \
             patch("src.session.obtener_eleccion_computadora", return_value="Tijera"), \
             patch("src.session.ui") as mock_ui, \
             patch("src.session.history.guardar_partida"), \
             patch("builtins.input", return_value=""):
            jugar(historial)
            assert mock_ui.mostrar_marcador.call_count == 3

    def test_victoria_suma_correctamente(self, historial):
        """Ganar todas las rondas debe llamar guardar_partida con victorias correctas."""
        with patch("src.session.pedir_numero_rondas", return_value=2), \
             patch("src.session.obtener_eleccion_jugador", return_value="Piedra"), \
             patch("src.session.obtener_eleccion_computadora", return_value="Tijera"), \
             patch("src.session.ui"), \
             patch("src.session.history.guardar_partida") as mock_guardar, \
             patch("builtins.input", return_value=""):
            jugar(historial)
            args = mock_guardar.call_args
            assert args[0][1] == 2  # victorias
            assert args[0][3] == 0  # derrotas