# Author: ATN 3/4/22

def build_car(wheels, axels, doors, color):
    return "Wheels: {0}\nAxels: {1}\nDoors: {2}\nColor: {3}".format(
        wheels, axels, doors, color
        )


print(build_car(4, 2, 4, "red"))
