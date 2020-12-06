from findMatch import find_match

#starts with a, then optional b, then c ends the string
find_match('^[A-Z]+', '', 1) # N
find_match('^[A-Z]+', 'c', 1) # N
find_match('^[A-Z]+', 'A', 1) # Y
find_match('^[A-Z]+', 'ABBFAb', 1) # Y
