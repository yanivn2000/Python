#slide 22
import fibonacci # use default namespace "fibonacci"
import fibonacci as fi #use alias

print(fibonacci.gen_fib(6))
print(fi.gen_fib(6))