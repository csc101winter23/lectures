# Suppose the user types:
#  3
#  y
#  0
# ...what will the following program print?

done = False

while not done:
    limit = int(input("Iterations? "))

    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

    done = (limit <= 0) or (input("Again? ") != "y")
