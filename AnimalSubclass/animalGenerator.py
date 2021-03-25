from Animal import Animal, Mammal, Bird
print('Welcome to the animal generator!\nThis program creates Animal objects.')
animalList = []
while True:
    print('\nWould you like to create a mammal or bird?\n1. Mammal\n2. Bird')
    while True:
        animalType = input('Which would you like to create? ')
        if animalType != "1" and animalType != "2":
            print("Please choose a valid option!")
            continue
        break
    print()
    if animalType == "2":
        while True:
            birdType = input('What type of bird would you like to create? ')
            if birdType == '':
                print("Please enter the type of bird")
                continue
            break
        while True:
            birdName = input('What is the bird\'s name? ')
            if birdName == '':
                print("Please enter the bird\'s name!")
                continue
            break
        while True:
            canFly = input('Can the bird fly? ')
            if canFly == '':
                print("Please enter whether the bird can fly!")
                continue
            break
        animalList.append(Bird(birdType,birdName,canFly))
    if animalType == '1':
        while True:
            mammalType = input('What type of mammal would you like to create? ')
            if mammalType == '':
                print("Please enter the type of mammal")
                continue
            break
        while True:
            mammalName = input('What is the mammal\'s name? ')
            if mammalName == '':
                print("Please enter the mammal\'s name!")
                continue
            break
        while True:
            hairColor = input('What color is the mammal\'s hair? ')
            if hairColor == '':
                print("Please enter the mammal\'s hair color!")
                continue
            break
        animalList.append(Mammal(mammalType,mammalName,hairColor))
    continueLoop = input('\nWould you like to add more animals (y/n)? ')
    if continueLoop != "y":
        break
print('\nAnimal List:')
for animal in animalList:
    print(animal.get_name() + ' the ' + animal.get_animal_type() + ' is ' + animal.get_mood())
