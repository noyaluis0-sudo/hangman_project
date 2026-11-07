#!/usr/bin/env python3

class HangmanGame:
    def __init__(self, word):
        """
        Inicializa el estado del juego del ahorcado.
        """
        self.word = word.lower()           # La palabra objetivo
        self.guessed_letters = []          # Lista de letras adivinadas<a data-citation-id="01a15ab8-6711-7193-91f8-6d68c01fb6a6" class="source-message-chip source-message-chip-node color-note source-message-chip-note" ><span class="dis-none source-message-chip-id" >01a15ab8-6711-7193-91f8-6d68c01fb6a6</span><i class="icon-note"></i></a>
        self.max_errors = 6                # Límite máximo de errores
        self.errors = 0                    # Contador de respuestas incorrectas

    def display_progress(self):
        """
        Muestra la palabra revelando letras adivinadas y dejando 
        visibles automáticamente los caracteres que NO son letras (guiones, espacios, etc.).
        """
        display = []
        for char in self.word:
            # 1. Si es una letra alfabética, comprobamos si ya fue adivinada<a data-citation-id="24b53d41-3198-4a68-ace6-c528d34c1b68" class="source-message-chip source-message-chip-chunk" ><span class="dis-none source-message-chip-id" >24b53d41-3198-4a68-ace6-c528d34c1b68</span>1</a>
            if char.isalpha():
                if char in self.guessed_letters:
                    display.append(char)
                else:
                    display.append("_")
            # 2. Si NO es una letra (espacio, guion, número), se muestra directamente<a data-citation-id="e865c382-9828-4de0-9f34-08f9035bb83b" class="source-message-chip source-message-chip-chunk" ><span class="dis-none source-message-chip-id" >e865c382-9828-4de0-9f34-08f9035bb83b</span>2</a>
            else:
                display.append(char)
        
        # Unimos todo con espacios para que se vea claro en la consola
        return " ".join(display)
    
    def process_guess(self, letter):
        """
        Procesa la letra adivinada por el usuario.
        """
        letter = letter.lower()  # Asegurarse de que la letra esté en minúscula
        
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True  # Adivinanza correcta
        else:
            self.errors += 1
            return False  # Adivinanza incorrecta

    def is_won(self):
        """
        Verifica si el jugador ha ganado (todas las letras adivinadas).
        """
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        """
        Verifica si el jugador ha perdido (superó el número máximo de errores).
        """
        return self.errors >= self.max_errors
    