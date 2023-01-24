def get_leg():
    return int(input("How long is one leg? "))

def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

side_a = get_leg()
side_b = get_leg()
side_c = hypotenuse(side_a, side_b)
print("The hypotenuse has length " + str(side_c))
