# Author: ATN 3/7/22

def r_max(numbers):
    counter = 0
    for x in numbers:
        if type(x) == list:
            x = r_max(x)
            if x > counter:
                counter = x
        else:
            if x > counter:
                counter = x
    return counter

my_numbers = [1, 2, 4, 6, [7, 9, 10]]

print(r_max(my_numbers))
