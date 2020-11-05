# Creating a Python class as a Child class of Snake

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__() # Inheriting everything from the Snake Class
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "I can eat almost anything..."

    def constrict(self):
        return "I can constrict! ... Whatever that means"

    def climb(self):
        return "Im an efficient climber"

    def shed_skin(self):
        return "I dont need no l'Oreal products to look sleeek"

# Creating an object of the Python() class
python_object = Python()

# print(python_object.eat())                       FROM Animal Class
# print(python_object.hunt())                      FROM Reptile Class
# print(python_object.use_tongue_to_smell())       FROM Snake Class
# print(python_object.climb())                     FROM Python Class