import numpy as np
# Implement a number guessing game where the computer generates a random number, and the user has to guess it. Provide feedback (too high, too low).

def guessnumber(number):
    if number <= 100 :
        return "The number is too Low"
    elif number >=500 :
        return "The number is too High"
    else:
        return "The number is moderate [Greater than 100 and less than 500]"


# Write a program that calculates the factorial of a given number using both iterative and recursive approaches.


def factIterator(number):
    if number in [0,1]:
        return 1
    else:
        for num in range(1,number):
            number *= num
    return number


def factRecursive(number):
    if number in [0,1]:
        return 1
    return number * factRecursive(number-1)






print("Factorial using iterator : ", factIterator(1))

print("Factorial using Recursive : ", factRecursive(5))

numbers = np.random.randint(1,1000)
print(numbers)

print(guessnumber(numbers))