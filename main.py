#!/usr/bin/env python3

from utils import get_random_word, get_user_input, show_game_status
from game import HangmanGame

def main():
    # 1. Preparación: Cargar palabra
    secret_word = get_random_word()
    if not secret_word:
        print("No se pudo iniciar el juego. Verifica tu archivo wordlist.txt.")
        return

    # 2. Inicialización
    game = HangmanGame(secret_word)
    print("¡Bienvenido al Ahorcado!")

    # 3. Bucle de juego
    while not game.is_over():
        show_game_status(game)
        guess = get_user_input(game)
        
        if game.make_guess(guess):
            print(f"¡Bien! La letra '{guess}' está en la palabra.")
        else:
            print(f"Lo siento, la letra '{guess}' no está.")

    # 4. Finalización
    show_game_status(game)
    if game.is_won():
        print("\n¡FELICIDADES! Has adivinado la palabra.")
    else:
        print(f"\n¡GAME OVER! Te has quedado sin intentos.")
        print(f"La palabra era: {game.word}")

if __name__ == "__main__":
    main()