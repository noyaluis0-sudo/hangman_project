import random

def get_random_word():
    """
    Lee palabras de wordlist.txt y devuelve una palabra aleatoria
    que contenga solo caracteres alfabéticos.
    """
    words = []
    
    try:

        with open("wordlist.txt", "r", encoding="utf-8") as file:
            for line in file:
                # Limpiar espacios en blanco y saltos de línea
                word = line.strip()
                
                # Filtrar para incluir solo palabras con caracteres alfabéticos
                if word.isalpha():
                    words.append(word)
        
        # Devolver una palabra aleatoria de la lista filtrada
        return random.choice(words) if words else None
        
    except FileNotFoundError:
        # Manejo de error en caso de que el archivo no exista<a data-citation-id="01a15aa5-d69d-7066-9b2d-aa175b713035" class="source-message-chip source-message-chip-node color-document" ><span class="dis-none source-message-chip-id" >01a15aa5-d69d-7066-9b2d-aa175b713035</span><i class="icon-document"></i></a>,<a data-citation-id="c8ebfcbd-ae66-4ad0-a0cf-50bf11e0adcc" class="source-message-chip source-message-chip-chunk" ><span class="dis-none source-message-chip-id" >c8ebfcbd-ae66-4ad0-a0cf-50bf11e0adcc</span>5</a>
        print("Error: El archivo wordlist.txt no fue encontrado.")
        return None