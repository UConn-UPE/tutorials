#Boolean and Conditional Operators in Python:
#
#True
#False
#None
#
#Not
#Empty sequences: lists, strings, tuples
#Empty mappings: dictionaries
#Comparison Operators: <, >, >=, <=
#Mutiple Operators using: and, or


#Conditional Setup
"""
if <condition statement>:
    "then do whatever you would do now that the condition is true"
else:
    "do whatever you would now that the condition is false"
"""

#True, False, Null Example

'''
example = False

if example == True:
    print("the statement is true")
elif example == None:
    print("the state is None")
else:
    print("the statement is not none or true")
'''

#Not / Negation

'''
num = 1

if num != 10:
    print("example is not equal to 10")
else:
    print("example is equal to 10")



example = False

if not True:
    print("example is False, so the not of False is True")
else: 
    print("example is True, so the not of True is False")
'''

#Empty sequences / Empty Mappings

'''
item = [1]

if item:
    print("There is something in the item")
else:
    print("The item is empty")
'''

#Comparison Operators

'''
num1 = 4
num2 = 10
num3 = 4

if num1 < num3:
    print("num2 is greater than num1")
else:
    print("num1 is greater than num2")
'''

#Multiple conditions


a = 1
b = 2
c = 3
d = True

if a == b or c != d:
    print("a and b are not equal and b and c are not equal")
else:
    print("a and b are equal and b and c are equal")

