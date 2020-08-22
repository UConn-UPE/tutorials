## SLICING LISTS

#          0     1    2    3    4    5    6    7    8    9   *positive 
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#          -10  -9   -8   -7   -6   -5   -4   -3   -2   -1   *negative

# Print single elements in a list using positive and negative indexes
print(letters[4])
print(letters[-1])
print(letters[-6])

# Notation to slice a list: letters[start:stop:step]

# Print letters 'a' through ' f'
print(letters[0:6])

# Print letters 'd', 'e', 'f'
print(letters[3:6])

# Combining positive and negative indexes
print(letters[3:-4])

# Print letters from a starting index to the end of the list
print(letters[1:])
print(letters[-2:])

# Print letters from the beginning of the list up until a stopping index
print(letters[:7])

# Print entire list
print(letters[:])

# Print letters 'b' through 'h' with step value of 2
print(letters[1:8:2])

# Print letters 'i' to 'c' with step value of 2 in reverse
print(letters[8:1:-2])

# Print letters 'i' to 'c' in reverse
print(letters[8:1:-1])

# Print entire list in reverse
print(letters[::-1])


## SLICING STRINGS

dessert = "cheesecake"
print(dessert)

# Reverse string
print(dessert[::-1])

# Print 'cake'
print(dessert[-4:])

# Print 'cheese'
print(dessert[:6])

# Print 'eese'
print(dessert[2:6])
