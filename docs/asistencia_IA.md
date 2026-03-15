# 🤖 Documentación de Asistencia IA

Registro de prompts, decisiones y metodología utilizada con IA durante el desarrollo de **The Sheldon Protocol Spock**.

---

## Metodología aplicada: AI Development Loop

```
Definir → Arquitectura → Plan → Código → Review → Optimizar → repeat
```

Cada commit de este proyecto representa una iteración del loop. No se avanzó al siguiente commit hasta revisar, probar y entender el código del anterior.

---

## Prompts por commit

### Commit 1 — Configuración inicial

**Prompt:**
> ¿Qué archivos debo incluir en .gitignore para un proyecto Python?

**Resultado:** Entradas para venvs, caché de Python, IDEs y sistema operativo.

**Prompt:**
> ¿Cómo estructuro un README básico para un juego de terminal en Python?

**Resultado:** Estructura con título, descripción, reglas, requisitos e instrucciones de uso.

---

### Commit 2 — Elección del jugador

**Prompt:**
> ¿Cómo capturo la entrada del usuario en Python con input()?

**Resultado:** Uso de `input()` con `int()` y `try/except ValueError` para manejar entradas no numéricas.

**Prompt:**
> ¿Cómo mapeo un número a un string usando un diccionario en Python?

**Resultado:** `OPCIONES = {1: "Piedra", 2: "Papel", ...}` con acceso directo por clave.

---

### Commit 3 — Elección de la computadora

**Prompt:**
> ¿Cómo uso random.choice() para elegir un elemento de una lista?

**Resultado:** `random.choice(list(OPCIONES.values()))` reutiliza el diccionario existente sin duplicar datos.

**Prompt:**
> ¿Cuál es la diferencia entre random.choice() y random.randint()?

**Resultado:** `random.choice()` trabaja sobre secuencias directamente. Se descartó `random.randint()` por requerir un mapeo adicional innecesario.

---

### Commit 4 — Determinar el ganador ⭐

Este fue el commit más importante. Se usó el método **S.P.E.C.A.R** para estructurar el prompt:

| S.P.E.C.A.R | Contenido |
|-------------|-----------|
| **S**ystem | Actúa como desarrollador Python senior |
| **P**royecto | Juego CLI de Piedra, Papel, Tijera, Lagarto, Spock |
| **E**ntorno | Python 3.8+, solo stdlib, un archivo |
| **C**onstraints | Sin cadenas if/elif, código limpio y escalable |
| **A**cción | Implementa la lógica de ganador con la estructura más eficiente |
| **R**espuesta | Código con explicación de cada decisión |

**Prompt resultante:**
> Actúa como desarrollador Python senior. Estoy construyendo un juego CLI de Piedra, Papel, Tijera, Lagarto, Spock en Python 3.8 sin dependencias externas. Necesito implementar la lógica que determina el ganador entre dos opciones. Constraints: sin cadenas largas de if/elif, código limpio y que no haya que modificar si se añade una opción nueva. Propón la estructura de datos más eficiente y genera el código con explicación de cada decisión.

**Resultado:** Diccionario anidado `REGLAS` donde cada clave es una opción y su valor es un diccionario con lo que vence y el motivo. Resuelve cualquier combinación con dos lookups, sin un solo `if` por caso.

---

### Commit 5 — Sistema de puntuación

**Prompt:**
> ¿Es mejor usar variables globales o pasar el marcador como parámetro a las funciones?

**Resultado:** Parámetros explícitos. Las funciones son más predecibles, testeables y fáciles de razonar sin estado global.

---

### Commit 6 — Múltiples rondas

**Prompt:**
> ¿Cómo implemento un bucle que se repita un número de veces mostrando progreso?

**Resultado:** `for ronda in range(1, total_rondas + 1)` para que el contador sea legible desde 1.

---

### Commit 7 — Interfaz de usuario

**Prompt:**
> ¿Cómo limpio la terminal en Python de forma compatible con Windows y Linux?

**Resultado:** `os.system("cls" if os.name == "nt" else "clear")` detecta el SO en tiempo de ejecución.

---

### Commit 8 — Estadísticas y resumen

**Prompt:**
> ¿Cómo calculo un porcentaje en Python y lo muestro con 1 decimal?

**Resultado:** `f"{porcentaje:.1f}%"` con especificador de formato en f-string.

---

### Commit 9 — Versión final

**Prompt (Code Review):**
> Actúa como code reviewer senior. Revisa este código Python y detecta bugs, malas prácticas y problemas de rendimiento.

**Resultado:** Sugerencia de encapsular el bucle principal en una función `jugar()` para separar la lógica de juego del punto de entrada. Aplicado en este commit.

**Prompt:**
> ¿Cómo escribo docstrings correctamente en Python siguiendo PEP 257?

**Resultado:** Docstring de una línea entre comillas triples, verbo en imperativo, describe qué hace y qué devuelve.

---

## Reflexiones finales

**Lo más útil de la IA en este proyecto:**
El diccionario anidado `REGLAS` fue la decisión más importante. La IA propuso una estructura que elimina toda la lógica condicional explícita y hace el código extensible sin modificaciones.

**Lo que no se delegó a la IA:**
Las pruebas manuales de cada caso (empate, victoria, derrota, entradas inválidas) y la decisión de cómo organizar los commits. El criterio de qué va en cada commit es una decisión de diseño que requiere entender el proyecto completo.

**Principio aplicado:**
Nunca se aceptó código sin entenderlo. Antes de cada commit se revisó línea a línea, se probó manualmente y se verificó que cada función tuviera una única responsabilidad.