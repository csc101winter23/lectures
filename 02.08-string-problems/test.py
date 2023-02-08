# A string is a collection...
s = "hello"

# ...it is possible to iterate over that collection:
for c in s:
    print(c)

# Alternatively, we could iterate over the range of valid indices, then use
#  each index to extract the corresponding character:
for i in range(len(s)):
    # It is possible to format expressions within strings:
    print("The character at index %d is %s." % (i, s[i]))
