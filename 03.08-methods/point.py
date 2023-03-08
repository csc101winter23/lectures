class Point:
    # These are the basic operations we pretty much always want: we want to be
    #  able to make Points, to compare Points, and to print Points.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return type(other) == Point and self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    # There are other special methods that also implement operations:
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("cannot add Points to non-Points")

    # We can also add arbitrary methods with no existing special meaning:
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


# Alternatively, that method could have been defined outside the class, but, as
#  an ordinary function, it has no "self". It will have to take the point on
#  which to operate as a separate argument:
def translate(pt, dx, dy):
    pt.x = pt.x + dx
    pt.y = pt.y + dy
