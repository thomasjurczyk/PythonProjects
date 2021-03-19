import random
print('Random Number File Writer')
while True:
    try:
        quantity = int(input('Quantity of random numbers = '))
        if quantity <= 0:
            print("The value entered is invalid. Quantity must be greater than zero.")
            continue
    except ValueError:
        print("The value entered is invalid. Please enter a numerical value only.")
    else:
        break
while True:
    try:
        lowerBound = int(input('The lowest possible random number = '))
        if lowerBound <= 0:
            print("The value entered is invalid. Lower bound must be greater than zero.")
            continue
    except ValueError:
        print("The value entered is invalid. Please enter a numerical value only.")
    else:
        break
while True:
    try:
        upperBound = int(input('The highest possible random number = '))
        if lowerBound <= 0:
            print("The value entered is invalid. Upper bound must be greater than zero.")
            continue
    except ValueError:
        print("The value entered is invalid. Please enter a numerical value only.")
    else:
        break
f = open("randomnum.txt","w")
for x in range(quantity):
    f.write(str(random.randrange(lowerBound,upperBound)) + "\n")
f.close()
print('The random numbers were written to randomnum.txt')
