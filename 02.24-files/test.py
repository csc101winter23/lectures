# In Python, files can be accessed within the form:
with open("hello.txt", "r") as file:
    # Within this block, the file can be accessed for reading via the variable
    #  "file" -- by default, it is assumed that files contain plain text.
    string = file.read()
    print("The file contains the text: \"%s\"" % string)


with open("in.txt", "r") as file:
    # It is also possible to read the file line by line instead of as one big
    #  string:
    lines = file.readlines()
    print("The file contains the lines: %s" % str(lines))


with open("out.txt", "w") as file:
    # Alternatively, files can be opened for writing:
    file.writelines(lines)


with open("log.txt", "a") as file:
    # Opening a file for writing will erase its existing contents. Opening a
    #  file for appending will preserve them:
    file.writelines(lines)


with open("in.txt", "r") as file:
    # Note that files are stored on disk, so reading from a file means that its
    #  contents have to be loaded from disk into memory -- it is possible that
    #  the file is larger than physical memory, and we probably don't want the
    #  whole thing at once...
    string = file.readline()
    print("The first line in the file is: \"%s\"" % string)

    # Behind the scenes, the interpreter knows how far "down" the file we are.
    #  When the file is first opened, we start at the beginning; every time we
    #  read a line, the interpreter knows that we've moved one line "down".
    string = file.readline()
    print("The second line in the file is: \"%s\"" % string)
    string = file.readline()
    print("The third line in the file is: \"%s\"" % string)
    string = file.readline()
    print("The fourth line in the file is: \"%s\"" % string)


# This is such a common pattern that it is the default behavior when iterating
#  over a file: to go line by line.
with open("in.txt", "r") as file:
    i = 0
    for line in file:
        # Note that the newline in the file is kept in the string that is read;
        #  it can be removed using the built-in "strip" function:
        print("The %d'th line in the file is: \"%s\"" % (i, line.strip()))
        i = i + 1
