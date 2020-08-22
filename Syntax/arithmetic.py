# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)
sub = float(num1) - float(num2)
mul = float(num1) * float(num2)
div = float(num1) / float(num2)
intDiv = float(num1) // float(num2)
mod = float(num1) % float(num2)
pow = float(num1) ** float(num2)

# Display the sum
#print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print(f'The sum of {num1} and {num2} is {sum}')
print(f'The sub of {num1} and {num2} is {sub}')
print(f'The div of {num1} and {num2} is {div}')
print(f'The int div of {num1} and {num2} is {intDiv}')
print(f'The mul of {num1} and {num2} is {mul}')
print(f'The mod of {num1} and {num2} is {mod}')
print(f'The pow of {num1} and {num2} is {pow}')

#Alternative to this, we can perform this addition in a single statement without using any variables as follows.
#print('The sum is %.3f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

if (float(num1) % 2) == 0:
   print(f"{num1} is Even")
else:
   print(f"{num1} is Odd")
