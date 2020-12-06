#slide 8
import re

txt = '11a22b33c'

# search a specific
m = re.search(r'\d+', txt)
print(f"{m.group()} {m.start()} {m.end()}") # 11 0 2

print()
#get group of items
res = re.finditer(r'\d+', txt)
for m in res:
    print(f"{m.group()} {m.start()} {m.end()}")

# 11 0 2
# 22 3 5
# 33 6 8

