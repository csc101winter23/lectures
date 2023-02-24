# Copies the contents of one file into another.

import sys


def copy(src, dest):
    """
    Copy the contents of a file.

    :param src: A filename from which to copy
    :param dest: A filename to which to copy
    """

    # It is possible to open multiple files simultaneously, so that they can
    #  be efficiently accessed at the same time.
    with open(src, "r") as src_file, open(dest, "w") as dest_file:
        for line in src_file:
            dest_file.write(line)


def main():
    # In Python, the "command line arguments" are accessed via the list
    #  "sys.argv". The first command line argument will always be the name
    #  of the script; the rest are passed in when invoking the program.
    copy(sys.argv[1], sys.argv[2])
    # ...this allows this to be run as "python3.9 copy.py in.txt copy.txt", in
    #  the same way that we would run the built-in "cp in.txt copy.txt".


if __name__ == "__main__":
    main()
