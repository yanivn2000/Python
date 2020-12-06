#slide
#re.X - in order to add comments
import re

m = re.search(r'\d+\.\d*', "1.23")

# very clear way to explain the regx
m = re.search(r"""\d + # the integral part
                  \.   # the decimal point
                  \d * # some factional digits""", "1.23", re.X)

print(m.group())
