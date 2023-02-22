import string


def sanitize_token(token):
    """
    Sanitize a single token.

    :param token: A single token from a line of text
    :return: The word with any punctuation and casing removed
    """
    word = ""

    for character in token:
        if character.isalpha():
            word = word + character.lower()

    return word


def sanitize_string(string):
    """
    Break a string into a list of words.

    :param string: A line of text
    :return: A list of words, with any punctuation and casing removed
    """
    # The "split" function breaks a string into a list of strings, by default,
    #  any whitespace is used as the delimiter.
    tokens = string.split()
    words = []

    for token in tokens:
        words.append(sanitize_token(token))

    return words


def count_words(words):
    """
    Count the words in a list.

    :param words: A list of words, with any punctuation and casing removed
    :return: A dictionary mapping words to frequencies
    """
    frequencies = {}
    
    for word in words:
        # Note that the values in a dictionary could be anything -- they need
        #  not be integers, and the interpreter has no way of knowing that
        #  nonexistent values ought to default to zero.
        if word != "":
            if word in frequencies:
                frequencies[word] = frequencies[word] + 1
            else:
                frequencies[word] = 1

    return frequencies


def main():
    # Each word will be mapped to its frequency by a dictionary -- this is
    #  better than a list, because it allows us to use the words as the keys,
    #  to lookup information using words instead of searching for them.
    string = input("Enter a line of text: ")
    words = sanitize_string(string)
    frequencies = count_words(words)

    # We need the information in this dictionary in sorted order, but a
    #  dictionary is unordered. We must first convert it into a list, keeping
    #  in mind that we will later need both keys and their values.
    lst = [[frequencies[key], key] for key in frequencies] 

    # When sorting a nested list, the default behavior is to first compare the
    #  first element of each nested list, so the frequencies will need to be
    #  the first elements and the words can then be the second elements.
    lst.sort(reverse = True)

    for word in lst[:10]:
        print("%s (%d)" % (word[1], word[0]))


if __name__ == "__main__":
    main()
