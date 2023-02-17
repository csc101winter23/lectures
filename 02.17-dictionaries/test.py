# A dictionary is essentially a list whose indices, which we now call "keys",
#  may have any type:
dct = {"a": "alpha", "b": "beta"}
print("dct: %s" % (str(dct)))
print("dct[\"a\"]: %s" % (dct["a"]))

# Since the keys may not have any meaningful ordering, it doesn't make sense to
#  "append" to the end of a dictionary; if the key doesn't exist, it will be
#  created:
dct["c"] = "gamma"
print("dct: %s" % (str(dct)))

# If the same key is used twice, the old value is replaced:
dct.update({"c": "kappa", "d": "delta"})
print("dct: %s" % (str(dct)))

# Just like lists, entire dictionaries cannot fit into variables; assigning one
#  dictionary to another simply creates a second reference:
dct2 = dct
dct2["e"] = "epsilon"
print("dct: %s" % (str(dct)))

# Just like lists, dictionaries can also be created by comprehensions:
dct3 = {x: x ** 2 for x in range(5) if x % 2 == 1}
print("dct3: %s" % (str(dct3)))

# Note that knowing a key is almost always more useful than knowing a value:
#  every key uniquely identifies its value, but each value does not necessarily
#  uniquely identify its key. The default behavior is to iterate over the keys.
for x in dct:
    # Once we have a key, we can use it to access a value, if desired.
    print("x: %s, dct[x]: %s" % (str(x), str(dct[x])))

# If we know that we only need the values, then we can explicitly ask for them:
for y in dct.values():
    print("y: %s" % (str(y)))

# Even though a dictionary is a more powerful generalization of a list, we
#  can't always use dictionaries -- there are operations that are only
#  applicable to lists:
# dct.sort()
lst = list(dct.keys())
lst.sort()
print("lst: %s" % (str(lst)))

# Even though a dictionary is a more powerful generalization of a list, if we
#  don't need that power, we don't want to open ourselves up to the possibility
#  of using it incorrectly -- if we only ever plan to use true integer indices,
#  a dictionary won't yell at us if we accidentally use a string...
dct4 = {0: 1, 1: 2, 2: 3}
print("dct4: %s" % (str(dct4)))
dct4["3"] = "4"
print("dct4: %s" % (str(dct4)))
