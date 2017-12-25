# -*- coding: utf-8 -*-

# Corresponds to display_data.py in V1

from __future__ import unicode_literals

import os, sys
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from nltk.corpus import stopwords
from master import *
from Declutter import Declutterer


def _plot_data(word_list, word_count, title, user=None, alias=False):
    """
    Generates the plot image files.
    """
    max_words = min(50, len(word_list))

    # Plot info/settings
    fp = FontProperties('Arial')
    fig = plt.figure(figsize=(19, 13))
    plt.bar(range(max_words), word_count[:max_words], align='center', color='g')
    plt.xticks(range(max_words), word_list[:max_words], size='large', rotation='45', fontproperties=fp)
    plt.gcf().subplots_adjust(bottom=0.15)
    if alias and master_count not in title:
        plt.axes().get_yaxis().set_ticks([])
    plt.title(title, fontsize='30')
    plt.margins(x=0.01)

    if user is None:
        fig.savefig(os.path.join(writepath, title))
    else:
        fig.savefig(os.path.join(writepath, user), dpi=96)


def generate_charts(readfile, writefile='', delimiter=CHAT_DELIMITER,
                    word_delimiter=COUNT_DELIMITER, alias=True, verbose=True):
    """
    Generates the charts by parsing data from the word
    count files. Optionally, aliases all names so that
    all chart labels (title, axis label) contain the
    aliases instead of real names.
    """
    readdir = os.path.join(readpath, readfile)

    # Start with the aggregated data stored in (master_count)
    user = master_count

    # Store data as a dict of dict containing lists of the
    # words, and their counts (elements in each list correspond
    # by index). This is for convenience of use with matplotlib.
    user_word_count = {user: {'tokens': [], 'count': []} for user, _ in namedict.items()}
    user_word_count[master_count] = {'tokens': [], 'count': []}
    newuser = False

    dc = Declutterer()

    print('Reading word counts...')
    with open(readdir, encoding='utf-8', mode='r') as data:
        for i, line in enumerate(data):
            if i == 0 or newuser:
                # Begin processing data for a new user
                user = line.split(delimiter)[0]
                newuser = False
            else:
                newuser = line == '\n' # Detect data for a new user
                if newuser: continue
                try:
                    # Split line into (token, count) then process;
                    # filter unwanted tokens and append the rest into
                    # the word count list. Tokens representing nicknames
                    # are processed into aliases if option enabled.
                    token, count = line.split(word_delimiter)
                    count = int(count.strip())
                    if not dc.filter_word(token):
                        if alias and token in name_to_alias_dict:
                            token = name_to_alias_dict[token]
                        user_word_count[user]['tokens'].append(token)
                        user_word_count[user]['count'].append(count)
                except ValueError as ve:
                    print('ValueError unpacking')
                    try:
                        print(line)
                    except UnicodeEncodeError:
                        print(line.encode('utf-8'))

            if verbose and i % period == 0:
                # Periodically display processed data.
                try:
                    print('Processing line:', str(i) + ',', 'user:', user, 'for display_data.')
                    print(line)
                except UnicodeEncodeError:
                    print('Processing line:', str(i) + ',', 'user:', user.encode('utf-8'), 'for display_data.')
                    print(line.encode('utf-8'))


    print('Done reading word counts.')
    print('Generating plots...')

    # Generate plot png files.
    for user, _ in user_word_count.items():
        _plot_data(user_word_count[user]['tokens'], user_word_count[user]['count'],
                   title='Word count for user %s' % (user if not alias else name_to_alias_dict[user],),
                   user=user if not alias else name_to_alias_dict[user], alias=alias)

    print('Done generating plots!')

if __name__ == '__main__':
    """
    Limited example for modularized usage of this file:
    """

    # generate_charts('1_wordcount.txt', alias=True)

    pass
