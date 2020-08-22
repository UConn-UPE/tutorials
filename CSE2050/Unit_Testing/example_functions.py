
def absolute_value(num):
    """Returns the absolute value of the inputted value"""

    if type(num) not in {int, float}:
        raise TypeError("Inputted value must be int or float")
    if num >= 0:
        return num
    else:
        return -num


def square(num):
    """Returns the squared value of the inputted value"""
    if type(num) not in {int, float}:
        raise TypeError("Inputted value must be int or float")

    return num**2

##print('---Absolute Value---')
##print(absolute_value(3))
##print(absolute_value(0))
##print(absolute_value(-1))
##print('\n---Square---')
##print(square(2))
##print(square(2.5))
##print(square(-3))
