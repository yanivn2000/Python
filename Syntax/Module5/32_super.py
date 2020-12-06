#Slide 14
#call parent

class C:
    def f1(self):
        print("C.f1")


class D(C):
    x = 2 #member override

    def f1(self): #method override
        super().f1() #call parent
        print("D.f1")


d1 = D() #C.f1
d1.f1() #D.f1
