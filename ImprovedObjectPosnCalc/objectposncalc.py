while True:
    print('Final Position Calculator')
    while True:
        try:
            initialX = float(input('Initial Position (in Meters) = '))
        except ValueError:
            print("The value entered is invalid. Please enter a numerical value only.")
        else:
            break
    while True:
        try:
            initialV = float(input('Initial Velocity (in Meters/Second) = '))
        except ValueError:
            print("The value entered is invalid. Please enter a numerical value only.")
        else:
            break
    while True:
        try:
            acceleration = float(input('Acceleration (in Meters/Second^2) = '))
        except ValueError:
            print("The value entered is invalid. Please enter a numerical value only.")
        else:
            break
    while True:
        try:
            time = float(input('Time (in Seconds) = '))
            if(time < 0):
                print("The value entered is invalid. Time must be greater than zero.")
                continue
        except ValueError:
            print("The value entered is invalid. Please enter a numerical value only.")
        else:
            break
    print('Final Position is ' + str(initialX + initialV * time + acceleration * time ** 2 / 2) + ' Meters')
    continueLoop = input('Another Calculation? (y/N): ')
    if continueLoop != "y":
        break
