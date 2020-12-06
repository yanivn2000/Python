#slide 12
#The problem

class Foo:
    def __init__(self,x):
        self.x = x
        # x ==> bar instance

    def __del__(self):
        print("end of Foo")


class Bar:
    def __init__(self):
        self.foo = Foo(self)

    def __del__(self):
        print("end of Bar")


bar = Bar()
foo = Foo(bar)
bar = None #will not call the del
while True:
    pass