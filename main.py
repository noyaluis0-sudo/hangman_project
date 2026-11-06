from utils import get_random_word
from game import HangmanGame

def get_user_input(game):
    """
    Solicita una letra al usuario y la valida.
    Asegura que sea una sola letra, alfabética y no repetida.
    """
    while True:
        guess = input("Ingresa una letra: ").lower().strip()

        # Validar que sea una sola letra y alfabética
        if len(guess) != 1 or not guess.isalpha():
            print("Error: Por favor, ingresa solo una letra (sin números ni símbolos).")
            continue

        # Validar que no se haya intentado antes (incluyendo fallos y aciertos)
        # Nota: En HangmanGame, podrías querer guardar también las letras fallidas
        # para esta validación, o simplemente verificar en guessed_letters.
        if guess in game.guessed_letters:
            print(f"La letra '{guess}' ya la habías dicho. Prueba con otra.")
            continue

        return guess

def show_game_status(game):
    """
    Muestra el estado visual del juego: progreso, letras usadas y errores.
    """
    print(f"\nProgreso: {game.display_progress()}") #<a data-citation-id="e865c382-9828-4de0-9f34-08f9035bb83b" class="source-message-chip source-message-chip-chunk" ><span class="dis-none source-message-chip-id" >e865c382-9828-4de0-9f34-08f9035bb83b</span>3</a>
    
    intentos = ", ".join(game.guessed_letters) if game.guessed_letters else "Ninguna"
    print(f"Letras adivinadas: {intentos}")
    
    intentos_restantes = game.max_errors - game.errors
    print(f"Intentos restantes: {intentos_restantes}")
    print("-" * 30)

def main():
    # 1. Obtener una palabra aleatoria de utils.py
    target_word = get_random_word()
    
    if not target_word:
        print("Error: No se pudo cargar ninguna palabra. Revisa wordlist.txt.")
        return

    # 2. Inicializar el juego
    game = HangmanGame(target_word)
    print("¡Bienvenido al juego del Ahorcado!")

    # 3. Bucle principal del juego
    # El juego sigue mientras no se superen los errores y queden guiones por completar
    while game.errors < game.max_errors and "_" in game.display_progress():
        show_game_status(game)
        
        letra = get_user_input(game)
        
        if game.process_guess(letra):
            print(f"¡Excelente! La letra '{letra}' está en la palabra.")
        else:
            print(f"Lo siento, la letra '{letra}' no se encuentra.")

    # 4. Resultado final
    if "_" not in game.display_progress():
        print(f"\n¡Felicidades! Has ganado. La palabra era: {game.word}")
    else:
        print(f"\nGame Over. Te has quedado sin intentos.")
        print(f"La palabra secreta era: {game.word}")

if __name__ == "__main__":
    main()