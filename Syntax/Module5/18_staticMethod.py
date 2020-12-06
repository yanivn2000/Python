#Class variable
#C::myClassVariable = 1
class C:
    myClassVariable = 1

    @classmethod
    def f(cls): #cls access class variables
        return cls.myClassVariable


    def g(self): #self access cls and instance variables
        self.x = 5
        self.__can_not_see_me();
        return self.myClassVariable

    def __can_not_see_me(self):
        print("did you?!?")

print(C.f())
c1 = C()
print(c1.g())
print(c1.f())

c1.__can_not_see_me()


