# A list is an indexed collection of arbitrary elements; a list is effectively
#  a string whose elements need not be characters:
lst = [1, 2, 3]
print("lst: %s" % str(lst))

# Just like strings, lists can be indexed using square brackets:
print("lst[1]: %d" % lst[1])

# Just like strings, membership in lists can be tested using "in":
print("\"1\" in lst: %s" % str("1" in lst))

# Just like strings, lists can be concatenated using "+":
lst = lst + [4, 5]
print("lst: %s" % str(lst))

# Just like strings, lists can be compared for equality, where order matters:
print("lst == [5, 4, 3, 2, 1]: %s" % (str(lst == [5, 4, 3, 2, 1])))

# Unlike strings, the elements in a lists can be mutated:
lst[1] = 0
print("lst: %s" % str(lst))

# Unlike strings, most of the built-in list functions mutate their lists:
lst.sort()
lst.reverse()
print("lst: %s" % str(lst))

# Lists can also be created using "comprehensions":
lst1 = lst
lst2 = [x ** 2 for x in range(5)]

# Note that a comprehension always creates a new list; it never modifies an
#  existing list:
print("lst1: %s" % str(lst1))
print("lst2: %s" % str(lst2))

# Optionally, a list comprehension may specify a condition that all elements
#  of the resulting list must pass:
lst3 = [x ** 2 for x in range(5) if (x ** 2) % 2 == 0]
print("lst3: %s" % str(lst3))

# Note that the condition in a list comprehension can only be an "if"; it
#  cannot have any "elif" or "else" blocks:
lst4 = []
for x in range(5):
    if (x ** 2) % 2 == 0:
        lst4.append(x ** 2)
    else:
        lst4.append(None)
print("lst4: %s" % str(lst4))

# ...if we want to modify an existing list, we must use a traditional loop:
for i in range(5):
    if lst4[i] is not None:
        lst4[i] = lst4[i] + 1
print("lst4: %s" % str(lst4))

# Note that assigning one list variable to another simply creates two variables
#  that refer to the same underlying block of memory -- changing one will
#  effectively change both:
lst5 = lst1
print("lst1: %s, lst5: %s" % (str(lst1), str(lst5)))
lst5[0] = 6
print("lst1: %s, lst5: %s" % (str(lst1), str(lst5)))

# If we as the programmers happen to know that we need a true copy of a list,
#  rather than two references to the same list, we can use the built-in copy
#  function to make one:
lst5 = lst1.copy()
print("lst1: %s, lst5: %s" % (str(lst1), str(lst5)))
lst5[0] = 7
print("lst1: %s, lst5: %s" % (str(lst1), str(lst5)))
