# Note that unless instructed otherwise, these definitions are only available
#  inside this "module"...

def get_leg():
    return int(input("How long is one leg? "))

def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

# To ensure that these lines only run when this is the "main program":
if __name__ == "__main__":
    side_a = get_leg()
    side_b = get_leg()
    side_c = hypotenuse(side_a, side_b)
    print("The hypotenuse has length " + str(side_c))
