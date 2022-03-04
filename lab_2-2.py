# Author: ATN 3/4/22

def build_vehicle(wheels, axels, doors, color):
    return "Wheels: {0}\nAxels: {1}\nDoors: {2}\nColor: {3}".format(
        wheels, axels, doors, color
        )


wheels = int(input("Please enter how many wheels: "))
axels = int(input("Please enter how many axels: "))
doors = int(input("Please enter how many doors: "))
color = input("Please enter the color: ")

print(build_vehicle(wheels, axels, doors, color))
