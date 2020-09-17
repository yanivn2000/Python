# Create a program that receives val+val+val and prints the sum

inputString=input("Please insert a string:")
list = inputString.split('+')
sumOfNumbers=0
for i in list:
    sumOfNumbers+=int(i)

print(f"{inputString}={sumOfNumbers}")
