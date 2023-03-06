# The coordinates of a point could be represented as individual variables, but
#  the interpreter will have no way of knowing that they're supposed to go
#  together -- if there are multiple points, we the programmers are responsible
#  for knowing which x's go with which y's; if a point is passed into a
#  function, we the programmers are responsible for knowing that x and y are
#  passed as separate arguments:
x = 3
y = 4

# To define a new type representing points (by convention, class names are
#  capitalized to distinguish them from variable and function names):
class Point:
    # To define how to instantiate a Point (note that "self." accesses the
    #  attributes inside the current instance of this class):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # To define how to convert a Point into a string (the interpreter has no
    #  idea what this class does, so by default the string is just the name
    #  of the class and the location of the object in memory):
    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    # To define how to compare a Point to another value (by default, this is
    #  done with reference equality; two objects are equal if and only if they
    #  are in the same location in memory):
    def __eq__(self, other):
        return type(other) == Point and self.x == other.x and self.y == other.y

# A class simply defines what a new type looks like; it doesn't create any
#  values of that type. To create an object, an instance of a class:
point = Point(3, 4)
# ...here, "point" does not contain a Point; it is a reference to a Point. Its
#  attributes can then be accessed with the "." operator:
print("point.x: %d" % point.x)
print("point.y: %d" % point.y)
print("point: %s" % str(point))

point2 = point
point3 = Point(3, 4)

# To compare two objects by calling their __eq__ method:
print("point2 == point: %s" % (point2 == point))
print("point3 == point: %s" % (point3 == point))

# To compare two objects by reference:
print("point2 is point: %s" % (point2 is point))
print("point3 is point: %s" % (point3 is point))

# In Python, the attributes of a class are generally mutable, just like
#  ordinary variables. This means it is possible that two equal objects become
#  non-equal later; it means it is possible that two references to the same
#  object reflect the same mutations later:
point.x = 5
print("point2 == point: %s" % (point2 == point))
print("point3 == point: %s" % (point3 == point))
