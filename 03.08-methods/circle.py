class Circle:
    def __init__(self, center, radius):
        # We could have Circles contain separate x and y attributes, but we
        #  already have the Point class that contains them for us:
        self.center = center  # A Point
        self.radius = radius  # An integer

    def __eq__(self, other):
        # Since the x and y are collected together into a Point, and Points
        #  already know how to compare themselves, we don't have to do the work
        #  of comparing the x and y here:
        return (type(other) == Circle
                and self.center == other.center
                and self.radius == other.radius)

    def __repr__(self):
        return "Circle(%s, %d)" % (str(self.center), self.radius)
