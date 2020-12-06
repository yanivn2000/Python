from findMatch import find_match

#starts with a, then optional b, then c ends the string
find_match('^ab*c$', 'ac', 1) # Y
find_match('^ab*c$', 'abc', 2) # Y
find_match('^ab*c$', 'abbbbc', 3) # Y
find_match('^ab*c$', 'ababc', 4) # N
