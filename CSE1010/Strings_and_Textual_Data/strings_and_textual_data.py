# Basic Hello World print statement
g = 'Hello World'
print(g)



# Printing with Double and Signle Quotes

# error in defining string variable
# greeting = 'Welcome to Michael's Video'

# one method to correct string
greeting = 'Welcome to Michael\'s Video'
print(greeting)

# another method to correct string
greeting = "Welcome to Michael's Video"
print(greeting)




# indexing and slicing slicing a String
greeting = 'Hello World'

# print the final character of string
print(greeting[10])

# also prints the final character of string
print(greeting[-1])

# index error if index DNE
# print(greeting[10000])

# slice Hello
print(greeting[:5])

# slice World
print(greeting[6:])





# String methods
greeting = 'Hello World'

# print all lowercase
print(greeting.lower())

# print all uppercase
print(greeting.upper())

# count number of occurences
print(greeting.count('Hello'))

# find index of first occurence
print(greeting.find('Hello'))





# String Concatenation
name = 'Michael'
action = 'is making a tutorial'

# method 1
message = name + ' ' + action
print(message)

# formatted string
message = '{}, a member of UPE, {}'.format(name, action)
print(message)

# f string method for Python 3.6 +
message = f'{name}, a member of UPE, {action}'
print(message)





# find methods associated with object
print(dir(message))

# print help documentation for join method on string
print(help(str.join))
