#function gets a list of numbers
#and return a NEW list only with its even values
#[1,2,3,4,5,6,7,8,9]
#[2,4,6,8]


def find_Even(l):
    even = []
    for n in l:
        if n % 2 == 0:
            even.append(n)
    return even

l=[1,2,3,4,5,6,7,8,9]
print(find_Even(l))
print(l)