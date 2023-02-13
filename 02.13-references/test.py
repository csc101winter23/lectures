# A list is a sequence of elements.
# Each element may be of any type.
# Each element could itself be a list.
matrix = [[1, 2, 3, 4], [5, 6, 7]]
print("matrix: %s" % (str(matrix)))

# A two-dimensional list must therefore be indexed twice to access its
#  "innermost" elements -- the first index only accesses an "inner" list:
matrix[0][1] = 8
print("matrix: %s" % (str(matrix)))

# The "inner" lists are separate and independent: modifying one does not
#  in this case modify the other.
matrix[1].append(9)
print("matrix: %s" % (str(matrix)))

# The "outer" elements may have any type -- they need not necessarily all be
#  "inner" lists.
matrix.append(10)
print("matrix: %s" % (str(matrix)))
