def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    VOWELS = "aeiouAEIOU"

    str_vowels = []
    result_str = []


    for char in s:
        if char in VOWELS:
            str_vowels.append(char)

    str_vowels.reverse()

    for char in s:
        if char in VOWELS:
            result_str.append(str_vowels[0])
            str_vowels.pop(0)
        else:
            result_str.append(char)

    return "".join(result_str)