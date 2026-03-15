import random
import os

# ── Datos del juego ────────────────────────────────────────────────────────────

OPCIONES = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera",
    4: "Lagarto",
    5: "Spock",
}

EMOJIS = {
    "Piedra":  "🪨",
    "Papel":   "📄",
    "Tijera":  "✂️ ",
    "Lagarto": "🦎",
    "Spock":   "🖖",
}


# ── Funciones ──────────────────────────────────────────────────────────────────

def obtener_eleccion_jugador():
    """Muestra el menú de opciones y devuelve la elección del jugador como string."""
    print("\nElige tu jugada:")
    for numero, nombre in OPCIONES.items():
        print(f"  {numero}. {EMOJIS[nombre]} {nombre}")

    while True:
        try:
            eleccion = int(input("\nTu elección (1-5): "))
            if eleccion in OPCIONES:
                return OPCIONES[eleccion]
            else:
                print("❌ Opción no válida. Introduce un número del 1 al 5.")
        except ValueError:
            print("❌ Entrada inválida. Debes introducir un número.")


# ── Punto de entrada temporal (para probar este commit) ───────────────────────

if __name__ == "__main__":
    jugada = obtener_eleccion_jugador()
    print(f"\nElegiste: {EMOJIS[jugada]} {jugada}")