import random

def get_random_phrase():
    # Abrir el archivo con la codificación utf-8 para manejar las tildes correctamente
    with open("phrases.txt", "r", encoding="utf-8") as file:
        phrases = file.readlines()
    return random.choice(phrases).strip()
