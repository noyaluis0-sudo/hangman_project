# Juego del Ahorcado/Hangman

1. ¿De qué trata el juego?

La idea principal del juego es encontrar la palabra oculta, intentando adivinarla letra por letra antes de quedarte sin intentos.

2. ¿Cómo se juega?

  - Al inicio aparece un una palabra oculta representada por guiones bajos (_ _ _ _) que corresponden a las letras correspondientes. 
  - En cada turno, debes de escribir una letra y dar Enter. No puedes utilizar símbolos ni números, solo se aceptan letras y no se pueden repetir. 
  - Si la letra que escribiste pertenece a la palabra, aparecerá en todas las posiciones de la palabra donde aparece (por ejemplo _ a _ a _ _ _)
  - Si la letra no pertenece a la palabra, cuenta como un error y lo podrás ver en el contador. Tienes un máximo de 6 errores, si llegas a 6 pierdes y verás la palabra oculta.
  - Podrás ir viendo el progreso de la partida, incluyendo: el progreso de la palabra, las letras que ya adivinaste y los intentos que te quedan.
  - Ganas el juego si logras completar la palabra antes de llegar a 6 errores. 

# Estructura del proyecto

El proyecto está organizado en módulos que separan la lógica del juego, las funciones auxiliares y la ejecución principal del programa.

1. main.py: Es el punto de entrada del programa. Importa los módulos utils y game. Se encarga de coordinar el desarrollo de la partida. Su función principal es main(), que inicializa el juego, gestiona los intentos y determina el resultado final.

2. game.py: Contiene la clase HangmanGame, responsable de administrar la lógica del juego. Sus métodos principales son:
   - init(): Inicializa la partida y sus atributos.
   - display_progress(): Muestra el progreso de la palabra.
   -  make_guess(): Procesa los intentos del jugador.
   -  is_won(): Comprueba si el jugador adivinó la palabra.
   -  is_over(): Determina si la partida terminó.

3. utils.py: Contiene funciones auxiliares e importa el módulo random para seleccionar palabras aleatorias. Sus funciones principales son:
   - get_random_word(): Obtiene una palabra aleatoria desde el archivo de palabras.
   - get_user_input(): Solicita y valida las letras ingresadas por el usuario.
   - show_game_status(): Muestra el estado actual de la partida y las estadísticas.
   
4. wordlist.txt
Es un archivo de texto que contiene las palabras que se van a utilizar en el juego, contiene 50 peliculas, aquellas que tienen mas de una palabra estan separadas por un guion.\\















El bloque if __name__ == "__main__": asegura que main() solo se ejecute si se corre el archivo directamente, y no si se importa como módulo.
