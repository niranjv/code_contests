# URL: https://www.interviewcake.com/question/python/matching-parens
# 
# Description
# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
# Example: If the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last # parenthesis).



def get_index_closing_parenthesis(s, idx_open):
    """
    :type s: str
    :type idx_open: int
    """

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


if __name__ == "__main__":

    s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
    idx_close = get_index_closing_parenthesis(s, 10)
    print("Index of matching closing parenthesis = " + str(idx_close))
