# 🪨📄✂️🦎🖖 The Sheldon Protocol

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Estado-Completado-brightgreen?style=flat)
![Commits](https://img.shields.io/badge/Commits-10-orange?style=flat)
![AI Assisted](https://img.shields.io/badge/Desarrollado%20con-IA-blueviolet?style=flat)

> Versión extendida del clásico Piedra, Papel o Tijera con las 5 opciones de *The Big Bang Theory*.  
> Jugador humano vs computadora · Sistema de puntuación · Estadísticas de sesión · CLI interactivo.

---

## 🎮 Ejemplo de ejecución

```
╔══════════════════════════════════════════════════╗
║   🪨 📄 ✂️  🦎 🖖  THE SHELDON PROTOCOL_SPOCK  ║
╚══════════════════════════════════════════════════╝

📋 REGLAS:
  • Tijera  corta Papel    | Tijera  decapita Lagarto
  • Papel   cubre Piedra   | Papel   desautoriza Spock
  • Piedra  aplasta Tijera | Piedra  aplasta Lagarto
  • Lagarto come Papel     | Lagarto envenena Spock
  • Spock   destroza Tijera| Spock   vaporiza Piedra

¿Cuántas rondas quieres jugar? (1-10): 3

──── Ronda 1 de 3 ────

Elige tu jugada:
  1. 🪨 Piedra
  2. 📄 Papel
  3. ✂️  Tijera
  4. 🦎 Lagarto
  5. 🖖 Spock

Tu elección (1-5): 1

Tú elegiste:          🪨 Piedra
La computadora eligió: 🦎 Lagarto

✅ ¡Ganaste! Piedra aplasta a Lagarto.

Marcador → Tú: 1 | Empates: 0 | PC: 0

╔══════════════════════════════════════════════╗
║              📊 RESUMEN FINAL                ║
╚══════════════════════════════════════════════╝

  Victorias : 2
  Empates   : 0
  Derrotas  : 1

  Porcentaje de victorias: 66.7%

  🏆 ¡Ganaste la partida! Sheldon estaría orgulloso.
```

---

## 📋 Reglas del juego

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

## 🚀 Cómo ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/kindred-98/The_Sheldon_ProtocolSpock.git
cd The_Sheldon_ProtocolSpock

# Ejecutar el juego
python src/juego.py
```

**Requisitos:** Python 3.8 o superior · Sin dependencias externas.

---

## 📁 Estructura del proyecto

```
The_Sheldon_ProtocolSpock/
│
├── main.py                        ← punto de entrada, solo arranca el menú
├── README.md
├── .gitignore
├── requirements.txt               ← añadir pytest
├── pytest.ini                     ← configuración de pytest
│
├── src/
│   ├── __init__.py
│   ├── config.py                  ← constantes: OPCIONES, EMOJIS, REGLAS
│   ├── game.py                    ← lógica pura: determinar_ganador
│   ├── player.py                  ← obtener_eleccion_jugador / computadora
│   ├── ui.py                      ← todo lo visual: bienvenida, marcador, resumen
│   ├── session.py                 ← gestión de la partida: bucle de rondas
│   └── history.py                 ← historial en memoria: guardar y consultar
│
├── tests/
│   ├── __init__.py
│   ├── test_game.py               ← tests de determinar_ganador
│   ├── test_player.py             ← tests de validaciones de entrada
│   ├── test_history.py            ← tests del historial
│   └── test_session.py            ← tests de la sesión
│
└── docs/
    ├── asistencia_IA.md
    └── mis_decisiones_IA.md       ← nuevo
```

---

## 🤖 Desarrollado con IA

Este proyecto fue desarrollado aplicando el **AI Development Loop**:

```
Definir → Arquitectura → Plan → Código → Review → Optimizar
```

Cada commit representa una iteración del loop, desde la configuración inicial hasta la versión final. Los prompts utilizados, las decisiones tomadas y las reflexiones del proceso están documentados en [`docs/asistencia_IA.md`](docs/asistencia_IA.md).

---

## 📄 Licencia

MIT — libre para usar, modificar y distribuir.
