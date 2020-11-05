# Creating an Animal class as PARENT/BASE/SUPER class

class Animal:

    def __init__(self):
        # Creating attributes/variables
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    # Now create behaviours as functions/methods (in classes)
    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "Nom Nom Nom"

    def procreate(self):
        return "Find partner"

    def move(self):
        return "Left to right and up and down.... "


# Instantiate our class/create an object

# cat = Animal() # Creating an object of Animal class

# cat, has all the attributes of the Animal class
# print(cat.breathe())
# print(cat.eyes)