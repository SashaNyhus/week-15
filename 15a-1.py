import random

print(random.randint(0, 10))

def getNumber():
    newNumber = input('enter a number')
    return newNumber


def getNumbersArray():
    newNumbersArray = []
    while(len(newNumbersArray) < 5):
        newNumbersArray.append(getNumber())
    return newNumbersArray


def getMinimum(array):
    minimum = array[0]
    for number in array:
        if(number < minimum):
            minimum = number
    return minimum

def getMaximum(array):
    maximum = array[0]
    for number in array:
        if(number > maximum):
            maximum = number
    return maximum


def getMode(array):
    sortedArray = array.sort()
    


def getAverage(array):
    sum = 0
    for number in array:
        sum += number
    average = (sum / (len(array)))
    print(sum)
    return average


numbersArray = getNumbersArray()


print(numbersArray)
print(getMinimum(numbersArray))
print(getMaximum(numbersArray))


