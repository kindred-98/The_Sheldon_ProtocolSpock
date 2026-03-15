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

def limpiar_pantalla():
    """Limpia la terminal de forma compatible con Windows y Linux/Mac."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida con el título y las reglas del juego."""
    limpiar_pantalla()
    print("╔══════════════════════════════════════════════╗")
    print("║   🪨 📄 ✂️  🦎 🖖  THE SHELDON PROTOCOL     ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    print("📋 REGLAS:")
    print("  • Tijera  corta Papel    | Tijera  decapita Lagarto")
    print("  • Papel   cubre Piedra   | Papel   desautoriza Spock")
    print("  • Piedra  aplasta Tijera | Piedra  aplasta Lagarto")
    print("  • Lagarto come Papel     | Lagarto envenena Spock")
    print("  • Spock   destroza Tijera| Spock   vaporiza Piedra")
    print()


def mostrar_resumen(victorias, empates, derrotas, total_rondas):
    """Muestra el resumen completo al final de la partida con estadísticas."""
    porcentaje = (victorias / total_rondas) * 100

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


def pedir_numero_rondas():
    """Solicita al jugador cuántas rondas quiere jugar. Devuelve un entero positivo."""
    while True:
        try:
            rondas = int(input("\n¿Cuántas rondas quieres jugar? (1-10): "))
            if 1 <= rondas <= 10:
                return rondas
            else:
                print("❌ Introduce un número entre 1 y 10.")
        except ValueError:
            print("❌ Entrada inválida. Debes introducir un número.")


# ── Punto de entrada temporal (para probar este commit) ───────────────────────

if __name__ == "__main__":
    victorias, empates, derrotas = 0, 0, 0

    mostrar_bienvenida()
    total_rondas = pedir_numero_rondas()

    for ronda in range(1, total_rondas + 1):
        limpiar_pantalla()
        print(f"\n──── Ronda {ronda} de {total_rondas} ────")

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

        if ronda < total_rondas:
            input("\nPulsa Enter para la siguiente ronda...")

    mostrar_resumen(victorias, empates, derrotas, total_rondas)