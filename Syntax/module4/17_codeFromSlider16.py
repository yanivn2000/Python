glob=10

#local variable override the global, therefore the error
def func():
    glob=11
    print(f"in func: {glob}")
    print(f"in func: {glob}")

func()
print(f"in main: {glob}")
