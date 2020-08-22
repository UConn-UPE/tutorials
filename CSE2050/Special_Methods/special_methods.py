class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


# dunder (mifflin) methods = special methods for classes, default methods, methods that work under the hood, explicitly called, implicitly called depending on circumstance

# __init__ = called when new instance of a class created, initializes all the attributes of an object
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# __str__ = called when printing an object
# comment out __str__
print(emp_1)
# implement __str__
print(str(emp_1))
print(emp_1.__str__())
print(emp_1)

# __add__ = called when adding two objects
print(1+3)
print(int.__add__(1, 3))
# comment out __add__
print(emp_1 + emp_2)
# implement __add__
print(emp_1 + emp_2)

# __len__ = called when using len function on object
print(len('word'))
print('word'.__len__())
# comment out __len__
print(len(emp_1))
# implement __len__
print(len(emp_1))


