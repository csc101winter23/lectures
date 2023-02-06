# A string, unlike other data types, is a collection of multiple characters:
s = "hello"
print("s is a string: " + str(s))

# The "len" function can be used to compute the size of a collection:
print("len(s): " + str(len(s)))

# Membership in a collection can be tested with the "in" operator:
#  Note that \" escapes the quote, so that it doesn't look like the end of
#  the string, and is just a normal character.
print("\"e\" in s: " + str("e" in s))

# Every character in a string is associated with a unique index:
print("\"e\" is in s at index: " + str(s.find("e")))

# Indices can be used to access specific characters using square brackets:
print("s[1]: " + s[1])

# In Python, indices "wrap around"; negative indices count backwards from the
#  end of a collection:
print("s[-1]: " + s[-1])

# In Python, a "slice" can be used to extract multiple elements of a collection
#  within a range of indices:
print("s[1:3]: " + s[1:3])
print("s[1:]: " + s[1:])
print("s[:1]: " + s[:1])
print("s[:]: " + s[:])
print("s[::-1]: " + s[::-1])
print("s[0:5:2]: " + s[0:5:2])
