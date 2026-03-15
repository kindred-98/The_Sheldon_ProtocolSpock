"""
main.py — Punto de entrada de The Sheldon Protocol Spock.
Arranca el menú principal y gestiona el flujo entre opciones.
Ejecutar con: python main.py
"""

from src import ui, history, session
from src.player import pedir_opcion_menu


def main() -> None:
    """Arranca el juego y gestiona el bucle del menú principal.

    Crea el historial de sesión y lo pasa a las funciones
    que lo necesitan. Maneja KeyboardInterrupt para salir
    limpiamente sin stack trace.
    """
    historial = history.crear_historial()

    while True:
        ui.limpiar_pantalla()
        ui.mostrar_menu_principal()

        opcion = pedir_opcion_menu([1, 2, 3])

        if opcion == 1:
            session.jugar(historial)

        elif opcion == 2:
            ui.limpiar_pantalla()
            ui.mostrar_historial(history.obtener_historial(historial))
            stats = history.obtener_estadisticas(historial)

            if stats["partidas_jugadas"] > 0:
                print(f"  📈 Estadísticas de la sesión:")
                print(f"     Partidas jugadas : {stats['partidas_jugadas']}")
                print(f"     Victorias totales: {stats['victorias_totales']}")
                print(f"     Derrotas totales : {stats['derrotas_totales']}")
                print(f"     Empates totales  : {stats['empates_totales']}")
                print(f"     % de victorias   : {stats['porcentaje_victorias']}%")
                print()

            input("Pulsa Enter para volver al menú...")

        elif opcion == 3:
            ui.limpiar_pantalla()
            print("\n👋 ¡Hasta la próxima! Bazinga.\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Juego interrumpido. ¡Hasta la próxima!\n")