def Ackermann(m, n):
    """
    Implements the recursive Ackermann function A(m, n).
    
    :param m: A non-negative integer.
    :param n: A non-negative integer.
    :return: The value of Ackermann's function A(m, n).
    """
    
    # Rule 1: Base Case for m
    if m == 0:
        return n + 1
    
    # Rule 2: Base Case for n when m > 0
    elif m > 0 and n == 0:
        # Note: You can simply use 'elif n == 0:' since m > 0 is implied 
        # because the m == 0 case was handled above.
        return Ackermann(m - 1, 1)
    
    # Rule 3: Recursive Step for m > 0 and n > 0
    else: # m > 0 and n > 0
        # The inner recursive call A(m, n - 1) is evaluated first, 
        # and its result becomes the 'n' parameter for the outer call A(m - 1, ...).
        inner_result = Ackermann(m, n - 1)
        return Ackermann(m - 1, inner_result)

# Example Usage (as required):
# print(Ackermann(1, 2)) # Should return 4
# A(1, 2) -> A(0, A(1, 1))
# A(1, 1) -> A(0, A(1, 0))
# A(1, 0) -> A(0, 1) -> 1 + 1 = 2
# A(1, 1) -> A(0, 2) -> 2 + 1 = 3
# A(1, 2) -> A(0, 3) -> 3 + 1 = 4
# print(f"A(1, 2) = {Ackermann(1, 2)}") # Output: A(1, 2) = 4
