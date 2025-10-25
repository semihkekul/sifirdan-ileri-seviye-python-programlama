class Person():
    def __init__(self,name):
        print("Person __init__", name)

class Student(Person):
    pass

class Worker(Person):
    # overriding
    def __init__(self, name):
        print("Worker __init__", name)

p1 = Person("Semih")
# Person __init__ Semih
s1 = Student("Mete")
# Person __init__ Mete
w1 = Worker("Arzu")
# Worker __init__ Arzu
