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
    :type s: string

    Method:
    - Track the number of chars appearing an odd number of times
    - Add a char to the set when we see it an odd number of times and remove it when we see if an even number of times
    - At most 1 char can appear an odd number of times for a word to be a palindrome

    Complexity: 
    - Time: O(n) since we loop over all characters in the string
    - Space: O(k) where k = size of alphabet since string can have all letters in the alphabet
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
    :type s: string

    Method:
    - Construct a dictionary with character as key and number of times it appears in the string as its value
    - Loop over all keys in the dictionary and count the number of keys that have an odd value
    - At most 1 char can appear an odd number of times for a word to be a palindrome
    - Note: This method is subject to integer overflow if a character appears a very large number of times in the input string

    Complexity: 
    - Time: O(n) + O(k) = O(n) since we loop over all characters in the string (k = |alphabet|)
    - Space: O(k) since string can have all letters in the alphabet
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
    :type s: string

    Method:
    - Get list of all permutations of input string 
    - Compare each permutation to its reverse to determine if any permutation is a palindrome
    - A string is a palindrome only when it is equal to its reverse

    Complexity:
    - Time:  O(n!) * O(n) = O(n!n) O(n!) to loop through all permutations and O(n) to compare permutation to its reverse
    - Space: O(n!n) since we need to store n! strings, each of length n
    """

    palin = {}
    for p in permutations(s):
        p = "".join(p)
        if p == p[::-1]: # compare string to its reverse
            return True

    return False
