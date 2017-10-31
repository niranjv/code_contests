import pytest
import interviewcake_matching_parenthesis # Module in parent dir found via $PYTHONPATH

def test_empty_string():
    s = ""
    with pytest.raises(Exception) as e:
        interviewcake_matching_parenthesis.get_index_closing_parenthesis(s, 0)
    assert str(e.value) == "Input string must contain at least 2 characters"

def test_string_with_1_char():
    s = "a"
    with pytest.raises(Exception) as e:
        interviewcake_matching_parenthesis.get_index_closing_parenthesis(s, 0)
    assert str(e.value) == "Input string must contain at least 2 characters"

def test_negative_open_index():
    s = "ab"
    with pytest.raises(Exception) as e:
        interviewcake_matching_parenthesis.get_index_closing_parenthesis(s, -1)
    assert str(e.value) == "Index of opening parenthesis must be >= 0"

def test_only_open_close():
    s = "()"
    idx_close = interviewcake_matching_parenthesis.get_index_closing_parenthesis(s, 0)
    assert idx_close == 1

def test_sample_string():
    s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
    idx_close = interviewcake_matching_parenthesis.get_index_closing_parenthesis(s, 10)
    assert idx_close == 79

def test_no_matching_closing_parenthesis():
    s = "Sometimes (when I nest them"
    with pytest.raises(Exception) as e:
        interviewcake_matching_parenthesis.get_index_closing_parenthesis(s, 10)
    assert str(e.value) == "No matching closing parenthesis found!"
