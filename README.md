<div align="center">

# 🪨📄✂️ The Sheldon Protocol Spock 🦎🖖

**Juego interactivo de Piedra, Papel, Tijera, Lagarto, Spock desarrollado en Python**  
*Arquitectura modular · CLI interactivo · Testing automatizado · Historial de sesión*

---

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-70%20passed-2ea44f?style=for-the-badge&logo=pytest&logoColor=white)](test/)
[![Coverage](https://img.shields.io/badge/Coverage-84%25-brightgreen?style=for-the-badge&logo=codecov&logoColor=white)](test/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Estado-Completado-success?style=for-the-badge)]()
[![AI Assisted](https://img.shields.io/badge/Desarrollado%20con-Claude%20AI-blueviolet?style=for-the-badge)]()

</div>

---

## 📌 Índice

- [Descripción](#-descripción)
- [Características](#-características)
- [Reglas del juego](#-reglas-del-juego)
- [Arquitectura](#-arquitectura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#️-uso)
- [Ejemplo de ejecución](#-ejemplo-de-ejecución)
- [Testing](#-testing)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Tecnologías](#-tecnologías)
- [Changelog](#-changelog)
- [Autor](#-autor)
- [Licencia](#-licencia)

---

## 📖 Descripción

**The Sheldon Protocol Spock** es un juego de terminal desarrollado en Python que implementa la variante extendida de Piedra, Papel o Tijera popularizada por *The Big Bang Theory*, enfrentando al jugador humano contra la computadora.

El proyecto fue construido con foco en:

- 🏗️ **Arquitectura modular** — separación clara por responsabilidades (`config`, `game`, `player`, `ui`, `session`, `history`)
- 🧪 **Testing robusto** — 70 tests automatizados con 84% de cobertura
- 🎮 **CLI interactivo** — menú principal, historial de sesión y estadísticas acumuladas
- 🤖 **Desarrollo asistido por IA** — proceso documentado commit a commit

---

## 🚀 Características

| Funcionalidad | Descripción | Estado |
|---|---|:---:|
| 5 opciones de juego | Piedra, Papel, Tijera, Lagarto, Spock | ✅ |
| Mensajes con motivo | "Piedra aplasta a Lagarto" en cada resultado | ✅ |
| Múltiples rondas | Configurable de 1 a 10 rondas por partida | ✅ |
| Marcador en tiempo real | Actualizado tras cada ronda | ✅ |
| Historial de sesión | Registro de todas las partidas jugadas | ✅ |
| Estadísticas acumuladas | Victorias, derrotas, empates y % de victorias | ✅ |
| Menú principal | Jugar, Ver historial, Salir | ✅ |
| Validación de entradas | Manejo de letras, números fuera de rango y entrada vacía | ✅ |
| Salida limpia | Manejo de Ctrl+C sin stack trace | ✅ |
| Tests automatizados | Suite con pytest + cobertura | ✅ |

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

## 🧠 Arquitectura del proyecto

```
┌─────────────────────────────────────────────────────────────────┐
│                  The Sheldon Protocol Spock                     │
│                                                                 │
│  ┌───────────────┐          ┌───────────────────────────────┐   │
│  │    main.py    │          │            src/               │   │
│  │               │◄────────►│                               │   │
│  │Menú principal │          │  config.py  → constantes      │   │
│  │KeyboardInterrupt         │  game.py    → lógica pura     │   │
│  │               │          │  player.py  → entradas        │   │
│  └───────────────┘          │  ui.py      → presentación    │   │
│                             │  session.py → coordinación    │   │
│                             │  history.py → historial       │   │
│                             └───────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Instalación

### Requisitos previos

- Python 3.8 o superior
- pip

### Pasos

**1. Clonar el repositorio:**

```bash
git clone https://github.com/kindred-98/The_Sheldon_ProtocolSpock.git
cd The_Sheldon_ProtocolSpock
```

**2. Instalar dependencias de desarrollo:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

### Ejecutar el juego

```bash
python main.py
```

### Ejecutar los tests

```bash
pytest
```

### Ejecutar tests con cobertura

```bash
pytest --cov
```

---

## 💡 Ejemplo de ejecución

```
╔══════════════════════════════════════════════╗
║  🪨 📄 ✂️  🦎 🖖 THE SHELDON PROTOCOL SPOCK ║
╚══════════════════════════════════════════════╝

  1. 🎮 Jugar partida
  2. 📊 Ver historial de partidas
  3. 🚪 Salir

──── Ronda 1 de 3 ────

Elige tu jugada:
  1. 🪨 Piedra
  2. 📄 Papel
  3. ✂️  Tijera
  4. 🦎 Lagarto
  5. 🖖 Spock

Tu elección (1-5): 1

Tú elegiste:           🪨 Piedra
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

## 🧪 Testing

El proyecto incluye una suite completa de tests automatizados con **pytest**.

```bash
# Todos los tests
pytest

# Con reporte de cobertura
pytest --cov

# Con reporte HTML
pytest --cov --cov-report=html
```

**Resultados actuales:**

```
==================== test session starts ====================

test/test_game.py       .......... PASSED
test/test_history.py    .......... PASSED
test/test_player.py     .......... PASSED
test/test_session.py    .....      PASSED

============== 70 passed in 0.36s ==============

Name               Stmts   Miss  Cover
--------------------------------------
src/config.py          5      0   100%
src/game.py            9      0   100%
src/history.py        23      0   100%
src/player.py         35      0   100%
src/session.py        24      1    96%
src/ui.py             68     57    16%
--------------------------------------
TOTAL                365     58    84%
```

---

## 📂 Estructura del proyecto

```
The_Sheldon_ProtocolSpock/
│
├── main.py                        ← punto de entrada, menú principal
├── conftest.py                    ← configuración de imports para pytest
├── pytest.ini                     ← configuración del runner de tests
├── README.md
├── .gitignore
├── requirements.txt
├── CHANGELOG.md
├── LICENSE
│
├── .github/
│   └── workflows/
│       └── tests.yml              ← GitHub Actions: tests en cada push
│
├── src/
│   ├── __init__.py
│   ├── config.py                  ← OPCIONES, EMOJIS, REGLAS
│   ├── game.py                    ← lógica pura: determinar_ganador
│   ├── player.py                  ← elecciones del jugador y computadora
│   ├── ui.py                      ← todo lo visual
│   ├── session.py                 ← coordinación del bucle de partida
│   └── history.py                 ← historial en memoria
│
├── test/
│   ├── __init__.py
│   ├── test_game.py
│   ├── test_player.py
│   ├── test_history.py
│   └── test_session.py
│
└── docs/
    ├── asistencia_IA.md
    └── Mi decisiones registradas/
        ├── RegistroDelCommit.md
        ├── RegistroDelCommit17_18.md
        ├── RegistroDelCommit19_20.md
        └── RegistroDelCommit21_22.md
```

---

## 🛠 Tecnologías

| Tecnología | Uso |
|---|---|
| [Python 3.8+](https://python.org) | Lenguaje principal |
| [Pytest](https://pytest.org) | Framework de testing |
| [Pytest-cov](https://github.com/pytest-dev/pytest-cov) | Cobertura de tests |
| [GitHub Actions](https://github.com/features/actions) | CI/CD — tests automáticos en cada push |

---

## 📋 Changelog

### v2.0.0 — Modularización completa
- ✅ Arquitectura modular con separación de responsabilidades
- ✅ `main.py` con menú principal (Jugar, Historial, Salir)
- ✅ Historial de sesión con estadísticas acumuladas
- ✅ 70 tests automatizados — 84% de cobertura
- ✅ GitHub Actions para tests automáticos en cada push
- ✅ Manejo de `KeyboardInterrupt` para salida limpia

### v1.0.0 — Versión inicial
- ✅ Juego funcional en un único archivo `src/juego.py`
- ✅ Variante de The Big Bang Theory con 5 opciones
- ✅ Mensajes de victoria con motivo ("Piedra aplasta a Lagarto")
- ✅ Sistema de puntuación y resumen final

---

## 🤖 IA utilizada durante el desarrollo

Este proyecto fue desarrollado con asistencia de **Claude (Anthropic)** como herramienta principal.

| Fase | Uso de Claude |
|---|---|
| Planificación | Estructura de commits, arquitectura modular y decisiones técnicas |
| Generación de código | Módulos, tests y configuración |
| Code review | Revisión de estructura, naming y separación de responsabilidades |
| Documentación | README, CHANGELOG y registros de decisiones |

Claude no tomó decisiones por sí solo. Todo el código generado fue analizado, comprendido y modificado según las necesidades del proyecto. El proceso completo está documentado en [`docs/`](docs/).

---

## 👨‍💻 Autor

<div align="center">

**MDL**

*Proyecto educativo — Módulo 2: Estrategias de Generación de Código con IA · Dicampus*

[![GitHub](https://img.shields.io/badge/GitHub-@tu__usuario-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98/The_Sheldon_ProtocolSpock.git)

</div>

---

<div align="center">

## 📜 Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

Ver archivo [LICENSE](LICENSE) para más detalles.

---

*Hecho con 🐍 Python y arquitectura modular*

⭐ Si este proyecto te resulta útil, considera dejarle una estrella en GitHub

</div>