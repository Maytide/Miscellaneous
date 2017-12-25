# Corresponds to analyze_data.py in V1

from collections import OrderedDict
from master import *
import sys, os
import operator
import nltk as nltk


def _replace_with_identifiers(name):
    """
    Replaces all nicknames (NOT aliases) with identifiers
    identifier - "real name"
    nickname   - how someone is referred to in chat. In contrast,
                 aliases are the names that will overwrite identifiers
                 when plotting to graph.
    """
    normalized_names = name
    for identifier, nickname in nickname_replace_list:
        normalized_names = normalized_names.replace(nickname, identifier)
    return normalized_names

def get_word_counts(readfile, writefile, delimiter=CHAT_DELIMITER,
                    word_delimiter=COUNT_DELIMITER, verbose=True):
    """
    Obtains the word counts of each word that exists in the chatlog.
    Uses a temporary dict to store this data while counting, for O(n)
    performance, then converts the dict into a list and sorts by
    increasing -> descending word count before writing to file.
    (Is there a better data structure to handle this?)
    """
    chatlog = readfile

    with open(os.path.join(readpath, chatlog), encoding=ENCODING, mode='r') as f:
        chat_text = f.readlines()

    # Store all the word counts in OrderedDict for simplicity
    # in debugging (performance hit over dict is negligible)
    # master_count, the aggregated word count, is treated like
    # a user.
    user_word_count_dicts = OrderedDict()
    for name in [master_count,] + namelist:
        user_word_count_dicts[name] = OrderedDict()

    print('Processing use word count lists...')

    max_key_error = 10
    ke_dict = {}
    for i, line in enumerate(chat_text):
        # First line of file indicating big-little endian-ness causing issue with first name that appears
        line = line.strip('\ufeff')
        line.strip('\n')

        try:
            name, message = line.split(delimiter)
        except ValueError as ve:
            print('Error parsing line', i, ':')
            print(line)
            print(ve, '\n')
            continue

        # Determine whether or not to process a user's data
        name = _replace_with_identifiers(name)
        if name not in namedict:
            if name not in ke_dict:
                ke_dict[name] = 1
            else:
                ke_dict[name] += 1

            if ke_dict[name] < max_key_error:
                print('User:', name, 'not recognized.')
            elif ke_dict[name] == max_key_error:
                print('Reached maximum number of KeyErrors for:', name)

            continue

        # Tokenize the lower case message, to ensure words with different
        # capitalizations are grouped together
        tokenized = nltk.word_tokenize(message.lower())
        # print(tokenized)

        # Count the words
        for token in tokenized:
            if token not in user_word_count_dicts[master_count]:
                user_word_count_dicts[master_count][token] = 1
            else:
                user_word_count_dicts[master_count][token] += 1

            if token not in user_word_count_dicts[name]:
                user_word_count_dicts[name][token] = 1
            else:
                user_word_count_dicts[name][token] += 1

        if verbose and i % period == 0:
            try:
                print('Processing message', i, name, ':', message)
            except UnicodeEncodeError:
                print('Processing message', i, name.encode('utf-8'), ':', message.encode('utf-8'))

    print('Done processing word counts.')
    print('Writing to wordcount log...')

    chatlog_word_count_file = open(os.path.join(writepath, writefile), encoding='utf-8', mode='w')

    # Convert the dict of words to a list, then write the list in
    # order of most used -> least used words to the
    # chatlog_word_count text file
    for user, word_dict in user_word_count_dicts.items():
        chatlog_word_count_file.write(user + delimiter + '\n')
        word_list = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
        for word, count in word_list:
            chatlog_word_count_file.write(word + word_delimiter + str(count) + '\n')
        chatlog_word_count_file.write('\n')

    chatlog_word_count_file.close()

    print('Done writing to wordcount log.')

if __name__ == '__main__':
    """
    Limited example for modularized usage of this file:
    """

    # chatnames = '1.txt'
    # if len(sys.argv) >= 2:
    #     readfile = sys.argv[1]
    # else:
    #     readfile = '_'.join(chatnames) + '.txt' if len(chatnames) > 1 else chatnames[0] + '.txt'
    # if len(sys.argv) >= 3: writefile = sys.argv[2]
    # else: writefile = '_'.join(chatnames) + '_wordcount.txt' if len(chatnames) > 1 else chatnames[0] + '_wordcount.txt'
    # if len(sys.argv) >= 4: delimiter = sys.argv[3]
    # else: delimiter = CHAT_DELIMITER
    #
    # get_word_counts(readfile, writefile, delimiter)

    pass