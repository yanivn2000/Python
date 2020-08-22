# Solve the quadratic equation ax**2 + bx + c = 0
#https://docs.python.org/3/library/math.html

# import complex math module
import math

number=float(input("Please enter a number: "))
# find two solutions
sqrt=math.sqrt(number)
pow=math.pow(number,2)
log=math.log(number)
ceil=math.ceil(number)
floor=math.floor(number)


print(f'The sqrt is {sqrt}')
print(f'The pow is {pow}')
print(f'The log is {log}')
print(f'The ceil is {ceil}')
print(f'The floor is {floor}')
