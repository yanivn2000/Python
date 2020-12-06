#slide 8
import re

txt = '1a2b3c'

res = re.sub(r'\d','?', txt)
print(txt) # 1a2b3c
print(res) # ?a?b?c

#sub only the first 2 cases
res = re.sub(r'\d','?', txt, 2)
print(res) # ?a?b3c

res = re.sub(r'A','?', txt, 2)
print(res) # 1a2b3c