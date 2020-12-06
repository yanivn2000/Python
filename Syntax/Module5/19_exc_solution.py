
class MyClass:
    numberOfIntances = 0

    def __init__(self):
        MyClass.numberOfIntances += 1

    def __del__(self):
        MyClass.numberOfIntances -= 1

    @classmethod
    def get_number_of_instances(cls):
        return cls.numberOfIntances

print(MyClass.numberOfIntances)
print(MyClass.get_number_of_instances())
m1 = MyClass()
print(MyClass.numberOfIntances)
print(MyClass.get_number_of_instances())
m2 = MyClass()
print(MyClass.numberOfIntances)
print(MyClass.get_number_of_instances())
m3 = MyClass()
print(MyClass.numberOfIntances)
print(MyClass.get_number_of_instances())
