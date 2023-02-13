def max_element(lst):
    """
    Find the largest element in a list.

    :param lst: A non-empty list of integers
    :return: The largest integer in the list
    """
    # Start by assuming that the first element is the largest:
    temp = lst[0]

    # Go through all of the elements.
    for element in lst:
        # If another element is larger, then the previous assumption was
        #  incorrect; update the assumption based on the new element.
        if element > temp:
            temp = element

    # Once we've gone through all of the elements, the final assumption must
    #  also be the answer.
    return temp


def scale_list(lst, scalar):
    """
    Multiply every element in a list by a scalar, modifying the list.

    :param lst: A list of integers
    :param scalar: An integer scalar
    """
    # Note that since our goal is modify the given list, we must use indices
    #  to put the resulting elements back into the list from which they came:
    for i in range(len(lst)):
        lst[i] = lst[i] * scalar


def scale_copy(lst, scalar):
    """
    Multiply every element in a list by a scalar, creating a copy.

    :param lst: A list of integers
    :param scalar: An integer scalar
    :return: A new list containing the scaled integers
    """
    temp = []

    # Note that since our goal is make a copy of the given list, we need not
    #  use indices -- we don't need to know where the elements came from:
    for element in lst:
        temp.append(element * scalar)

    # Since we've now made a new list, that list is currently local to this
    #  function. If we need to pass it back to our caller, we must return it:
    return temp
