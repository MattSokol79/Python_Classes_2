# Getters and Setters
# Why - Use cases
# To hide the data - Seperation of concern (not available for others to access)
# Syntax 2 functions, 1 to get information, and 1 to set information

# Create a class called Student:
# Step 1
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    @property # A decorator in python is any callable python object that is used
    # to modify a function or a class
    def Student(self, value): # Setter
        self.__name # __ are used to hide the data


    @Student.setter # Allows special permissions to access the name
    def Student(self, value): # Getter
        print(" calling @student.student method")
        self.__name = value


student_object = Student("Matt", "Sparta Global")

print("Student name is " + student_object.name)
print("=" * 34)
print("student works in " + student_object.company)