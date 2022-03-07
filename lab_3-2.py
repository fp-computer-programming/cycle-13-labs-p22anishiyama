# Author: ATN 3/7/22

result = []

def factorial(n):
    counter = n
    result.append(n)
    if counter == 0:
        return result
    else:
        factorial(counter - 1)  

print(factorial(4))
