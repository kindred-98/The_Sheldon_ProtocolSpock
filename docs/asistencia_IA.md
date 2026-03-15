# 🤖 Documentación de Asistencia IA

Registro de los prompts utilizados con IA durante el desarrollo de **The Sheldon Protocol**.

---

## Commit 1 — Configuración inicial

**Prompt:**
> ¿Qué archivos debo incluir en .gitignore para un proyecto Python?

**Resultado:** Lista de entradas para venvs, caché de Python, IDEs y sistema operativo.

**Prompt:**
> ¿Cómo estructuro un README básico para un juego de terminal en Python?

**Resultado:** Estructura con título, descripción, reglas, requisitos, instrucciones de uso y árbol de carpetas.

---

## Commit 2 — Elección del jugador

**Prompt:**
> ¿Cómo capturo la entrada del usuario en Python con input()?

**Resultado:** Uso de `input()` combinado con `int()` y `try/except ValueError` para manejar entradas no numéricas.

**Prompt:**
> ¿Cómo mapeo un número a un string usando un diccionario en Python?

**Resultado:** Diccionario `OPCIONES = {1: "Piedra", 2: "Papel", ...}` con acceso directo por clave.

---

## Commit 3 — Elección de la computadora

**Prompt:**
> ¿Cómo uso random.choice() en Python para elegir un elemento de una lista?

**Resultado:** `random.choice(list(OPCIONES.values()))` para elegir directamente desde el diccionario existente.

**Prompt:**
> ¿Cuál es la diferencia entre random.choice() y random.randint()?

**Resultado:** `random.choice()` trabaja sobre secuencias directamente; `random.randint()` genera un número que luego hay que mapear. Se optó por `random.choice()` para evitar lógica redundante.

---

## Commit 4 — Determinar el ganador

**Prompt:**
> ¿Cómo implemento la lógica de Piedra, Papel, Tijera, Lagarto, Spock con un diccionario en Python?

**Resultado:** Diccionario anidado `REGLAS` donde cada clave es una opción y su valor es otro diccionario con las opciones que vence y el motivo. Elimina la necesidad de cadenas `if/elif`.

---

## Commit 5 — Sistema de puntuación

**Prompt:**
> ¿Es mejor usar variables globales o pasar el marcador como parámetro a las funciones?

**Resultado:** Se optó por pasar el marcador como parámetros (`victorias, empates, derrotas`) para mantener las funciones puras y sin efectos secundarios.

---

## Commit 6 — Múltiples rondas

**Prompt:**
> ¿Cómo implemento un bucle que se repita un número de veces en Python?

**Resultado:** `for ronda in range(1, total_rondas + 1)` para que el contador sea legible desde 1 en lugar de 0.

---

## Commit 7 — Interfaz de usuario

**Prompt:**
> ¿Cómo limpio la terminal en Python de forma compatible con Windows y Linux?

**Resultado:** `os.system("cls" if os.name == "nt" else "clear")` detecta el sistema operativo en tiempo de ejecución.

---

## Commit 8 — Estadísticas y resumen

**Prompt:**
> ¿Cómo calculo un porcentaje en Python y lo muestro con 1 decimal?

**Resultado:** `f"{porcentaje:.1f}%"` con f-string y especificador de formato `.1f`.

---

## Commit 9 — Versión final

**Prompt:**
> ¿Cómo escribo docstrings correctamente en Python siguiendo PEP 257?

**Resultado:** Docstring de una línea para funciones simples, entre comillas triples, con verbo en imperativo describiendo qué devuelve la función.

**Prompt:**
> ¿Cómo añado la opción de jugar otra partida sin cerrar el programa?

**Resultado:** Bucle `while True` en el punto de entrada que llama a `jugar()` y pregunta al usuario si quiere continuar.

---

## Reflexiones finales

La IA fue útil principalmente para decidir estructuras de datos (el diccionario anidado `REGLAS` fue la decisión más importante del proyecto) y para resolver detalles de compatibilidad como la limpieza de terminal entre sistemas operativos.

En todos los casos el código generado fue revisado, probado y ajustado antes de cada commit, siguiendo el Principio 4 del módulo: nunca aceptar código sin entenderlo.