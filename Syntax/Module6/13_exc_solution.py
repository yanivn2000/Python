from findMatch import find_match

find_match('^([A-Z][a-z]){2,}$', '', 1) # N
find_match('^([A-Z][a-z]){2,}$', 'Aa', 2) # N
find_match('^([A-Z][a-z]){2,}$', 'AaAa', 3) # Y
find_match('^([A-Z][a-z]){2,}$', 'AaAaAa', 4) # Y
find_match('^([A-Z][a-z]){2,}$', 'AAaa', 5) # N
find_match('^([A-Z][a-z]){2,}$', 'aa', 6) # N
