x=1
x=2
y=x
x=3

#x -> 1
#x -> 2 (1 waits for the GC!)
#y -> 2 <- x
#x -> 3

#Note: 1, 2, 3, are immutable, this is wy above does not override them!
#like string in C#