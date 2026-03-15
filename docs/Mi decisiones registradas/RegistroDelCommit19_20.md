
---

## Sesión 5 — Commits 19 y 20

### Commit 19 — `player.py` y `session.py`

**Lo que pedí:**
Extraer la gestión de entradas del jugador a `player.py` y la coordinación de la partida a `session.py`.

**Lo que la IA hizo:**

`player.py` agrupa todas las funciones de entrada:
- `obtener_eleccion_jugador()` — menú con validación.
- `obtener_eleccion_computadora()` — elección aleatoria.
- `pedir_numero_rondas()` — usa `MIN_RONDAS` y `MAX_RONDAS` de `config.py`, nada hardcodeado.
- `pedir_opcion_menu()` — función genérica que recibe la lista de opciones válidas. No pedí esto expresamente pero tiene sentido para el menú principal.

`session.py` actúa como director de orquesta: llama a `player`, `game`, `ui` e `history` en orden. No sabe nada de reglas ni de presentación. Recibe el `historial` como parámetro para no usar estado global.

**En qué estuvimos de acuerdo ✅**
- `session.py` recibe el `historial` como parámetro en lugar de crearlo internamente. Más limpio y testeable.
- `pedir_opcion_menu()` genérica en lugar de una función específica para cada menú.
- `session.py` termina con `input("Pulsa Enter para volver al menú...")` para que el jugador lea el resumen antes de que se limpie la pantalla.

**Lo que cambié yo 📝**
- Nada en este commit. La estructura quedó clara desde la planificación.

---

### Commit 20 — `history.py`

**Lo que pedí:**
Historial de partidas en memoria, sin persistencia en ficheros.

**Lo que la IA hizo:**
Cuatro funciones con responsabilidades separadas:
- `crear_historial()` — devuelve lista vacía. `main.py` la llama una vez al arrancar.
- `guardar_partida()` — calcula `resultado_final` y guarda un diccionario con fecha/hora y estadísticas.
- `obtener_historial()` — devuelve una copia de la lista, no la lista original.
- `obtener_estadisticas()` — calcula acumulados de toda la sesión.

**Decisiones técnicas acordadas ✅**

| Decisión | Razonamiento |
|----------|--------------|
| `crear_historial()` devuelve lista vacía | Evita estado global. `main.py` la crea y la pasa como parámetro |
| `obtener_historial()` devuelve una copia | Protege la lista original de modificaciones externas |
| Porcentaje calculado sobre rondas totales | Más preciso que calcularlo sobre número de partidas |
| Devuelve ceros si historial vacío | Evita errores de división por cero sin `try/except` |
| Fecha/hora con `datetime.now()` | El formato `dd/mm/yyyy hh:mm` que ya espera `ui.mostrar_historial()` |

**Lo que la IA propuso y no pedí:**
- `obtener_estadisticas()` con acumulados de toda la sesión. Lo acepté porque complementa bien el historial y será útil en el menú principal.

**Lo que cambié yo 📝**
- Nada en este commit. El diseño encajó con lo planificado.

---
