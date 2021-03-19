import random
class Animal:
    __animal_type = ""
    __name = ""
    __mood = ""
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        randMood = random.randint(1,3)
        if(randMood == 1):
            self.__mood = "happy"
        elif(randMood == 2):
            self.__mood = "hungry"
        else:
            self.__mood = "sleepy"
    def get_animal_type(self):
        return self.__animal_type
    def get_name(self):
        return self.__name
    def get_mood (self):
        return self.__mood
