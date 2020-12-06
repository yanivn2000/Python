# This program adds two numbers
#https://www.w3schools.com/python/python_operators.asp

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# Store input numbers
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# Add two numbers
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 #keeps leftover
intDiv = num1 // num2
mod = num1 % num2
pow = num1 ** num2

# Display the sum
#print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print(f'The sum of {num1} and {num2} is {sum}')
print(f'The sub of {num1} and {num2} is {sub}')
print(f'The div of {num1} and {num2} is {div}')
print(f'The int div of {num1} and {num2} is {intDiv}')
print(f'The mul of {num1} and {num2} is {mul}')
print(f'The mod of {num1} and {num2} is {mod}')
print(f'The pow of {num1} and {num2} is {pow}')

print(f"{num1}+={num2} = ")
num1+=num2
print(f"...{num1}")

print(f"{num1}/3 = ")#divid like float (C#)
print(f"...{num1/3}")

print(f"{num1}//3 = ")#divid like int (C#)
print(f"...{num1//3}")


#Alternative to this, we can perform this addition in a single statement without using any variables as follows.
#print('The sum is %.3f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

if (num1 % 2) == 0:
   print(f"{num1} is Even")
else:
   print(f"{num1} is Odd")
