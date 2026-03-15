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


# Cada opción tiene un diccionario con las opciones que vence y el motivo.
REGLAS = {
    "Piedra":  {"Tijera": "aplasta",      "Lagarto": "aplasta"},
    "Papel":   {"Piedra": "cubre",         "Spock":   "desautoriza"},
    "Tijera":  {"Papel":  "corta",         "Lagarto": "decapita"},
    "Lagarto": {"Papel":  "come",          "Spock":   "envenena"},
    "Spock":   {"Tijera": "destroza",      "Piedra":  "vaporiza"},
}


# ── Funciones ──────────────────────────────────────────────────────────────────

def mostrar_marcador(victorias, empates, derrotas):
    """Muestra el marcador actual de la sesión."""
    print(f"\nMarcador → Tú: {victorias} | Empates: {empates} | PC: {derrotas}")


def determinar_ganador(jugador, computadora):
    """Compara las elecciones y devuelve el resultado: 'victoria', 'derrota' o 'empate'."""
    if jugador == computadora:
        print("\n🤝 ¡Empate!")
        return "empate"
    elif computadora in REGLAS[jugador]:
        motivo = REGLAS[jugador][computadora]
        print(f"\n✅ ¡Ganaste! {jugador} {motivo} a {computadora}.")
        return "victoria"
    else:
        motivo = REGLAS[computadora][jugador]
        print(f"\n❌ ¡Perdiste! {computadora} {motivo} a {jugador}.")
        return "derrota"


def obtener_eleccion_computadora():
    """Devuelve una elección aleatoria para la computadora."""
    eleccion = random.choice(list(OPCIONES.values()))
    print(f"\nLa computadora eligió: {EMOJIS[eleccion]} {eleccion}")
    return eleccion


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
    victorias, empates, derrotas = 0, 0, 0

    jugada_jugador = obtener_eleccion_jugador()
    print(f"\nTú elegiste:          {EMOJIS[jugada_jugador]} {jugada_jugador}")
    jugada_pc = obtener_eleccion_computadora()

    resultado = determinar_ganador(jugada_jugador, jugada_pc)

    if resultado == "victoria":
        victorias += 1
    elif resultado == "empate":
        empates += 1
    else:
        derrotas += 1

    mostrar_marcador(victorias, empates, derrotas)