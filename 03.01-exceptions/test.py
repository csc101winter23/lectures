# An exception indicates that something unpredictable and extraordinary has
#  disrupted normal execution -- some input to some operation does not
#  represent a meaningful, solvable problem:
lst = [1, 2, 3]

# This raises a IndexError, since the index is out of bounds:
# lst[4]

# This instead raises a ZeroDivisionError, even though the line involves
#  indexing, the error occurs before the index is actually used:
# lst[1 // 0]

# It is also possible to raise exceptions ourselves:
def foo():
    # When raising an exception, we may also include a message, to hopefully
    #  indicate exactly what went wrong:
    raise Exception("I have a bad feeling about this...")

    # This return statement never executes; raising an exception immediately
    #  stops the function and sends the exception back to the caller:
    return 2

def bar():
    # This call will eventually raise an exception. Since we don't do anything
    #  about this exception, it will be sent back up to our caller:
    foo()

    # This return statement also never executes.
    return 1

# Exceptions can be handled using "try...except" blocks:
try:
    x = bar()
    # Since the line above raises an exception, this next line doesn't run...
    print(str(x))
except:
    # ...this line runs instead, so we can do something about the problem:
    print("Nothing to see here!")

# A bare "except" will handle any exception, which is usually considered poor
#  form at best -- different types of exceptions will typically require
#  different corrective actions:
try:
    bar()
except IndexError:
    print("This only prints when an IndexError occurs.")
except ValueError:
    print("This only prints when a ValueError occurs.")
# ...if none of the "except" blocks matches, then the exception is left
#  unhandled, as though the "try...except" wasn't there.
