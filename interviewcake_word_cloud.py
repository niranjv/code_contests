# URL: https://www.interviewcake.com/question/python/word-cloud
# 
# Description
# You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.
# To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary, where the keys are words and the values # are the number of times the words occurred.
# 
# Think about capitalized words. For example, look at these sentences:
# 
#  'After beating the eggs, Dana read the next step:'
# 'Add milk and eggs, then add flour and sugar.'
# 
# What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should include one "Add" or "add" with a value of 22. Make reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".
# 
# Assume the input will only contain words and standard punctuation.


import operator

def get_word_counts(s):
    """
    * Exclude all punctuation surrounding a word
    * Use lowercase words only even if word only appears in uppercase in string
    * This methods gives O(n) time solution. Alternative method of using split() & then checking each word gives O(n2) time solution
    """

    word_counts = {}

    cur_word_index = None
    cur_word_length = 0

    for i, c in enumerate(s):

        c = s[i]

        if c.isalpha():
            if cur_word_index is None: 
                cur_word_index = i

            cur_word_length += 1

        else:

            if c == '-':
                if s[i-1].isalpha() and s[i+1].isalpha():
                    print("Found - as part of hyphenated word")
                    continue

            # this can happen if the last char is a punctutation
            if cur_word_index is not None:
                word = s[cur_word_index:cur_word_index+cur_word_length]
                word = word.lower()
                
                # will result in single letter words like s resulting from possessive 's
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

                cur_word_index = None
                cur_word_length = 0


    # Add last word
    word = s[cur_word_index:cur_word_index+cur_word_length]
    word = word.lower()

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

    return word_counts



if __name__ == "__main__":

    s = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.The bill came to five dollars. Last"
    word_counts = get_word_counts(s)
    sorted_words = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    
    for i in sorted_words:
        print(i)

