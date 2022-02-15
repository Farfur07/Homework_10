import random
x = [random.randrange(0, 100, 2) for i in range(0, 100)]

def findMaxNumb (x):
    y = max(x)
    return (y)

print(findMaxNumb(x))
