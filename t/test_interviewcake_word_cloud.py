import pytest
import interviewcake_word_cloud # Module in parent dir found via $PYTHONPATH

def test_empty_string():
    s = ""
    with pytest.raises(Exception) as e:
        interviewcake_word_cloud.get_word_counts(s)
    assert str(e.value) == "String must have at least 1 character"

def test_with_1_word():
    s = "a"
    expected_dict = {"a": 1}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_with_1_nonword():
    s = "!"
    expected_dict = {}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_with_1_hyphenated_word():
    s = "Sugar-free"
    expected_dict = {"sugar-free": 1}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_with_words_only():
    s = "Test Me"
    expected_dict = {"test": 1, "me": 1}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_with_nonwords_only():
    s = "!@#$%^&*()"
    expected_dict = {}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_with_hyphenated_words_only():
    s = "Sugar-free sugar-free full-length long-distance sun-dried part-time"
    expected_dict = {"sugar-free": 2, "full-length": 1, "long-distance": 1, "sun-dried": 1, "part-time": 1}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_ending_with_words():
    s = "Test me again"
    expected_dict = {"test": 1, "me": 1, "again": 1}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_ending_with_punctuation():
    s = "Test me now!"
    expected_dict = {"test": 1, "me": 1, "now": 1}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_same_words_different_case():
    s = "TEST test ME ME me now now Now!!!"
    expected_dict = {"test": 2, "me": 3, "now": 3}
    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict

def test_sample_string():
    s = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake. The bill came to five dollars."
    expected_dict = {}
    expected_dict['we'] = 4
    expected_dict['came'] = 2
    expected_dict['bill'] = 2
    expected_dict['saw'] = 1
    expected_dict['conquered'] = 1
    expected_dict['then'] = 1
    expected_dict['ate'] = 1
    expected_dict['s'] = 1
    expected_dict['mille-feuille'] = 1
    expected_dict['cake'] = 1
    expected_dict['the'] = 1
    expected_dict['to'] = 1
    expected_dict['five'] = 1
    expected_dict['dollars'] = 1

    result_dict = interviewcake_word_cloud.get_word_counts(s)
    assert expected_dict == result_dict
