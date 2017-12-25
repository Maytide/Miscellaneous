"""
Does all the steps required to generate graphs. Optionally, generates
markovified text as well.
"""

import os, sys
import argparse
from master import *
from html_to_chatlog import process_html_to_chatlog
from get_word_counts import get_word_counts
from display_data import generate_charts
from simulate_chat import simulate_chat, clean_text_for_markovify

if __name__ == '__main__':
    assert len(sys.argv) >= 2

    """
    Preprocessing
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('readfiles')
    parser.add_argument('--user', default=None)
    parser.add_argument('--delimiter', default=CHAT_DELIMITER)
    parser.add_argument('--simulate', default=False)
    parser.add_argument('--alias', default=False)
    args = parser.parse_args()
    readfiles = args.readfiles
    user = args.user
    delimiter = args.delimiter
    alias = bool(args.alias)
    simulate = bool(args.simulate)

    if simulate:
        print('Option to simulate is enabled; will process simulation after generating graphs.')
    else:
        print('Option to simulate is disabled; will still perform other tasks.')

    if ',' in readfiles:
        readfiles = readfiles.split(',')
    else:
        readfiles = (readfiles,)

    chatnames = [readfile.split('.')[0] for readfile in readfiles]
    chatlog = '_'.join(chatnames) + '.txt' if len(chatnames) > 1 else chatnames[0] + '.txt'
    chatlog_word_count = '_'.join(chatnames) + '_wordcount.txt' if len(chatnames) > 1 else chatnames[0] + '_wordcount.txt'

    # Verbose processing by default
    print('Beginning processing...')

    """
    Generates chat html file -> chatlog with Name: Message
    using provided delimiter
    """
    process_html_to_chatlog(readfiles, chatlog, delimiter)
    print('Chatlog saved to file:', chatlog)

    """
    Generates chatlog -> text file with word: count for each user
    """
    get_word_counts(chatlog, chatlog_word_count, delimiter)
    print('Word counts saved to file:', chatlog_word_count)

    """
    Generates charts from each user's word count
    """
    generate_charts(readfile=chatlog_word_count, alias=alias)

    """
    Generates Markov text
    """
    if simulate:
        cleaned_text_file = clean_text_for_markovify(readfile=chatlog, user=user)
        simulation_file = simulate_chat(cleaned_text_file, user=user)
        print('Simulated text saved to file:', simulation_file)

    print('Finished processing everything.')
