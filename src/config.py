"""
config.py — Constantes globales del juego.
Cualquier módulo que necesite datos del juego los importa desde aquí.
"""

# Opciones disponibles: número → nombre
OPCIONES = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera",
    4: "Lagarto",
    5: "Spock",
}

# Emoji asociado a cada opción, usado solo en la presentación
EMOJIS = {
    "Piedra":  "🪨",
    "Papel":   "📄",
    "Tijera":  "✂️ ",
    "Lagarto": "🦎",
    "Spock":   "🖖",
}

# Reglas del juego: quién vence a quién y con qué motivo
# Estructura: { ganador: { perdedor: "motivo" } }
REGLAS = {
    "Piedra":  {"Tijera": "aplasta",    "Lagarto": "aplasta"},
    "Papel":   {"Piedra": "cubre",      "Spock":   "desautoriza"},
    "Tijera":  {"Papel":  "corta",      "Lagarto": "decapita"},
    "Lagarto": {"Papel":  "come",       "Spock":   "envenena"},
    "Spock":   {"Tijera": "destroza",   "Piedra":  "vaporiza"},
}

# Límites de rondas por partida
MIN_RONDAS = 1
MAX_RONDAS = 10