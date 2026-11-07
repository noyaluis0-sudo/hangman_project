#!/usr/bin/env python3

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
        # Manejo de error en caso de que el archivo no exista<a

        print("Error: El archivo wordlist.txt no fue encontrado.")

        return None
