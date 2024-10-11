## ESP:

# Prueba de Escritura Veloz ✍️🍃

Este es un sencillo programa con el que podrás poner a prueba la velocidad de tu escritura en el ordenador. Ideal para mejorar la velocidad de tu mecanografía.

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es recrear un programa para realizar test de velocidad de escritura en el ordenador. Está realizado en **Python** con los módulos **Tkinter** para generar 
una interfaz, **random** para generar frases randoms a partir de un archivo de texto y **timeit** para controlar el cronómetro

## 🛠️ Estructura del Proyecto

El proyecto está organizado en varios archivos para facilitar su mantenimiento y expansión:

Una carpeta **assets** con otra carpeta dentro llamada **sounds** para insertar algunos sonidos al juego:
- **Pokemon Blue_Red - Route 1.mp3**: Archivo de audio que se utiliza para poner de música de fondo mientras el programa está ejecutandose
  
Una carpeta **src** con todo el codigo principal de la lógica del juego. Está dividido en varios módulos:
- **data.py**: Aquí se utiliza el módulo **random** para obtener frases aleatorias a partir de un fichero de texto.
- **logic.py**: Controla la lógica del cronómetro con el módulo **timeit**
- **ui.py**: Maneja el flujo del programa y toda su lógica principal, así como generar la interfaz con el módulo **tkinter**, introducir la música con el módulo **pygane**, mostrar resultados, etc...

**main.py**: El archivo principal que ejecuta el juego y reúne todas las funciones del programa.
**phrases.txt**: Archivo de texto que recoge todas las frases disponibles para el programa.

## 🚀 Funcionalidades y uso

- **Botón de start**: Generará una frase aleatoria y usted deberá escribirla en el menor tiempo posible. Al pulsar la tecla `Enter` el cronómetro se parará
- **Historial de tiempo**: Tras completar cada frase con éxito, se guardará el tiempo que has tardado. Si vuelve a salir la misma frase, abajo se te indicará cuanto tardaste la última vez en escribirla, y si la escribes más rápido batirás un record y se almacenará el nuevo tiempo.
- **Antitrampas**: Existe una función para que no se pueda copiar y pegar el texto y así obtener los mejores tiempos posibles. Saltará un cuadro de texto con un warning indicando que no hagas trampas.
- **Errores**: Si te equivocas en escribir la frase, aunque sea por una coma o una tilde, te marcará la frase como incorrecta y no se te guardará el tiempo.

## 🎮 Controles

- **Start**: Botón para generar una nueva frase cada vez.
- **Enter**: Pulsa la tecla `Enter` al acabar la frase para que se pare el cronómetro y guarde el tiempo.

## 🛠️ Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   https://github.com/kaeedev/Projects-Python.git
   
2. No es necesario instalar ninguna dependencia, solo es necesario tener VSCode para abrirlo

3. Ejecuta el juego sin utilizar WSL:
   ```bash
   python main.py

## 📝 Licencia

Este proyecto está disponible únicamente para uso **docente** y con fines de aprendizaje.

### Condiciones:
- El código fuente de este proyecto puede ser usado, modificado y distribuido solo con fines educativos.

Si tienes alguna duda o quieres utilizar algún recurso de este proyecto, por favor contacta conmigo.

---
## ENG:

# Fast Typing Test ✍️🍃

This is a simple program that allows you to test your typing speed on the computer. It's ideal for improving your typing skills.

## 🎯 Project Objective

The goal of this project is to recreate a program to conduct typing speed tests on the computer. It is built in **Python** using the **Tkinter** module to create a user interface, **random** to generate random phrases from a text file, and **timeit** to control the timer.

## 🛠️ Project Structure

The project is organized into several files to facilitate maintenance and expansion:

An **assets** folder with another folder inside called **sounds** to insert some sounds into the game:

- **Pokemon Blue_Red - Route 1.mp3:** An audio file used as background music while the program is running.
  
A **src** folder containing all the main code for the game logic. It is divided into several modules:

- **data.py:** This uses the random module to obtain random phrases from a text file.
- **logic.py:** Controls the timer logic using the timeit module.
- **ui.py:** Manages the program flow and all its main logic, including generating the interface with the tkinter module, introducing music with the pygame module, displaying results, etc.
- **main.py:** The main file that runs the game and brings together all the program functions.
- **phrases.txt:** A text file that contains all the phrases available for the program.

## 🚀 Features and Usage

- **Start Button:** Generates a random phrase that you must type as quickly as possible. Pressing the Enter key will stop the timer.
- **Time History:** After successfully completing each phrase, the time you took will be saved. If the same phrase appears again, it will indicate below how long you took the last time to type it, and if you type it faster, you'll break a record, and the new time will be stored.
- **Anti-cheat:** There is a function that prevents copying and pasting the text to achieve the best possible times. A warning message will pop up indicating not to cheat.
- **Errors:** If you make a mistake in typing the phrase, even by a comma or an accent, the phrase will be marked as incorrect, and the time will not be saved.
  
## 🎮 Controls

- **Start:** Button to generate a new phrase each time.
- **Enter:** Press the Enter key after finishing the phrase to stop the timer and save the time.
  
## 🛠️ Installation and Execution

- Clone this repository:
   ```bash
   https://github.com/kaeedev/Projects-Python.git
   
- No dependencies need to be installed; you only need to have VSCode to open it.

- Run the game without using WSL:
  ```bash
  python main.py
  
## 📝 License

This project is available solely for educational use and for learning purposes.

### Conditions:

The source code of this project can be used, modified, and distributed only for educational purposes.
If you have any questions or want to use any resources from this project, please contact me.
