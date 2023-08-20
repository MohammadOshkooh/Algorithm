def bead_sort(array):
    """
    sort a list of positive integers
    """
    if any(not isinstance(x, int) or x < 0 for x in array):
        raise TypeError('array must be list of non-negative integers')

    for _ in range(len(array)):
        for i, (rod_lower, rod_upper) in enumerate(zip(array, array[1:])):
            if rod_upper < rod_lower:
                array[i] = rod_upper
                array[i + 1] = rod_lower
    return array


arr = list(map(int, input().split()))

print('input: ', arr)

sorted_arr = bead_sort(arr)

print('output: ', sorted_arr)
