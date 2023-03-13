def min_element(lst):
    """ Find the smallest element in a list. """
    temp = None

    for element in lst:
        if temp is None or element < temp:
            temp = element

    return temp
