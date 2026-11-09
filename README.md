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

# Hangman Project — Descripción por archivos

1. wordlist.txt

Es un archivo de texto que contiene la lista de palabras disponibles para el juego, cada palabra está en una línea distinta:

elephant
tortuga
gato
pez
perro
vaca
oveja
cordero
chancho jabali
pez espada

Es el "banco de palabras" del juego: al inicio, el programa elige una al azar.
Solo se aceptan palabras con letras (las que tienen números o símbolos, el programa las descarta).


2. utils.py

Es un módulo que se encarga de obtener la palabra secreta. Tiene una sola función:

get_random_word()

Lo que hace:

Abre wordlist.txt.

Lee línea por línea y elimina los espacios en blanco con strip().

Solo deja pasar las líneas que sean solo letras (isalpha()).

Guarda esas palabras en una lista.

Elige una al azar con random.choice().

Si la lista está vacía, retorna None.

Si el archivo no existe, captura el error e imprime un mensaje, retornando None.

En resumen: lee el archivo, filtra las palabras válidas y devuelve una al azar.

3. game.py

Es el módulo más importante. Contiene la clase HangmanGame, que guarda el estado del juego y tiene los métodos para jugarlo.

Clase HangmanGame

Al crear una partida se pasa la palabra secreta y la clase inicializa:

self.word → la palabra objetivo, en minúsculas.
self.guessed_letters → lista de letras que el jugador ya ha dicho.
self.max_errors → límite de errores, son 6.
self.errors → contador de errores que ya falló el jugador.
Métodos:

display_progress(): muestra la palabra con las letras adivinadas reveladas y las otras como guiones bajo. Además, deja visibles los caracteres que no son letras, como espacios o guiones.

process_guess(letter): recibe una letra del jugador. Si la letra sí está en la palabra, se guarda en guessed_letters y retorna True. Si no, suma un error en errors y retorna False.

is_won(): retorna True si todas las letras de la palabra están en guessed_letters.

is_lost(): retorna True si el número de errores llegó o superó los 6.

En resumen: esta clase guarda todo lo que necesita el juego (palabra, letras acertadas, errores) y contiene la lógica de todos los movimientos.

4. main.py

Es el módulo de interacción con el usuario. Aquí está el programa principal y el bucle del juego.

Funciones:

get_user_input(game): pide al jugador que escriba una letra. Valida que sea exactamente una letra, que sea alfabética (sin números ni símbolos) y que no se haya repetido antes. Si no cumple alguna regla, muestra un mensaje de error y pide otra. Solo retorna cuando la entrada es válida.

show_game_status(game): imprime el estado del juego: el progreso de la palabra, las letras ya adivinadas y los intentos restantes (max_errors - errors).

# main(): es la función que orquesta todo el juego:

Llama a get_random_word() para obtener la palabra secreta.

Si no hay palabra, muestra un error y termina.

Crea un objeto HangmanGame con la palabra.

Entra en un bucle que se repite mientras los errores sean menores a 6 y queden guiones en la palabra.

En cada vuelta, muestra el estado, pide una letra y procesa la respuesta.

Cuando termina el bucle, muestra si ganó o perdió y revela la palabra.

El bloque if __name__ == "__main__": asegura que main() solo se ejecute si se corre el archivo directamente, y no si se importa como módulo.
