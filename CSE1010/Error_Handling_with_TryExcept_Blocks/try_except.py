
def divide(a, b):
    return a/b

# divide(1, 0)  # error -> cannot divide by 0


try:
    print(divide(1, 0))  # will raise a ZeroDivisionError, will be caught
except ZeroDivisionError as e:
    print(e)  # will be printed
else:
    print('Nothing went wrong')
finally:
    print('End of try/except block')
print()

try:
    print(divide(1, 1))  # no error since we can divide 1 by 1
    l = []  # create empty list
    print(l[0])  # will raise an IndexError, will be caught
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)  # will be printed
else:
    print('Nothing went wrong')
finally:
    print('End of try/except block')
print()

try:
    print(divide(1, 1))  # no error since we can divide 1 by 1
    l = []  # create empty list
    print(l)  # no error will be raise
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
else:
    print('Nothing went wrong')  # will be printed since there will be no error
finally:
    print('End of try/except block')