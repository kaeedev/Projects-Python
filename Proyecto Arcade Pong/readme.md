# Arcade Pong 🎮

Este es un sencillo pero divertido juego de Pong clásico desarrollado en **Python** utilizando el módulo **Pygame**. Es perfecto para aquellos que quieran aprender sobre la programación de videojuegos básicos o disfrutar de un juego retro.

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es recrear el clásico juego de Pong en una versión arcade, con una estructura modular en Python. El enfoque está en una implementación fácil de entender, pero con características personalizables, como sonidos agregados cada vez que ocurre una acción, como cuando rebota la pelota en una de las paletas o se marca gol.

## 🛠️ Estructura del Proyecto

El proyecto está organizado en varios archivos para facilitar su mantenimiento y expansión:

Una carpeta **assets** con otra carpeta dentro llamada **sounds** para insertar algunos sonidos al juego:
- **bounce-8111.mp3**: Archivo de audio para el rebote de la pelota contra las paletas.
- **game-start-6104.mp3**: Archivo de audio para cuando el juego comienza.
- **goal-sfx-95846.mp3**: Archivo de audio para cuando uno de los jugadores marca gol.

Una carpeta **src** con todo el codigo principal de la lógica del juego. Está dividido en varios módulos:
- **ball.py**: Maneja la lógica de la pelota, incluyendo su movimiento y colisiones.
- **paddle.py**: Controla las paletas de los jugadores.
- **scoreborad.py**: Muestra y actualiza el puntaje de los jugadores.
- **game.py**: Maneja el flujo del juego y toda su lógica principal.
- **settings.py**: Configura algunos ajustes del juego como el tamaño de la pelota, tamaño de la ventana del juego, etc....
- **menu.py**: Maneja un menú para salir del juego o reiniciar la partida al pulsar la tecla ESC.

**main.py**: El archivo principal que ejecuta el juego y reúne todas las funciones del programa.

## 🚀 Funcionalidades

- **Juego clásico**: Dos jugadores controlan las paletas y el objetivo es evitar que la pelota pase por detrás de sus paletas.
- **Efectos de sonido**: El juego incluye sonidos al anotar, cuando la pelota rebota en las paletas y otros eventos.
- **Marcador dinámico**: Muestra el puntaje de ambos jugadores en pantalla.
- **Interfaz modular**: Cada componente del juego está estructurado en archivos independientes para facilitar su desarrollo y personalización.

## 🎮 Controles

- **Jugador 1**: Usa las teclas `W` y `S` para mover la paleta hacia arriba y abajo.
- **Jugador 2**: Usa las teclas de flecha hacia arriba `↑` o hacia abajo `↓` para controlar su paleta.

## 🛠️ Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   https://github.com/kaeedev/Projects-Python.git
   
2. Instala las dependencias necesarias (Es necesario ya que necesita instalarse Pygame):
   ```bash
   pip install -r requirements.txt

3. Ejecuta el juego:
   Si utilizas WSL desactivalo y ejecuta el codigo de abajo, ya que con WSL Windows no puede encontrar los archivos de audio
   ```bash
   python main.py

## 📝 Licencia

Este proyecto está disponible únicamente para uso **docente** y con fines de aprendizaje.

### Condiciones:
- El código fuente de este proyecto puede ser usado, modificado y distribuido solo con fines educativos.

Si tienes alguna duda o quieres utilizar algún recurso de este proyecto, por favor contacta conmigo.
