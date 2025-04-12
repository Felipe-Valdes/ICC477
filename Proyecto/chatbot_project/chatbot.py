# Importar la biblioteca spaCy para procesamiento de lenguaje natural

import spacy

# Importar las funciones de los módulos correspondientes

from modules.dolar import obtener_dolar
from modules.uf import obtener_uf
from modules.news import obtener_noticias
from modules.weather import obtener_clima  

# Cargar el modelo en español de spaCy
nlp = spacy.load("es_core_news_sm")

# Función principal del chatbot
# Esta función recibe un texto y devuelve una respuesta basada en el contenido del texto
# y en las funciones de los módulos importados.
# Se han añadido comentarios para explicar cada parte del código.

def chatbot_response(text):
    doc = nlp(text)

    # Respuestas básicas de saludo
    if "hola" in text.lower():
        return "¡Hola! ¿Cómo estás?"
    elif "adiós" in text.lower():
        return "¡Adiós! ¡Que tengas un buen día!"
    elif "cómo estás" in text.lower():
        return "¡Estoy bien, gracias por preguntar! ¿Y tú?"
    
    # Consultas para el valor del dólar y UF
    elif "dólar" in text.lower():
        return obtener_dolar()
    elif "uf" in text.lower():
        return obtener_uf()
    
    # Consultas para el clima (sin parámetro de ciudad, siempre será Santiago)
    elif "clima" in text.lower():
        return obtener_clima()  
    
    # Consultas para las noticias (siempre serán de business en inglés y traducidas al español)
    elif "noticias" in text.lower():
        return obtener_noticias()  
    
    # Respuesta por defecto si no se entiende el comando
    else:
        return "Lo siento, no te entendí. ¿Puedes repetirlo?"

# Interacción con el usuario
# Se inicia un bucle que permite al usuario interactuar con el chatbot
# hasta que escriba "adiós".
print("¡Hola! Soy tu chatbot. Escribe 'adiós' para salir.")
while True:
    user_input = input("Tú: ")
    
    if "adiós" in user_input.lower():
        print("Chatbot: ¡Adiós! ¡Que tengas un buen día!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
