#Function that get a parameter to print number of
#numbers to print from the fibonacci series
#For example if function gets 6 it will print:
# #1, 1, 2, ,3, 5 ,8

def gen_fib(n):
    i = 1
    if n == 0:
        fib = []
    elif n == 1:
        fib = [1]
    elif n == 2:
        fib = [1,1]
    elif n > 2:
        fib = [1,1]
        while i < (n - 1):
            fib.append(fib[i]+ fib[i-1])
            i += 1
    return fib

