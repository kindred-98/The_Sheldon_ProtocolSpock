# 🪨📄✂️🦎🖖 Piedra, Papel, Tijera, Lagarto, Spock

Juego de terminal en Python basado en la variante extendida popularizada por la serie *The Big Bang Theory*.

Jugador humano contra la computadora, con sistema de puntuación, estadísticas y validación de entradas.

---

## Reglas del juego

| Opción | Vence a | Motivo |
|--------|---------|--------|
| ✂️ Tijera | 📄 Papel | corta |
| ✂️ Tijera | 🦎 Lagarto | decapita |
| 📄 Papel | 🪨 Piedra | cubre |
| 📄 Papel | 🖖 Spock | desautoriza |
| 🪨 Piedra | ✂️ Tijera | aplasta |
| 🪨 Piedra | 🦎 Lagarto | aplasta |
| 🦎 Lagarto | 📄 Papel | come |
| 🦎 Lagarto | 🖖 Spock | envenena |
| 🖖 Spock | ✂️ Tijera | destroza |
| 🖖 Spock | 🪨 Piedra | vaporiza |

---

## Requisitos

- Python 3.8 o superior
- Sin dependencias externas (solo biblioteca estándar)

---

## Cómo ejecutar

```bash

# Clonar el repositorio
git clone https://github.com/tu-usuario/The_Sheldon_Protocol.git
cd The_Sheldon_Protocol

# Ejecutar el juego
python src/juego.py

```

---

## Estructura del proyecto

```
piedra-papel-tijera-spock/
│
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   └── juego.py
└── docs/
    └── asistencia_ia.md
```

---

## Documentación de asistencia IA

Los prompts utilizados con IA durante el desarrollo están documentados en [`docs/asistencia_ia.md`](docs/asistencia_ia.md).
