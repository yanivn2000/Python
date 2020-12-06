#slide 5
from findMatch import find_match

#\s - white space
#\S - not white space
find_match(r'\s$', ' ', 1) # Y
find_match(r'\s$', 'a', 2) # N
find_match(r'\S$', ' ', 3) # N
find_match(r'\S$', 'a', 4) # Y
