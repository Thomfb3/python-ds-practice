def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    counts_one = {}
    counts_two = {}

    for num in str(num1):
        counts_one[num] = counts_one.get(num, 0) + 1

    for num in str(num2):
        counts_two[num] = counts_two.get(num, 0) + 1

    return counts_one == counts_two