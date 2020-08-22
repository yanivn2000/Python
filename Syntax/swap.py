# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# simple
#temp = x
#x = y
#y = temp

#pyhon simple construct to swap variables. 
x, y = y, x

print("x =", x)
print("y =", y)

#If the variables are both numbers, we can use arithmetic operations to do the same
#Addition and Subtraction
x = x + y
y = x - y
x = x - y

print("x =", x)
print("y =", y)
#Multiplication and Division
x = x * y
y = x / y
x = x / y

print("x =", x)
print("y =", y)
#This algorithm works for integers only
x = int(x)
y = int(y)
x = x ^ y
y = x ^ y
x = x ^ y

print("x =", x)
print("y =", y)