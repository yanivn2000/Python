#function gets a list of number
#and return a NEW list only with its even values

def find_Even(l):
    even = []
    for n in l:
        if n % 2 == 0:
            even.append(n)
    return even

print(find_Even([1,2,3,4,5,6,7,8,9]))