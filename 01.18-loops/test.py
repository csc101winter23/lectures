# The basic syntax of an "if" statement allows certain operations to be skipped
#  when a condition is not met:
if 1 < 2:
    # The "body" of an "if" can be any sequence of statements...
    print("This only runs when 1 < 2.")

if 1 < 2:
    # ...including more "if" statements:
    if 1 < 3:
        print("This only runs when 1 < 2 and 1 < 3.")
    print("This runs when 1 < 2, regardless of whether or not 1 < 3.")

# NOTE: The above nested "if"s are equivalent to a single "if" with the
#       conditions "and"ed together.
if 1 < 2 and 1 < 3:
    print("This only runs when 1 < 2 and 1 < 3.")

# NOTE: ...but splitting the "if...and..." into two nested "if"s allows us to
#       attach "else"s to them independently.
x = 1
y = 2
z = 3

if x > y:
    # To get here, y is not the biggest.
    if x > z:
        # To get here, z is also not the biggest, so x must be the biggest.
        print("x is the largest of x, y, z")
    else:
        # To get here, x is also not the biggest, so z must be the biggest.
        print("z is the largest of x, y, z")
else:
    # To get here, x is not the biggest.
    if y > z:
        # To get here, z is also not the biggest, so y must be the biggest.
        print("y is the largest of x, y, z")
    else:
        # To get here, y is also not the biggest, so z must be the biggest.
        print("z is the largest of x, y, z")

# By convention, the "loop counter" is often the variable "i":
i = 0
while i < 5:
    print("This runs as long as i < 5; the current value of i is " + str(i))
    i = i + 1
print("This only runs once i >= 5; the current value if i is " + str(i))

# If the condition is always false -- here, i is already 5 -- then the loop
#  will never run:
while i < 5:
    print("This runs as long as i < 5; the current value of i is " + str(i))
    i = i + 1

# If the condition is always true -- here, i will never be < 5 -- then the loop
#  will run infinitely:
# while i >= 5:
#     print("This runs as long as i >= 5; the current value of i is " + str(i))
#     i = i + 1
# ...when this happens, Ctrl+c at the terminal can tell the operating system
#  to stop the program.

# Alternatively, we could tell the interpreter exactly what values should be
#  incrementally assigned to i, instead of managing ourselves:
for i in range(5):
    print("This runs for i in range(5); the current value of i is " + str(i))
# ...the interpreter knows to start at i = 0; it knows to increment i = i + 1;
# it knows to stop once i >= 5 -- there is less danger of messing up ourselves.

# It is possible to specify a lower bound:
for i in range(5, 11):
    print("This runs for i in range(5, 11); the current value of i is " + str(i))

# It is possible to specify an increment:
for i in range(5, 0, -1):
    print("This runs for i in range(5, 0, -1); the current value of i is " + str(i))

# The interpreter is smart enough to know when there are no integers in a range
#  instead of allowing the loop to run forever:
for i in range(5, 0):
    print("This runs for i in range(5, 0); the current value of i is " + str(i))
