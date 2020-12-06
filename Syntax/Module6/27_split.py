#slide 8
import re

#"2004-10-09;Yaniv;Nuriel;44""
txt1 = 'a1b2c3'
txt2 = '1a2A3'

res = re.split(r'\d', txt1)
print(res) # ['a', 'b', 'c', '']

#1 split only!
res = re.split(r'\d', txt1, 1)
print(res) # ['a', 'b2c3']

res = re.split(r'[a-z]', txt2)
print(res) # ['1', '2A3']

res = re.split(r'[a-z]', txt2, flags=re.IGNORECASE)
print(res) # ['1', '2', '3']