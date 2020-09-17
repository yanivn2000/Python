#Find if a number is prime number
#if the number is a prime number print: "Prime number"
#Otherwise orint "Not a prime number" + print 2 numbers it is diveded by
#e.g.
#Please enter a number: 35
#35 is not a prime number
#5 times 7 is 35
#OR
#Please enter a number: 23
#23 is a prime number

num=int(input("Plase enter a number: "))
found = -1

for i in range(2, num):
    if (not (num % i)):
        found = i
        break

if found != -1:
    print(f"{num} is not a prime number")
    print(f"{found} times {num // found} is {num}")
else:
    print(f"{num} is a prime number")

