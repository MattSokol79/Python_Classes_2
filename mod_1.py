# Using __name__ and __main__

print("This is mod_1 name ----> " + __name__)
# Key word --> pass <-- helps you to pass without errors
def main():
     return "from mode 1 function"

# Syntax if __name__ == "__main__":
if __name__ == "__main__": # it checks whether the code is run from current file
    main()

# Soooo for those wondering "why?" well if you wanna debug a file, lets say
# our main.py is the place where we do all the calls for python snake we made.
# We can make another __name__ == "__main__": in another file and in that
# if statement we can create funky code we need debugging that
# will not be ran if we import but it will run when we run that specific file
# the file you run py file_name.py is always __main__
# file you import
# lets say from python import Python
# its __name__ == python
