#slide
#re.M - multi line
import re

txt = """Yaniv
Nuriel"""

for m in re.finditer('^[A-z][a-z]', txt):
    print(m.group())
# Ya

print()
# re.M - Multiline
for m in re.finditer('^[A-z][a-z]', txt, re.M):
    print(m.group())

# Y
# a
# n
# i
# v