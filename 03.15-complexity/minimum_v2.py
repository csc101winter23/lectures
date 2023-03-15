def min_element(lst):
    """ Find the smallest element in a list. """
    temp = None

    # ...this is much more efficient, even in the worst case scenario, we only
    #  have to go through the list once.
    for element in lst:
        if temp is None or element < temp:
            temp = element

    return temp
