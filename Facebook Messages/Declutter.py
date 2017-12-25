from nltk.corpus import stopwords


class Declutterer:
    """
    Cleans up raw text containing unwanted tokens such as stopwords and links.
    """
    nonwords = set('[]+=\'')

    @staticmethod
    def filter_list(word_list, remove_stopwords=True, remove_short_strings=True, remove_nonwords=True,
                   remove_links=True):
        """
        Filters words in a list; can probably be more efficient using
        python's build in `filter` function, but this function isn't
        being used as of right now so I'll leave it like this.

        If remove_stopwords is False, remove_short_strings is True and the word is
        a short stopword, the priority will be to still filter it.
        """
        filtered_word_list = []
        for i, (word, count) in enumerate(word_list):
            if ((not remove_stopwords or word not in stopwords.words('english')) and
                    (not remove_short_strings or len(word) > 2) and
                    (not remove_nonwords or not any(character in Declutterer.nonwords for character in word)) and
                    (not remove_links or 'http' not in word)):

                filtered_word_list.append(word)

        return filtered_word_list

    @staticmethod
    def filter_word(word, remove_stopwords=True, remove_short_strings=True, remove_nonwords=True,
                   remove_links=True):
        """
        Checks whether a single word should be filtered or not.

        If remove_stopwords is False, remove_short_strings is True and the word is
        a short stopword, the priority will be to still filter it.
        """
        filter = True
        if ((not remove_stopwords or word not in stopwords.words('english')) and
                (not remove_short_strings or len(word) > 2) and
                (not remove_nonwords or not any(character in Declutterer.nonwords for character in word)) and
                (not remove_links or 'http' not in word)):
            filter = False

        return filter
