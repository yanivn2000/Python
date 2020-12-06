class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self._grade = grade

    def get_grade(self):
        return self._grade

    def __str__(self):
        return f"{self.get_name()}'s grade is {self.get_grade()}"


s1 = Student("Yaniv", 95)
print((s1))  # Yaniv's grade is 95
s2 = Student("Bob", 89)
print((s2))  # Bob's grade is 89
