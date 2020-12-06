#slide
#re.S - multi line
import re

txt = """Yaniv
Nuriel"""

# the new line cuts the string
m = re.search('.+', txt)
print(m.group())
# Yaniv

print()
# re.S - Multiline
m = re.search('.+', txt, re.S)
print(m.group())

# Yaniv
# Nuriel
