def is_min(lst, value):
    """ Check if a value is smallest in a list. """
    for element in lst:
        if element < value:
            return False
    return True


def min_element(lst):
    """ Find the smallest element in a list. """
    for element in lst:
        if is_min(lst, element):
            return element
    return None
