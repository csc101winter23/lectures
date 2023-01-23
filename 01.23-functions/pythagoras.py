# Note that a function need not necessarily take any inputs. To define a
#  function with no parameters:
def get_leg():
    # Note that a function need not necessarily produce any outputs. To return
    #  a value from a function:
    return int(input("How long is one leg? "))

# To define a function with two parameters: 
def hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5

    # Note that a, b, and c are "local" to this function -- they can only be
    #  accessed inside its body.
    print("Inside hypotenuse, the value of 'c' is " + str(c))

    # Note that side_a and side_b are "global" -- they can be accessed anywhere
    #  in any function body or even outside all functions.
    print("Inside hypotenuse, the value of 'side_a' is " + str(side_a))

    return c

# To apply a function that has no parameters, and assign its return value to
#  a variable:
side_a = get_leg() 
side_b = get_leg()

# To apply a function that has two parameters, and assign its return value to
#  a variable:
side_c = hypotenuse(side_a, side_b)

# The Python "standard library" defines a number of built-in functions,
#  including the print function:
print("The hypotenuse has length " + str(side_c))

# Note that these functions are, by default, only defined inside this file.
#  Unless explicitly instructed otherwise, the interpreter will not know what
#  they mean outside of this file.
