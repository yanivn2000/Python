import re

def find_match(pattern, string, index):
    x = re.search(pattern, string)

    if x:
        print(f"{index} - Match")
    else:
        print(f"{index} - No Match")

#period here is new line
find_match('^.', '.a', 1) # Y
find_match('^.', 'ab', 2) # Y
#period here is period
#\ is a special caracter therefore we need r to avoid \\
find_match(r'^\.', 'ba', 3) # N
find_match(r'^\..', '.a', 4) # Y
