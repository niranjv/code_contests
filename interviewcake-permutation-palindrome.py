# URL: https://www.interviewcake.com/question/python/permutation-palindrome
# 
# Description:
# Write an efficient function that checks whether any permutation of an input string is a palindrome. 
# You can assume the input string only contains lowercase letters.
# 
# Examples:
# - "civic" should return True
# - "ivicc" should return True
# - "civil" should return False
# - "livci" should return False


from itertools import permutations


def is_palindrome_set(s):
    """
    Track the number of chars appearing an odd number of times
    At most 1 char can appear an odd number of times
    Complexity: Time = O(n); space = O(k) where k = size of alphabet
    """

    odd = set()
    for c in s:
        if c in odd:
            odd.remove(c)
        else:
            odd.add(c)

    return len(odd) <= 1


def is_palindrome_dict(s):
    """
    Track the number of times each char appears in the string
    At most 1 char can appear odd number of times; all other chars must appear an even number of times
    Complexity: Time: O(n); space = O(k) but subject to integer overflow is a char appears a very large number of times in string
    """

    char_count = {}

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    num_even = num_odd = 0

    for k, v in char_count.items():
        if v % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

    return num_odd <= 1


def is_palindrome_brute_force(s):
    """
    Get list of all permutations of input string and compare each to its reverse to determine if any permutation is a palindrome
    Complexity is O(n!n) - n! to loop through each permutation and n to compare permutation to its reverse
    """

    palin = {}
    for p in permutations(s):
        p = "".join(p)
        if p == p[::-1]:
            return True


if __name__ == "__main__":

    s = "civil"
    print(is_palindrome(s))


