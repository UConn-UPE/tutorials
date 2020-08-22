# Our dictionary with key-value pairs
course = {"number":1010, "instructor":"Mickey", "materials":["pencil", "notebook"]}

# Print entire dictionary
print(course)

# Print value of one specific key
print(course["number"])
print(course["instructor"])
print(course["materials"])

# Keys can be any immutable data type (ex: integer)
course = {"number":1010, 20:"Mickey", "materials":["pencil", "notebook"]}
print(course[20])

### Set the key back to "instructor" for the following examples

# KeyError is thrown when we access a key that does not exist
print(course["time"])

# Use .get method to return "None" instead of a KeyError
print(course.get("time"))

# Change default return value from "None" to "Does not exist"
print(course.get("time", "Does not exist"))

# Add 'time' key to our dictionary
course["time"] = "10:00"

# Update the value of a key that already exists
course["instructor"] = "Minnie"

# Use .update method to make multiple changes in one line of code
course.update({"number":1000, "instructor":"Minnie", "time":"10:00"})

# Delete key-value pair
del course["materials"]

# Pop key-value pair
materials = course.pop("materials")
print(materials)

# Print number of keys in our dictionary
print(len(course))

# Print all keys in our dictionary
print(course.keys())

# Print all values in our dictionary
print(course.values())

# Print all key-value pairs in our dictionary
print(course.items())

# Loop through all key-value pairs in our dictionary
for key, value in course.items():
    print(key, value)
