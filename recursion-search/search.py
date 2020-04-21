def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return item
    if index == len(array):
        return None
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    lower_bound = 0
    upper_bound = len(array) - 1
    mid_bound = (lower_bound + upper_bound) // 2

    while not array[mid_bound] == item:
        if item > array[mid_bound]:
            lower_bound = mid_bound + 1
            mid_bound = (lower_bound + upper_bound) // 2

        elif item < array[mid_bound]:
            upper_bound = mid_bound - 1
            mid_bound = (lower_bound + upper_bound) // 2

        if lower_bound == mid_bound and array[lower_bound] != item:
            return None
    return mid_bound
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left == None and right == None:
        left = 0
        right = len(array) - 1

    mid_bound = (left + right) // 2
    if array[mid_bound] == item:
        return mid_bound
    elif left == mid_bound and array[left] != item:
        return None
    else:
        if item > array[mid_bound]:
            left = mid_bound + 1
        else:
            right = mid_bound - 1
        return binary_search_recursive(array, item, left, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


print(linear_search([1, 2, 4, 5, 6, 8, 9], 8))
print(binary_search([1, 2, 4, 5, 6, 8, 9], 8))
