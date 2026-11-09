#!/usr/bin/env python3

class HangmanGame:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """
        Genera la cadena a mostrar. Los caracteres que no son letras
        (guiones, espacios) se muestran automáticamente.
        """
        display = []
        for char in self.word:
            if char.isalpha():
                if char in self.guessed_letters:
                    display.append(char)
                else:
                    display.append("_")
            else:
                # Se muestra automáticamente si es espacio, guion, etc.
                display.append(char)
        return " ".join(display)

    def make_guess(self, letter):
        """Procesa el intento del jugador y actualiza los errores."""
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.errors += 1
            return False
        return True

    def is_won(self):
        """Verifica si todas las letras alfabéticas han sido adivinadas."""
        for char in self.word:
            if char.isalpha() and char not in self.guessed_letters:
                return False
        return True

    def is_over(self):
        """El juego termina por victoria o por exceso de errores."""
        return self.is_won() or self.errors >= self.max_errors
