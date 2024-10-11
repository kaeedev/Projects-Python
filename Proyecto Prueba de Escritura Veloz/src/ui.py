import tkinter as tk
from tkinter import messagebox
import pygame  # Importar pygame para manejar música
from src.logic import TypingSpeedTest
from src.data import get_random_phrase

class TypingSpeedTestApp:
    def __init__(self):
        # Inicializar pygame y la música
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/Pokemon Blue_Red - Route 1.mp3")  # Ruta de la música
        pygame.mixer.music.set_volume(0.1)  # Ajusta el volumen (0.0 a 1.0)
        pygame.mixer.music.play(-1)  # Reproducir en bucle (-1 significa que se repetirá)

        self.root = tk.Tk()
        self.root.title("Prueba de Escritura Veloz")
        self.root.geometry("800x300")
        self.test = TypingSpeedTest()

        # Diccionario para almacenar el mejor tiempo por frase
        self.time_records = {}

        # GUI Elements
        self.label_phrase = tk.Label(self.root, text="Presiona Start para comenzar", font=("Helvetica", 12))
        self.label_phrase.pack(pady=10)

        self.entry_text = tk.Entry(self.root, font=("Helvetica", 14), width=50)
        self.entry_text.pack(pady=10)
        self.entry_text.config(state=tk.DISABLED)  # Inicialmente deshabilitado

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.previous_time_label = tk.Label(self.root, text="", font=("Helvetica", 10), fg="gray")
        self.previous_time_label.pack(pady=5)

        self.new_record_label = tk.Label(self.root, text="", font=("Helvetica", 12, 'bold'), fg="green")
        self.new_record_label.pack(pady=5)

    def start_test(self):
        # Reset fields
        self.result_label.config(text="")
        self.entry_text.config(state=tk.NORMAL)
        self.entry_text.delete(0, tk.END)

        # Obtener frase random
        self.test.phrase = get_random_phrase()

        # Mostrar el tiempo anterior de la frase si existe
        if self.test.phrase in self.time_records:
            previous_time = self.time_records[self.test.phrase]
            self.previous_time_label.config(text=f"Tiempo anterior: {previous_time:.2f} segundos")
        else:
            self.previous_time_label.config(text="")

        self.label_phrase.config(text=self.test.phrase)


        # Empezar el tiempo
        self.test.start_timer()

        # Bind Return key to check result
        self.entry_text.bind("<Return>", self.check_result)

        # Bloquear la selección en el Entry
        self.entry_text.bind("<Button-2>", lambda e: "break")  # Deshabilitar selección con botón del medio
        self.entry_text.bind("<Control-c>", lambda e: "break")  # Deshabilitar Ctrl+C
        self.entry_text.bind("<Control-x>", lambda e: "break")  # Deshabilitar Ctrl+X
        self.entry_text.bind("<Control-v>", lambda e: "break")  # Deshabilitar Ctrl+V
        self.entry_text.bind("<Control-C>", lambda e: "break")  # Deshabilitar Ctrl+C (mayúscula)
        self.entry_text.bind("<Control-X>", lambda e: "break")  # Deshabilitar Ctrl+X (mayúscula)
        self.entry_text.bind("<Control-V>", lambda e: "break")  # Deshabilitar Ctrl+V (mayúscula)
        self.entry_text.bind("<Control-v>", self.show_warning)  # Mostrar advertencia al intentar pegar
        self.entry_text.bind("<Control-V>", self.show_warning)  # Mostrar advertencia al intentar pegar (mayúscula)

    def show_warning(self, event):
        # Mostrar un mensaje de advertencia al intentar pegar
        messagebox.showwarning("¡ALTO! 🚫", "NO HAGAS TRAMPAS Y NO COPIES Y PEGUES EL TEXTO. 😡")
        return "break"  # Evitar que se ejecute la acción de pegar

    def check_result(self, event):
        user_input = self.entry_text.get()
        self.test.stop_timer()

        current_time = self.test.get_time()
        if self.test.check_accuracy(user_input):
            result = f"Correcto! Tiempo: {current_time:.2f} segundos"  # Mostrar 2 decimales

            # Guardar el mejor tiempo en el diccionario para esa frase
            if self.test.phrase in self.time_records:
                previous_time = self.time_records[self.test.phrase]

                # Solo actualizar si el nuevo tiempo es menor que el anterior
                if current_time < previous_time:
                    self.time_records[self.test.phrase] = current_time
                    self.new_record_label.config(text="¡Nuevo récord!")
                else:
                    self.new_record_label.config(text="")
            else:
                # Primera vez que se guarda, así que se almacena el tiempo
                self.time_records[self.test.phrase] = current_time
                self.new_record_label.config(text="")

            # Mostrar el mejor tiempo registrado
            self.previous_time_label.config(text=f"Mejor tiempo anterior: {self.time_records[self.test.phrase]:.2f} segundos")
        else:
            result = "Incorrecto! Inténtalo de nuevo."
            self.new_record_label.config(text="")  # Resetea el mensaje de nuevo récord

        self.result_label.config(text=result)
        self.entry_text.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()
