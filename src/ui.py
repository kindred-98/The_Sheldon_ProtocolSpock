"""
ui.py — Presentación e interfaz de terminal.
No toma decisiones ni contiene lógica del juego.
Solo recibe datos y los muestra por pantalla.
"""

import os
from src.config import EMOJIS


def limpiar_pantalla() -> None:
    """Limpia la terminal de forma compatible con Windows y Linux/Mac."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_bienvenida() -> None:
    """Muestra la pantalla de bienvenida con título y reglas."""
    limpiar_pantalla()
    print("╔══════════════════════════════════════════════╗")
    print("║  🪨 📄 ✂️  🦎 🖖 THE SHELDON PROTOCOL SPOCK ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    print("📋 REGLAS:")
    print("  • Tijera  corta Papel    | Tijera  decapita Lagarto")
    print("  • Papel   cubre Piedra   | Papel   desautoriza Spock")
    print("  • Piedra  aplasta Tijera | Piedra  aplasta Lagarto")
    print("  • Lagarto come Papel     | Lagarto envenena Spock")
    print("  • Spock   destroza Tijera| Spock   vaporiza Piedra")
    print()


def mostrar_menu_principal() -> None:
    """Muestra el menú principal de opciones."""
    print("╔══════════════════════════════════════════════╗")
    print("║  🪨 📄 ✂️  🦎 🖖 THE SHELDON PROTOCOL SPOCK ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    print("  1. 🎮 Jugar partida")
    print("  2. 📊 Ver historial de partidas")
    print("  3. 🚪 Salir")
    print()


def mostrar_cabecera_ronda(ronda: int, total: int) -> None:
    """Muestra el encabezado de la ronda actual."""
    limpiar_pantalla()
    print(f"\n──── Ronda {ronda} de {total} ────")


def mostrar_elecciones(jugador: str, computadora: str) -> None:
    """Muestra las elecciones del jugador y la computadora."""
    print(f"\nTú elegiste:           {EMOJIS[jugador]} {jugador}")
    print(f"La computadora eligió: {EMOJIS[computadora]} {computadora}")


def mostrar_resultado_ronda(resultado: str, mensaje: str) -> None:
    """Muestra el resultado de la ronda con el motivo."""
    if resultado == "victoria":
        print(f"\n✅ ¡Ganaste! {mensaje}")
    elif resultado == "derrota":
        print(f"\n❌ ¡Perdiste! {mensaje}")
    else:
        print(f"\n🤝 {mensaje}")


def mostrar_marcador(victorias: int, empates: int, derrotas: int) -> None:
    """Muestra el marcador actual de la sesión."""
    print(f"\nMarcador → Tú: {victorias} | Empates: {empates} | PC: {derrotas}")


def mostrar_resumen(victorias: int, empates: int, derrotas: int, total: int) -> None:
    """Muestra el resumen completo al final de la partida."""
    porcentaje = (victorias / total) * 100

    print("\n╔══════════════════════════════════════════════╗")
    print("║              📊 RESUMEN FINAL                ║")
    print("╚══════════════════════════════════════════════╝")
    print(f"\n  Victorias : {victorias}")
    print(f"  Empates   : {empates}")
    print(f"  Derrotas  : {derrotas}")
    print(f"\n  Porcentaje de victorias: {porcentaje:.1f}%")
    print()

    if victorias > derrotas:
        print("  🏆 ¡Ganaste la partida! Sheldon estaría orgulloso.")
    elif derrotas > victorias:
        print("  💻 ¡Ganó la computadora! Bazzinga.")
    else:
        print("  🤝 ¡Partida empatada! Digno rival.")
    print()


def mostrar_historial(historial: list) -> None:
    """Muestra el historial de partidas jugadas en la sesión."""
    print("\n╔══════════════════════════════════════════════╗")
    print("║           📋 HISTORIAL DE PARTIDAS           ║")
    print("╚══════════════════════════════════════════════╝\n")

    if not historial:
        print("  Todavía no has jugado ninguna partida.\n")
        return

    for i, partida in enumerate(historial, 1):
        resultado = partida["resultado_final"]
        emoji = "🏆" if resultado == "victoria" else "💻" if resultado == "derrota" else "🤝"
        print(
            f"  Partida {i:>2} | {partida['fecha_hora']} | "
            f"Rondas: {partida['total_rondas']:>2} | "
            f"V:{partida['victorias']} E:{partida['empates']} D:{partida['derrotas']} "
            f"| {emoji} {resultado.capitalize()}"
        )
    print()