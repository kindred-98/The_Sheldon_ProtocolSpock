
---

## Sesión 6 — Commits 21 y 22: `main.py`, tests y resolución de incidencia

### Commit 21 — `main.py`

**Lo que pedí:**
Crear el punto de entrada con menú principal.

**Lo que la IA hizo:**
- `main()` crea el historial una vez con `history.crear_historial()` y lo pasa como parámetro a todo lo que lo necesita. Sin estado global en ningún punto.
- Bucle `while True` que limpia la pantalla en cada iteración para que el menú aparezca siempre fresco.
- Opción 2 muestra historial y estadísticas juntos. Si no hay partidas jugadas, el bloque de stats no aparece.
- `try/except KeyboardInterrupt` en `__main__` para capturar Ctrl+C en cualquier punto y salir limpiamente sin stack trace.

**En qué estuvimos de acuerdo ✅**
- `main()` no contiene lógica del juego, solo coordina el flujo entre módulos.
- El historial se crea en `main()` y se pasa como parámetro, no como variable global.
- `KeyboardInterrupt` se captura en el punto de entrada, no dentro de los módulos.

**Lo que cambié yo 📝**
- Nada en este commit.

---

### Commit 22 — Tests completos con pytest

**Lo que pedí:**
Tests completos cubriendo todos los módulos.

**Lo que la IA generó:**

| Archivo | Técnica usada | Qué cubre |
|---------|---------------|-----------|
| `test_game.py` | `@pytest.mark.parametrize` | 10 victorias, 10 derrotas, 5 empates — 100% de combinaciones |
| `test_player.py` | `monkeypatch` | Entradas válidas, inválidas, vacías y fuera de rango |
| `test_history.py` | `fixtures` | Estructura, cálculos, copia vs referencia |
| `test_session.py` | `unittest.mock.patch` | Coordinación de módulos sin testear sus dependencias |

También se generaron:
- `pytest.ini` — configura `testpaths`, nombre de archivos y clases de test, y activa `-v --tb=short`.
- `requirements.txt` actualizado con `pytest>=7.0.0`.

**En qué estuvimos de acuerdo ✅**
- Separar los tests por módulo en archivos distintos.
- Usar clases `Test*` para agrupar tests relacionados dentro de cada archivo.
- `test_game.py` cubre el 100% de combinaciones posibles con `parametrize`, no solo casos representativos.
- `test_session.py` usa mocks para aislar `session.py` de sus dependencias — no se testea lo que ya prueban otros archivos.

---

### Incidencia — `ModuleNotFoundError: No module named 'src'`

**Qué pasó:**
Al correr `pytest` por primera vez aparecieron 4 errores de colección. Todos del mismo tipo: `ModuleNotFoundError: No module named 'src'`.

**Causa raíz — dos problemas simultáneos:**

| Problema | Causa | Fix |
|----------|-------|-----|
| `No module named 'src'` | Python no sabía que la raíz del proyecto estaba en el path de búsqueda | Crear `conftest.py` en la raíz con `sys.path.insert` |
| `No files were found in testpaths` | `pytest.ini` tenía `testpaths = tests` pero la carpeta real se llama `test` (sin s) | Cambiar `pytest.ini` a `testpaths = test` |

**Solución aplicada:**

`conftest.py` en la raíz del proyecto:
```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
```
Este archivo lo carga pytest automáticamente antes de correr cualquier test. El `sys.path.insert` le dice a Python que busque módulos desde la raíz, por eso `from src.game import ...` pasa a funcionar.

**Resultado tras el fix:**
```
70 passed in 0.36s

Name                Stmts   Miss  Cover
---------------------------------------
src\config.py           5      0   100%
src\game.py             9      0   100%
src\history.py         23      0   100%
src\player.py          35      0   100%
src\session.py         24      1    96%
src\ui.py              68     57    16%
---------------------------------------
TOTAL                 365     58    84%
```

**Por qué `ui.py` tiene 16% de cobertura:**
`ui.py` solo contiene funciones que imprimen en pantalla. No tiene lógica que testear, por eso no escribimos tests para ella. El 16% son las líneas que se ejecutan indirectamente desde otros tests. Esto es correcto y esperado.

**Decisión tomada:**
No añadir tests para `ui.py`. Testear output de terminal no aporta valor real y hace los tests frágiles. El 84% de cobertura total es un resultado sólido para este proyecto.

**Lo que cambié yo 📝**
- Detecté el error ejecutando pytest tú mismo antes de hacer el commit. La incidencia se resolvió en el momento, no después.

---

