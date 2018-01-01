# Corresponds to simulate.py in V1

import os, sys
import markovify
import nltk
import re
from master import *


joke_word = '' # Replace empty strings (and not yet implemented: and unwanted words) with this word.
def clean_text_for_markovify(readfile, user=None, writefile=None,
                             delimiter=CHAT_DELIMITER):
    """
    Output text file with all of a user's messages formatted
    in sentences on a single line, to comply with Markovify's
    preferred input method.
    """

    # Preprocessing
    if writefile is None:
        if user is not None:
            writefile = user + '_feed_data.txt'
        else:
            writefile = 'master_feed_data.txt'
    else:
        pass

    print('Cleaning text for simulation...')

    chatlog = readfile
    readdir = os.path.join(readpath, chatlog)
    with open(readdir, encoding=ENCODING, mode='r') as f:
        chat_text = f.readlines()

    message_list = []
    name_list = []

    # Clean text for simulation by replacing empty strings, then
    # append them to message/name_list
    for line in chat_text:
        try:
            name, message = line.split(delimiter)
            if user is not None and name != user: continue
            if not message:
                message = joke_word
            message_list.append(message.replace('\n', ''))
            name_list.append(name)
        except ValueError:
            # print('stop shitposting')
            print('Unable to parse line:', line)
            continue

    simulation_log = os.path.join(writepath, writefile)
    feed_data_file = open(simulation_log, encoding=ENCODING, mode='w')

    print('Done cleaning text for simulation.')
    print('Writing cleaned text...')

    # Write to the feed_data file which will be processed by Markovify
    for name, message in zip(name_list, message_list):
        if user is None or name == user:
            feed_data_file.write(' ')
            feed_data_file.write(message)
            feed_data_file.write('.')
        else:
            pass

    feed_data_file.close()
    print('Done writing cleaned text...')

    return writefile


class POSifiedText(markovify.Text):
    """
    https://github.com/jsvine/markovify#extending-markovifytext
    Use nltk's part-of-speech (POS) tagger for generating sentences
    with more natural structure:
    """
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ '::'.join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = ' '.join(word.split('::')[0] for word in words)
        return sentence


def simulate_chat(readfile, user=None, writefile=None, simulations=50,
                  max_sentence_length=150):
    """
    Generate Markovified text from the cleaned feed_data file.
    """

    # Preprocessing
    if writefile is None:
        if user is not None:
            writefile = user + '_markovified.txt'
        else:
            writefile = 'master_markovified.txt'
    else:
        pass

    print('Preparing chat simulation...')

    feed_data = readfile
    messagelog = open(os.path.join(readpath, feed_data), encoding=ENCODING, mode='r')
    text = messagelog.read()
    messagelog.close()

    # Generate the Markov chain text model
    text_generator = POSifiedText(text)

    print('Done preparing chat simulation...')

    print('Writing markovified text.')

    # Generate sentences
    message_output_file = open(os.path.join(writepath, writefile), encoding=ENCODING, mode='w')
    for i in range(simulations):
        message_output_file.write(text_generator.make_short_sentence(max_sentence_length))
        message_output_file.write('\n')

    print('Done writing markovified text. Returning from simulate_chat')

    return writefile


if __name__ == '__main__':
    """
    Limited example for modularized usage of this file:
    """

    # if len(sys.argv) >= 2:
    #     user = sys.argv[1].replace('_', ' ')
    # else:
    #     user=None
    # cleaned_text_file = clean_text_for_markovify('1.txt', user=user)
    # simulate_chat(cleaned_text_file, user=user)

    pass
