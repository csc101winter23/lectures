# This function is too broad: it is trying to solve two problems, one after the
#  other. In the future, if we only wanted to solve one of these problems, it
#  is not possible to call half of a function...
def get_integer_and_sum_squares():
    n = 0
    while n <= 0:
        n = int(input("Enter a positive integer: "))
    total = 0
    for i in range(n + 1):
        total = total + i ** 2
    return total


# Now that n is needed in a separate function, it must be returned:
def get_integer():
    n = 0

    while n <= 0:
        n = int(input("Enter a positive integer: "))

    return n


# Now that n is needed from a separate function, it must be taken as argument:
def sum_squares(n):
    total = 0

    for i in range(n + 1):
        total = total + i ** 2

    return total


# This function is too specific: it has so many details hardcoded with it that
#  it can't solve very similar problems.
def sum_cubes(n):
    total = 0

    for i in range(n + 1):
        total = total + i ** 3

    return total


# It is not possible to change a detail inside a function when calling it, but
#  it is always possible to pass in more details as arguments:
def sum_powers(n, power):
    total = 0

    for i in range(n + 1):
        total = total + i ** power

    return total


def main():
    # ...but it is always possible to call two functions, one after the other:
    print(sum_powers(get_integer(), 2))


if __name__ == "__main__":
    main()
