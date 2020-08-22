#Our first function
def fancy_hello():
    print("~~~Hello!~~~")
    
#Running the function
fancy_hello()

#Accepting an argument to our function
def fancy_message(msg):
    print("~~~" + msg + "~~~")

fancy_message("Python Rocks!")

## Return Values
#A celcius to Farenheit converting function, using "return"
def c_to_f(cel):
    far = (1.8 * cel) + 32
    return far
#Using returned values
x = c_to_f(100)
print(x)
# OR
print(c_to_f(0))

#Another example: Multiple return statements can make consice code!
def is_negative(x):
    if x < 0:
        return True
    # I'm omitting an else statement here on purpose.
    # if "True" is returned, the function is done!
    return False

print(is_negative(1))
print(is_negative(-1))

## Array Functions: Can be a little tricky!
def fruity_function(fruit_list):
    fruit_list.append("kiwi")
    print(fruit_list)

fruits = ['apple','banana','tomato']

print(fruits) #['apple','banana','tomato']
fruity_function(fruits) #['apple','banana','tomato', 'kiwi'] Makes sense?
print(fruits) #['apple','banana','tomato', 'kiwi'] What the heck happened?

## Default Values:
# Our 'fancy function' with default values for each 
def fancy_string(msg = "Hello!", design = "~~~"):
    return design + msg + design

print(fancy_string("Python Rocks!", ".-.-.-."))
#Specifying ONLY the second value of our function that uses default values
print(fancy_string(design = ".-.-."))
