#slide 8
import re

for m in re.finditer('[a-z]', "Yaniv"):
    print(m.group())
# a
# n
# i
# v

print()
for m in re.finditer('[A-Z]', "Yaniv", re.I):
    print(m.group())

# Y
# a
# n
# i
# v