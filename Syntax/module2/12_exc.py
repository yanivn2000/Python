#print the number of choices to pick K numbers from group of N numbers
#Lottory! 37 & 6 + strong number (1-7)
#N - the range: 37
#k - the number of correct selections: 6
#strong number: 1-7
#The math: (strong number) * (fact(N) // (fact(K) * fact(N-K)))
# math.factorial

import math
from math import factorial as fact

n=int(input("Please enter the range of numbers:"))
k=int(input("Please enter the number of balls to pick:"))
s=int(input("Please enter the number of strong numbers range:"))

factN=fact(n)
factK=math.factorial(k)
factNK=math.factorial(n-k)
result=s*(factN // (factK *factNK))
print(f'The number of choice are: {result}')