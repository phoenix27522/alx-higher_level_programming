def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Peak may be in the left subarray
            high = mid
        else:
            # Peak may be in the right subarray
            low = mid + 1

    # 'low' is the index of a peak
    return list_of_integers[low]
