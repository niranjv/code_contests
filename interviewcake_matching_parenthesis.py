# URL: https://www.interviewcake.com/question/python/matching-parens
# 
# Description
# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
# 
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
# Example: 
# If the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last # parenthesis).


def get_index_closing_parenthesis(s, idx_open):
    """
    :type s: str
    :type idx_open: int

    Method:
    - Init counter to keep track of number of open & close parenthesis
    - Start at the position immediately after the given position & move forward one character at a time
    - Increment counter for every open parenthesis and decrement for closing parenthesis. 
    - Position of matching parenthesis is found when counter = 0

    Complexity:
    - Time: O(n) since we loop over the characters in the string only once
    - Space: O(1) since we only keep track of counter
    """

    if len(s) < 2: raise ValueError("Input string must contain at least 2 characters")
    if idx_open < 0: raise IndexError("Index of opening parenthesis must be >= 0")

    chars = list(s)
    counter = 1
    for i in range(idx_open+1, len(chars)):
        if chars[i] == '(':
            counter += 1
        elif chars[i] == ')':
            counter -= 1

        if counter == 0:
            return i

    raise Exception("No matching closing parenthesis found!")
