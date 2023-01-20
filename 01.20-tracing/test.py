# A loop allows lines of code to be repeated:
i = 0
while i < 5:
    # The body of a loop may contain any statements...
    print("The current value of i is " + str(i))
    i = i + 1

# ...including another loop:
for i in range(2):
    for j in range(3):
        # The first time through, i = 0 and j = 0.
        # The second time, j is incremented to 1 per line 10, but i is still 0.
        # In general, the "j loop" must run to completion for each and every
        #  iteration of the "i loop".
        print("The current values of i and j are " + str(i) + ", " + str(j))

# Note that the order in which the loops are nested matters:
for j in range(3):
    for i in range(2):
        # In general, the "i loop" must run to completion for each and every
        #  iteration of the "j loop".
        print("The current values of i and j are " + str(i) + ", " + str(j))
