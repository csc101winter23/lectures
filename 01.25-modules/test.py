# When this file is run from the command line, this is the "entry point":
#  execution begins here, and other files will only get run once they are
#  imported later.

# ...to import definitions from another module:
import pythagoras

# By convention, the code at the entry point is often encapsulated in a
#  function named "main":
def main():
    # To access a definition from another module:
    x = pythagoras.hypotenuse(3, 4)
    print("The value of x is " + str(x))

if __name__ == "__main__":
    main()
