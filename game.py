#!/usr/bin/env python3

class HangmanGame:
    def __init__(self, word):
        """
        Inicializa el estado del juego del ahorcado.
        """
        self.word = word.lower()           # La palabra objetivo
        self.guessed_letters = []          # Lista de letras adivinadas
        self.max_errors = 6                # Límite máximo de errores
        self.errors = 0                    # Contador de respuestas incorrectas

    def display_progress(self):
        """
        Muestra la palabra revelando letras adivinadas y dejando 
        visibles automáticamente los caracteres que NO son letras (guiones, espacios, etc.).
        """
        display = []
        for char in self.word:
            # 1. Si es una letra alfabética, comprobamos si ya fue adivinada
            if char.isalpha():
                if char in self.guessed_letters:
                    display.append(char)
                else:
                    display.append("_")
            # 2. Si NO es una letra (espacio, guion, número), se muestra directamente
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
    