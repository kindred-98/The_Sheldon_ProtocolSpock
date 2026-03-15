# Changelog

Todos los cambios relevantes de este proyecto están documentados aquí.  
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [2.0.0] — Modularización completa

### Añadido
- `src/config.py` — constantes centralizadas: `OPCIONES`, `EMOJIS`, `REGLAS`, `MIN_RONDAS`, `MAX_RONDAS`
- `src/game.py` — lógica pura del juego, sin output de terminal
- `src/player.py` — gestión de todas las entradas del jugador y la computadora
- `src/ui.py` — presentación completa separada de la lógica
- `src/session.py` — coordinación del bucle de partida
- `src/history.py` — historial de partidas en memoria con estadísticas acumuladas
- `main.py` — punto de entrada con menú principal (Jugar, Ver historial, Salir)
- `conftest.py` — configuración de pytest para resolución de imports
- `pytest.ini` — configuración del runner de tests
- Tests completos con pytest: 70 tests, 84% de cobertura
- Manejo de `KeyboardInterrupt` para salida limpia con Ctrl+C
- `docs/mis_decisiones_IA.md` — registro de decisiones tomadas con asistencia IA

### Cambiado
- `determinar_ganador()` ahora devuelve una tupla `(resultado, mensaje)` en lugar de imprimir directamente
- `requirements.txt` actualizado con `pytest>=7.0.0`
- Nombre del proyecto actualizado a **The Sheldon Protocol Spock** en todos los archivos

---

## [1.0.0] — Versión inicial

### Añadido
- Juego funcional de Piedra, Papel, Tijera, Lagarto, Spock en un único archivo `src/juego.py`
- Reglas completas de la variante de The Big Bang Theory (10 combinaciones ganadoras)
- Mensajes de victoria con motivo ("Piedra aplasta a Lagarto")
- Sistema de puntuación por rondas con marcador actualizado tras cada ronda
- Múltiples rondas configurables (1-10) con validación de entrada
- Interfaz de terminal con pantalla de bienvenida, emojis y separadores visuales
- Resumen final con estadísticas y porcentaje de victorias
- Opción de jugar otra partida sin cerrar el programa
- `docs/asistencia_IA.md` — prompts y metodología usada con IA
- README con badges, ejemplo de ejecución y tabla de reglas