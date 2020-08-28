# The Class Definiton
class Husky:
    # __init__, a magic method, runs whenever a new instace is declared.
    def __init__(self, name, email, year):
        # Self refers to the specific "instance" of a class.
        # We create "instance variables", or attributes.
        self.name = name
        self.email = email
        self.year = year
    # getDescription takes an instance's attributes
    # and uses them.
    def getDescription(self):
        return f'{self.name} graduates in {self.year}.'
    # getFullDescription takes an instance's attributes
    # and methods and acts upon them.
    def getFullDescription(self):
        return self.getDescription() + " Email them at " + self.email

class EngineeringStudent(Husky):
    pass

#The Instance Declarations
student_1 = EngineeringStudent("finn", "finn@uconn.edu", 2022)
student_2 = EngineeringStudent("mike", "mike@uconn.edu", 2021)
