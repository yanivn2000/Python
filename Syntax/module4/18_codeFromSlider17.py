glob=10

#local variable override the global, therefore the error
def func():
    global glob
    print(f"in func: {glob}")
    glob=11
    print(f"in func: {glob}")

func()
print(f"in main: {glob}")
