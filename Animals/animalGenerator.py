from Animal import Animal
print('Welcome to the animal generator!\nThis program creates Animal objects.')
animalList = []
while True:
    while True:
        animalType = input('\nWhat type of animal would you like to create? ')
        if animalType == '':
            print("Please enter the animal's type")
            continue
        break
    while True:
        animalName = input('What is the animal’s name? ')
        if animalName == '':
            print("Please enter the animal's name")
            continue
        break
    animalList.append(Animal(animalType,animalName))
    continueLoop = input('\nWould you like to add more animals (y/n)? ')
    if continueLoop != "y":
        break
print('\nAnimal List:')
for animal in animalList:
    print(animal.get_name() + ' the ' + animal.get_animal_type() + ' is ' + animal.get_mood())
