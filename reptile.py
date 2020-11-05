# Creating a reptile class as a child class of Animal Class
from animal import Animal  # From (animal - FILE) import (Animal - CLASS)

class Reptile(Animal):

    def __init__(self):

        super().__init__() # Super key word is used to inherit everything from a parent class
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chambers = [3, 4]


    # Creating methods for our Reptile class
    def seek_heat(self):
        return "I need WARMTH"

    def hunt(self):
        return "I'm hungry, I need to eat! Don't shame me."

    def use_venom(self):
        return "Super effective for hunting"

# Creating an object for our Reptile class to utilise the amazing functionalities
# of OOP
reptile_object = Reptile()

# Below are the inherited methods from the Animal Parent Class
# print(reptile_object.eat())
# print(reptile_object.breathe())
# print(reptile_object.procreate())

# Below are the reptile class methods
# print(reptile_object.hunt())
# print(reptile_object.use_venom())