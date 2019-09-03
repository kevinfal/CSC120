"""
    File: classify.py
    Author: Kevin Falconett
    Function: determines whether the first letter of a word
        is a vowel, consonant, or neither
"""
if __name__ == "__main__":
    string = input("input: ")  # retrieve input

    vowels = ["A", "E", "I", "O", "U"]  # list of vowels
    consonants = [
        "B",
        "C",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "V",
        "X",
        "Z",
        "W",
        "Y",
    ]  # list of consonants
    first = string[0].upper()  # first character made uppercase

    # conditionals
    if first in vowels:  # character is a vowel
        print("vowel")
    elif first in consonants:  # character is a consonant
        print("consonant")
    else:  # character is neither
        print("neither")
