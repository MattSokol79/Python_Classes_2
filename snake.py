# Creating a Snake class as a Child class of Reptile
from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__() # Inheriting all the attributes from the Reptile class
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    # Creating methods for the Snake class
    def use_tongue_to_smell(self):
        return "I can smell with my TONGUE!"

# Creating an object for the Snake class
snake_object = Snake()

# print(snake_object.limbs)
# print(snake_object.breathe())
# We have double inheritance and Encapsulated in methods (functions)
# in parent classes