#!/usr/bin/env python3
import random

def get_random_word(filename="wordlist.txt"):
    """
    Lee el archivo de texto y devuelve una palabra al azar.
    Permite palabras con espacios y guiones.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Leemos líneas, quitamos espacios en blanco y descartamos las vacías
            words = [line.strip() for line in file if line.strip()]
        
        if not words:
            return None
        return random.choice(words).lower()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'.")
        return None

def get_user_input(game):
    """
    Solicita una letra al usuario y valida que sea una sola letra alfabética
    y que no haya sido usada antes.
    """
    while True:
        guess = input("\nAdivina una letra: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Entrada inválida. Por favor, ingresa solo una letra.")
            continue

        if guess in game.guessed_letters:
            print(f"Ya habías usado la letra '{guess}'. Intenta con otra.")
            continue

        return guess

def show_game_status(game):
    """Muestra el progreso de la palabra y las estadísticas actuales."""
    print("\n" + "="*40)
    print(f"Palabra: {game.display_progress()}")
    print(f"Intentos fallidos: {game.errors} / {game.max_errors}")
    print(f"Letras probadas: {', '.join(game.guessed_letters)}")
    print("="*40)