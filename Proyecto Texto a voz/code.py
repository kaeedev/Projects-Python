import newspaper
from gtts import gTTS

def extraer_texto_desde_url(url):
    try:
        # Instanciar un objeto Article con la URL proporcionada
        articulo = newspaper.Article(url)
        articulo.download()
        articulo.parse()

        # Devolver el texto del artículo
        return articulo.text
    except Exception:
        # Manejar el error y mostrar un mensaje al usuario
        print("No se pudo obtener el texto desde la URL. La pagina está protegida probablemente o no pasaste una URL")
        raise

def texto_a_audio(texto, nombre_archivo="audio.mp3", idioma="es"):
    try:
        # Verificar si hay texto para convertir a audio
        if texto.strip():
            # Crear un objeto gTTS con el texto y el idioma especificados
            tts = gTTS(text=texto, lang=idioma)

            # Guardar el audio en un archivo mp3
            print("Creando archivo de audio. Por favor, espera...")
            tts.save(nombre_archivo)
            print(f"El archivo de audio '{nombre_archivo}' ha sido creado con éxito.")
        else:
            print("No se encontró texto para convertir a audio.")
    except Exception:
        # Manejar el error y mostrar un mensaje al usuario
        print("Ocurrió un error al procesar el texto. Por favor, inténtalo de nuevo.")
        raise

def obtener_texto_opcion():
    while True:
        opcion = input("¿Deseas ingresar una URL o texto? (u/t): ")
        if opcion.lower() == "u":
            url = input("Por favor, introduce la URL del artículo: ")
            texto = extraer_texto_desde_url(url)
            return texto
        elif opcion.lower() == "t":
            texto = input("Por favor, introduce el texto que deseas convertir a audio: ")
            return texto
        else:
            print("Opción no válida. Por favor, selecciona 'u' para URL o 't' para texto.")

try:
    texto = obtener_texto_opcion()

        # Convertir el texto en audio
    texto_a_audio(texto)
except Exception:
    print("Ocurrió un error al procesar el texto")
