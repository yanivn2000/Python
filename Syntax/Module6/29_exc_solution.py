#slide 8
import re

def find_words(txt):
    for m in re.finditer('[A-Z][a-z]{2,}', txt):
        print(m.group())

find_words("My name is Amir Adler an I teach you Python")