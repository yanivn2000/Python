#calculate the average until it gets 'q'
n=input("Insert a number: ")
sumOfNumbers=0
count=0
while n != 'q':
    sumOfNumbers+=int(n)
    count += 1
    n = input("Insert a number or q to quit: ")
avg=sumOfNumbers / count
print(avg)
