print("This runs unconditionally.")

# NOTE: Any of these conditions could involve variables, such that we don't
#       know whether they are going to be true or false at the time we write
#       the code.

# In Python, a conditional "if" statement has the basic form:
if 1 > 2:
    # This statement is only executed when the condition is true (which, in this
    #  case, it never is).
    print("This only runs when 1 > 2.")

# Each "if" can optionally have an "else":
if 1 > 2:
    print("This only runs when 1 > 2.")
else:
    print("This only runs when 1 <= 2.")

# As many "elif" cases as desired may be added, as long as they are after the
#  "if" (which is always required) and before the "else" (which is optional):
if 1 > 2:
    print("This only runs when 1 > 2.")
elif 1 < 2:
    print("This only runs when 1 < 2.")
else:
    print("This only runs when 1 == 2.")

# NOTE: An "if...elif" is not necessarily the same as an "if...if", because
#       the conditions may not be mutually exclusive:
# if 1 < 2:
#     ...
# elif 1 <= 2:
#     ...
# 
# if 1 < 2:
#     ...
# if 1 <= 2:
#     ...

print("This also runs unconditionally.")
