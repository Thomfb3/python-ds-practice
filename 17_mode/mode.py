def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    number_counts = {}

    for num in nums:
        number_counts[num] = number_counts.get(num, 0) + 1

    most_common = max(number_counts.values())
    
    for (num, freq) in number_counts.items():
        if freq == most_common:
            return num

