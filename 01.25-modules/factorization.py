# Suppose the user types:
#  15
# ...what will the following program print?

def divides(a, b):
    return b % a == 0


def factors(number):
    factor = 2
    count = 0

    while number > 1:
        if divides(factor, number):
            print(str(factor))
            number = number // factor
            count = count + 1
        else:
            factor = factor + 1

    return count


def main():
    number = int(input("Number? "))

    if factors(number) == 1:
        print(str(number) + " is prime.")
    else:
        print(str(number) + " is not prime.")


if __name__ == "__main__":
    main()
