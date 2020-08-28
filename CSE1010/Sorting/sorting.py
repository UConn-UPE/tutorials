# Sorting in Python


"""
.sort() -> None

The .sort() method is a built in method for a list object that sorts the
elements of a given list in a specific ascending or descending order. The
.sort() method will sort the existing list in place and modify the list
itself.

The syntax for using the .sort() method is follows:
    list.sort(key=None, reverse=False)

By default, sort() doesn't require any parameters. However, it has two
optional ones:
    - reverse: if True, the list is sorted in reverse
    - key: function that is used for the sort comparison
"""

# List of random numbers
num_list = [12, 33, 2, 453, 90, 3, 7, 38]

# num_list.sort()
##print(f"Sorted num_list: {num_list}")
##
# num_list.sort(reverse=True)
##print(f"Reverse Sorted num_list: {num_list}")


# List of names
names_list = ['Sam', 'Mike', 'Virginia',
              'Lenny', 'Chris', 'Ali', 'Finn', 'Brandon']

# names_list.sort()
##print(f"Sorted names_list: {names_list}")
##
# names_list.sort(reverse=True)
##print(f"Reverse Sorted names_list: {names_list}")
##
# names_list.sort(key=len)
##print(f"Sorted names_list by length: {names_list}")
##
##names_list.sort(key=lambda name: (len(name), name))
##print(f"Reverse Sorted names_list by length: {names_list}")


"""
sorted() -> list

The sorted() function returns a sorted list from the items of an iterable.
It does not change the object in place

The syntax for the sorted() function is as follows:
    sorted(iterable, key=None, reverse=False)

By default, sort() requires one parameter. However, it has two
optional ones as well:
    - iterable: a sequence (string, tuple, list) or a container (set,
                dictionary, etc.)
    - reverse: if True, the list is sorted in reverse
    - key: function that is used for the sort comparison
"""


##sorted_num_list = sorted(num_list)
##print(f"Sorted num_list: {sorted_num_list}")
##print(f"Original num_list: {num_list}")


# Tuple of random letters
my_tuple = ('a', 'd', 'b', 'c')
##sorted_my_tuple = sorted(my_tuple)
##print(f"my_tuple: {my_tuple}")
##print(f"Sorted my_tuple: {sorted_my_tuple}")
# print(type(sorted_my_tuple))


# Cities and their population (in millions)
cities_dict = {
    'New York': 8.4,
    'Los Angeles': 3.8,
    'Chicago': 2.7,
    'Houston': 2.1
}


def by_key(item):
    return item[0]


def by_value(item):
    return item[1]


# print(sorted(cities_dict))
##
##print(sorted(cities_dict.items(), key=by_key))
##print(sorted(cities_dict.items(), key=lambda item: item[0]))
##
##print(sorted(cities_dict.items(), key=by_value, reverse=True))
##print(sorted(cities_dict.items(), key=lambda item: item[1], reverse=True))


# Sorting User Defined Objects
class Car:
    """Car class"""

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        return f"{self.name}: {self.year}"


car1 = Car("Camry", 2014)
car2 = Car("Prius", 2011)
car3 = Car("Mustang", 2018)

# Garage variable is a tuple of Car objects
garage = (car1, car2, car3)

##cars_sorted_by_name = sorted(garage, key=lambda car: car.name)
##print(f"Cars Sorted By Name: {cars_sorted_by_name}")
##newest_cars = sorted(garage, key=lambda car: car.year, reverse=True)
##print(f"Newest Cars: {newest_cars}")
##print(f"Original Garage Tuple: {garage}")
