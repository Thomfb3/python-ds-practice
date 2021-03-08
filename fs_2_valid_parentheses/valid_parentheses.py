def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    if parens.startswith(")"):
        return False

    if parens.endswith("("):
        return False
    
    open_parentheses = 0

    for p in parens:
        if p == "(":
            open_parentheses += 1
        elif p == ")":
            open_parentheses -= 1
        
    return open_parentheses == 0

