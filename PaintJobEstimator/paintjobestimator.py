import math
def round_Up(value:float,places:int):
    multipliedPlaces = 10 ** places
    return float(math.ceil(value*multipliedPlaces)/multipliedPlaces)
while True:
    print('Paint Job Estimator')
    while True:
        try:
            wallSpace = float(input('Wall Space (in square feet) = '))
            if wallSpace <= 0:
                print("The value entered is invalid. Wall Space must be greater than zero.")
                continue
        except ValueError:
            print("The value entered is invalid. Please enter a numerical value only.")
        else:
            break
    while True:
        try:
            paintPrice = float(input('Price of Paint (per gallon) = '))
            if paintPrice <= 0:
                print("The value entered is invalid. Price of Paint must be greater than zero.")
                continue
        except ValueError:
            print("The value entered is invalid. Please enter a numerical value only.")
        else:
            break
    gallons = math.ceil(wallSpace/350)
    laborHours = round_Up(gallons*6,1)
    laborCharge = round_Up(laborHours*62.25,2)
    totalCost = round_Up(laborCharge+gallons*paintPrice,2)
    print("Number of gallons required = " + str(gallons))
    print("Hours of labor required = " + str(laborHours))
    print("Total Labor Charges = $" + str(laborCharge))
    print("Total Cost = $" + str(totalCost));
    continueLoop = input('Another Calculation? (y/N): ')
    if continueLoop != "y":
        break
