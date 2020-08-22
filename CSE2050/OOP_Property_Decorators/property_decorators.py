class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, new_name):
        first, last = new_name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print("Deleting name...")
        self.first_name = None
        self.last_name = None
    

st = Student("SpongeBob", "SquarePants")

st.full_name = "Patrick Star"

print(st.first_name)
print(st.email)
print(st.full_name)

del st.full_name
