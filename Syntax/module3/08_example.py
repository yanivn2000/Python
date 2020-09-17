import math

i = 5

print("The program will print square root of 5 non-negative (0 to exit)")
while i:
    s = input("Enter a number:")
    num = int(s)
    if num == 0:
        break
    if num < 0:
        continue
    i -= 1
    print(math.sqrt(num))
