# Suppose the user types:
#  -2
#  0
#  17
# ...what will the following program print?

total = 0
count = 0

while total <= 0:
    total = int(input("Sum? "))

while total > 0:
    if total >= 25:
        temp = 25
    elif total >= 10:
        temp = 10
    elif total >= 5:
        temp = 5
    else:
        temp = 1

    total = total - temp
    count = count + 1
    print(temp)

print(str(count) + " addend(s)")
