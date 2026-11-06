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
        Construye y devuelve el estado actual de la palabra (ej. "_ _ e _ _ a _ _").
        """
        display = []
        
        # Bucle para construir la palabra oculta basándose en las letras adivinadas<a data-citation-id="e865c382-9828-4de0-9f34-08f9035bb83b" class="source-message-chip source-message-chip-chunk" ><span class="dis-none source-message-chip-id" >e865c382-9828-4de0-9f34-08f9035bb83b</span>2</a>
        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        
        # Unir los caracteres con espacios para mejorar la visualización
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
    