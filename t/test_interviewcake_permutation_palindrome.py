import pytest
import interviewcake_permutation_palindrome # Module in parent dir found via $PYTHONPATH

def test_empty_string():
    s = ""
    result_bf = interviewcake_permutation_palindrome.is_palindrome_brute_force(s)
    assert result_bf is True
    result_dict = interviewcake_permutation_palindrome.is_palindrome_dict(s)
    assert result_dict is True
    result_set = interviewcake_permutation_palindrome.is_palindrome_set(s)
    assert result_set is True

def test_palindrome():
    s = "civic"
    result_bf = interviewcake_permutation_palindrome.is_palindrome_brute_force(s)
    assert result_bf is True
    result_dict = interviewcake_permutation_palindrome.is_palindrome_dict(s)
    assert result_dict is True
    result_set = interviewcake_permutation_palindrome.is_palindrome_set(s)
    assert result_set is True

def test_permutation_of_palindrome():
    s = "ivicc"
    result_bf = interviewcake_permutation_palindrome.is_palindrome_brute_force(s)
    assert result_bf is True
    result_dict = interviewcake_permutation_palindrome.is_palindrome_dict(s)
    assert result_dict is True
    result_set = interviewcake_permutation_palindrome.is_palindrome_set(s)
    assert result_set is True

def test_non_palindrome_1():
    s = "civil"
    result_bf = interviewcake_permutation_palindrome.is_palindrome_brute_force(s)
    assert result_bf is False
    result_dict = interviewcake_permutation_palindrome.is_palindrome_dict(s)
    assert result_dict is False
    result_set = interviewcake_permutation_palindrome.is_palindrome_set(s)
    assert result_set is False

def test_non_palindrome_2():
    s = "abcde"
    result_bf = interviewcake_permutation_palindrome.is_palindrome_brute_force(s)
    assert result_bf is False
    result_dict = interviewcake_permutation_palindrome.is_palindrome_dict(s)
    assert result_dict is False
    result_set = interviewcake_permutation_palindrome.is_palindrome_set(s)
    assert result_set is False
