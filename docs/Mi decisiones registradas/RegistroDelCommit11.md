# 🧠 Mis Decisiones con IA

Registro personal de lo que pedí, lo que la IA propuso, en qué estuvimos de acuerdo y qué cambié yo.  
Proyecto: **The_Sheldon_ProtocolSpock**

---

## Sesión 1 — Planificación y construcción inicial

### Lo que pedí

El ejercicio original del PDF pedía un juego de Piedra, Papel o Tijera en terminal con 10 commits incrementales.
Yo pedí ampliarlo con la variante de **The Big Bang Theory**: añadir Lagarto y Spock, con los mensajes de victoria con el motivo ("Piedra aplasta a Lagarto").

También pedí que se llamara **The Sheldon Protocol** (luego corregí a **The_Sheldon_ProtocolSpock**).

### Lo que la IA propuso

Mantener exactamente la misma estructura de 10 commits del PDF pero adaptada a 5 opciones. El argumento fue que técnicamente solo cambiaba una cosa real: el diccionario de reglas pasa de 3 opciones a 5. Todo lo demás (bucles, validación, puntuación, interfaz) es idéntico.

### En qué estuvimos de acuerdo ✅

- Mantener la estructura de commits del PDF como base.
- Usar un diccionario anidado `REGLAS` para la lógica del ganador, evitando cadenas largas de `if/elif`.
- Separar `EMOJIS` de la lógica del juego, usarlos solo en la presentación.
- Validación con `while True` + `try/except` en todos los puntos de entrada.
- Pasar el marcador como parámetros a las funciones en lugar de usar variables globales.
- Encapsular la partida completa en una función `jugar()` para separar lógica de punto de entrada.
- Añadir `input("Pulsa Enter...")` entre rondas para que el jugador lea el resultado antes de que se limpie la pantalla.

### Lo que cambié yo 📝

- El nombre del repositorio: primero fue `piedra-papel-tijera-spock`, luego lo cambié a **The_Sheldon_ProtocolSpock**.
- El nombre del archivo de documentación: la IA lo llamó `asistencia_ia.md`, yo lo corregí a **asistencia_IA.md**.
- Todos los archivos generados los acomodé yo a la estructura real de mi repositorio.

---

## Sesión 2 — Profesionalización del README

### Lo que pedí

Aplicar elementos de mi sistema **IA_DEV_SYSTEM** para dejar el repo más profesional en GitHub.

### Lo que la IA propuso

No aplicar todo el framework (dijo que era overkill para este proyecto) sino piezas concretas:
- Badges en el README (Python version, licencia, estado, commits, desarrollado con IA).
- Sección "Desarrollado con IA" en el README explicando el AI Development Loop aplicado.
- `asistencia_IA.md` mejorado con el método S.P.E.C.A.R documentando el prompt más importante.

### En qué estuvimos de acuerdo ✅

- Añadir badges al README.
- Añadir ejemplo de ejecución real con output en el README.
- Documentar el método S.P.E.C.A.R en `asistencia_IA.md` para el Commit 4 (el del diccionario de reglas), que fue la decisión más importante del proyecto.
- Incluir reflexiones finales reales en `asistencia_IA.md`, no solo una lista de prompts.

### Lo que rechacé o no apliqué ❌

- GitHub Actions en esta fase. La IA lo propuso como lo que más impresiona en un repo universitario, pero lo dejé para la siguiente fase del proyecto.

---

## Sesión 3 — Modularización y arquitectura

### Lo que pedí

- Modularizar `juego.py` y repartir responsabilidades en módulos separados.
- Añadir tests completos con pytest.
- Crear un `main.py` como punto de entrada.
- Guardar historial de partidas.
- Crear este archivo `mis_decisiones_IA.md`.
- Que la IA me dijera qué más añadiría para hacerlo profesional.

### Lo que la IA propuso adicionalmente

Cosas que no pedí pero que propuso:

| Propuesta | Mi decisión |
|-----------|-------------|
| `config.py` para centralizar constantes | ✅ Acepto |
| `__init__.py` en cada carpeta | ✅ Acepto |
| Manejo de `KeyboardInterrupt` (Ctrl+C) | ✅ Acepto |
| Historial con fecha/hora y estadísticas acumuladas | ✅ Acepto |
| `pytest.ini` para configurar pytest | ✅ Acepto |
| `CHANGELOG.md` | ✅ Acepto |
| GitHub Actions para correr tests en cada push | ✅ Acepto — lo incluimos |
| Menú principal con opciones (Jugar, Historial, Salir) | ✅ Acepto |

### Decisiones técnicas acordadas ✅

- **Historial solo en memoria** — sin ficheros JSON, CSV ni SQLite. Al cerrar el programa se pierde. Es suficiente para el alcance del proyecto.
- **Tests completos** — cubrir todos los módulos con pytest, no solo las funciones clave.
- **`game.py` no imprime nada** — solo devuelve `"victoria"`, `"derrota"` o `"empate"`. Los mensajes los muestra `ui.py`. Esta fue la decisión más importante de la modularización porque es lo que hace que los tests funcionen sin capturar output de terminal.
- **Responsabilidad única por módulo** — cada archivo hace una sola cosa y no se mete en la responsabilidad del otro.

### Nueva estructura acordada

```
The_Sheldon_ProtocolSpock/
│
├── main.py
├── README.md
├── .gitignore
├── requirements.txt
├── pytest.ini
├── CHANGELOG.md
│
├── src/
│   ├── __init__.py
│   ├── config.py       ← OPCIONES, EMOJIS, REGLAS
│   ├── game.py         ← lógica pura: determinar_ganador
│   ├── player.py       ← elecciones del jugador y computadora
│   ├── ui.py           ← todo lo visual
│   ├── session.py      ← gestión del bucle de rondas
│   └── history.py      ← historial en memoria
│
├── tests/
│   ├── __init__.py
│   ├── test_game.py
│   ├── test_player.py
│   ├── test_history.py
│   └── test_session.py
│
└── docs/
    ├── asistencia_IA.md
    └── mis_decisiones_IA.md
```

### Plan de commits acordado

| Commit | Descripción |
|--------|-------------|
| 11 | Reestructura carpetas, `__init__.py`, constantes a `config.py` |
| 12 | Lógica a `game.py`, presentación a `ui.py` |
| 13 | Entradas a `player.py`, sesión a `session.py` |
| 14 | `history.py` con historial en memoria |
| 15 | `main.py` con menú principal |
| 16 | Tests completos con pytest |
| 17 | `mis_decisiones_IA.md`, `pytest.ini`, `CHANGELOG.md`, README actualizado |

---

## Principio aplicado en todo el proyecto

> Nunca aceptar código de la IA sin entenderlo.  
> Antes de cada commit: revisar línea a línea, probar manualmente, ser capaz de explicar qué hace cada función.