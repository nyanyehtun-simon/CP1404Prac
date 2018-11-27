"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

word_format = "ccvcvvc"
word = ""

word_format = input('Enter the word format % (for CONSONANTS) or # (for VOWELS)?: ').lower()

for kind in word_format:
    if kind == "%":  # % for consonants
        word += random.choice(CONSONANTS)
    elif kind == '#':  # # for vowels
        word += random.choice(VOWELS)
    elif kind == '*':  # * for any alphabets
        word += random.choice(ALPHABETS)
    elif ALPHABETS.find(kind) >= 0:  # if specific characters are provided
        word += kind

print(word)