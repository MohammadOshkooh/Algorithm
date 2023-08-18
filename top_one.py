def top_one(array):
    """
    Returns the most frequently occurring numbers
    Time complexity: O(n)
    """
    result = []
    numbers = {}

    for num in array:
        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1

    max_count = max(numbers.values())

    for num in numbers.keys():
        if numbers[num] == max_count:
            result.append(num)

    return result


arr = list(map(int, input().split()))

print(f'input: {arr}')

print(f'output: {top_one(arr)}')
