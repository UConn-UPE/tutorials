#The superclass or parent class
class Husky:
    def __init__(self, name, email, year):
        self.name = name
        self.email = email
        self.year = year
    def getDescription(self):
        return f'{self.name} graduates in {self.year}.'
    def getFullDescription(self):
        return self.getDescription() + " Email them at " + self.email

# The subclass or child class.
class EngineeringStudent(Husky):
    def __init__(self, name, email, year, major):
        #Run our superclass' init methods, then add our own.
        super().__init__(name, email, year)
        self.major = major
    def complain(self):
        print("My major is so haarrrd :(")
    def getDescription(self):
        # Overwrites the old description class.
        # We can still refer to the old method with super.
        return super().getDescription() + " They are an engineering student"
    

student_1 = EngineeringStudent("finn", "finn@uconn.edu", 2022, "CS")
student_2 = EngineeringStudent("mike", "mike@uconn.edu", 2021, "CS")

# Properties defined in Husky are usable!
print(student_1.name)
# Old methods from Husky are still available to use!
print(student_2.getFullDescription())
# Our complain method works
student_1.complain()
