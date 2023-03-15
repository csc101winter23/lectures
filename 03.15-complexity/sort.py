# Now that we know minimum_v1 and minimum_v2 are equally correct, but the
#  latter is faster, there is basically no reason to use the former...
import minimum_v2

def selection_sort(lst):
    """
    Sort a list of integers in ascending numerical order.

    :param lst: A list of integers
    :return: A new list containing the same integers in sorted order
    """
    sorted_lst = []

    # This is a "selection sort": until the unsorted list is emptied, we will
    #  repeatedly "select" the next smallest element:
    while len(lst) > 0:
        # The next smallest element of the unsorted list must be the next
        #  element of the sorted list:
        temp = minimum_v2.min_element(lst)
        sorted_lst.append(temp)
        # But we don't want to pick the same element twice:
        lst.remove(temp)

    return sorted_lst
