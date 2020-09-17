#read a number from the user-n
#create a dictionary with keys from 0 to n-1 and values of key*key

n=int(input("Input a number: "))
d={}

for x in range(n):
    d[x]=x*x

print(d)