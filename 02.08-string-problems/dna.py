# Determine whether or not two DNA strands consist of complementary base pairs.


def get_string(prompt):
    """
    Get a string from user input.

    :param prompt: A string to show the user
    :return: The next valid DNA strand typed by the user
    """
    return ""


def check_string(string):
    """
    Determine whether or not a string is a valid DNA strand.

    :param string: A string to check
    :return: Whether or not the string consists of 'A's, 'C's, 'G's, and 'T's
    """
    if len(string) == 0:
        return False

    for character in string:
        # NOTE: Just because one character is valid does not necessarily mean
        #       the whole string is valid, but if one character is invalid,
        #       then the whole string is invalid.
        if character != "A" and character != "C" and character != "G" and character != "T":
            return False

    return True


def check_strands(strand_a, strand_b):
    """
    Determine whether or not two strands consist of complementary pairs.

    :param strand_a: A strand to check
    :param strand_b: Another strand to check
    :return: The first mismatched pair, or None if the strands match
    """
    for i in range(len(strand_a)):
        # NOTE: We can't just iterate over the bases in one string; we need to
        #       iterate over both at the same time, which we can do by instead
        #       iterating over the indices, and using the same index on both.
        if not check_bases(strand_a[i], strand_b[i]):
            return strand_a[i], strand_b[i]

    return None


def check_bases(base_a, base_b):
    """
    Determine whether or not two bases are complementary.

    :param base_a: A base to check
    :param base_b: Another base to check
    :return: Whether or not the bases match
    """
    if base_a == "A":
        return base_b == "T"
    elif base_a == "C":
        return base_b == "G"
    elif base_a == "G":
        return base_b == "C"
    else:
        return base_b == "A"


def main():
    # Each DNA strand will be a string. We wish we had the functions:
    #  * A function to get a string from the user
    #  * A function to check if a string is a valid DNA strand
    #  * A function to iterate over both strands simultaneously
    #    (and also check to see if they're the same length first?)
    #  * A function to check if two individual bases are complementary
    pass


if __name__ == "__main__":
    main()
