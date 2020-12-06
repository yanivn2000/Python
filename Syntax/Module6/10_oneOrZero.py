from findMatch import find_match

#optionl a-z. char, optional 0-9, end
find_match('^[a-z]?.[0-9]?$', '', 1) # N
find_match('^[a-z]?.[0-9]?$', 'a', 1) # Y
find_match('^[a-z]?.[0-9]?$', 'aa', 1) # Y
find_match('^[a-z]?.[0-9]?$', 'aa5', 1) # Y
find_match('^[a-z]?.[0-9]?$', 'aa55', 1) # N
