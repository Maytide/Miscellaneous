# Corresponds to 'parse.py' in V1

from lxml.html import parse
from master import *
import os, sys


# Stores simplified message text in file as
# Name, DELIMITER, message text
# ENCODING = 'ISO-8859-1'

# Fetch the entire conversation contained in file
# div 'thread' class contains everything
def process_html_to_chatlog(readfiles, writefile, delimiter=CHAT_DELIMITER,
                            verbose=True):
    """
    Convert HTML to readable text chatlog.
    """
    ####################################
    print('Cleaning HTML...')
    # - Trivial method to remove newline characters inside <p> elements that cause xpath to intepret them
    #   as multiple lines
    # - Remove empty <p>'s
    raw_html_all = ''
    for readfile in readfiles:
        chat_html = open(os.path.join(readpath, readfile), encoding=ENCODING, mode='r')
        raw_html = chat_html.read()
        raw_html = raw_html.replace('\n', ' ')
        raw_html = raw_html.replace('<p></p>', '<p> </p>')
        raw_html_all += '/n' + raw_html
        chat_html.close()

    readfile_clean = '_'.join([readfile.split('.')[0] for readfile in readfiles]) + '_clean.html'
    chat_html_clean = open(os.path.join(readpath, readfile_clean), encoding=ENCODING, mode='w')
    chat_html_clean.write(raw_html_all)
    chat_html_clean.close()

    print('Done cleaning HTML.')
    ####################################

    print('Building chat content from HTML...')
    chatlog = open(os.path.join(writepath, writefile), encoding=ENCODING, mode='w')

    # Should be only 1 thread in facebook's new download format
    chat_html = parse(os.path.join(readpath, readfile_clean)).getroot()
    main_classes = chat_html.find_class('thread')

    # Fetch all the messages from HTML
    messages, names = [], []
    for i, thread_class in enumerate(main_classes):
        user = thread_class.find_class('user')

        # Will not distinguish if two people have same name
        for username in user:
            names.append(username.text_content())

        current_thread_messages = thread_class.xpath("p/text()") # https://stackoverflow.com/questions/11007527/xpath-to-get-all-text-in-element-as-one-value-removing-line-breaks

        messages.extend(current_thread_messages)
    print('Done building chat content from HTML.')
    print('Building chatlog...')

    for index, message_data in enumerate(messages):
        if verbose and index % period == 0:
            try:
                print('Currently adding message #', index, names[index], ':')
                print(message_data)
            except UnicodeEncodeError:
                print('Currently adding message #', index, names[index].encode('utf-8'), ':')
                print(message_data.encode('utf-8'))
        # Write messages to chatlog
        chatlog.write(names[index] + delimiter + message_data.replace('\n', ' ').replace('\r\n', ' ') + '\n')

    chatlog.close()
    print('Done building chatlog.')

if __name__ == '__main__':
    """
    Limited example for modularized usage of this file:
    """

    # if len(sys.argv) >= 2:
    #     readfiles = sys.argv[1].split(',')
    #     chatnames = [readfile.split('.')[0] for readfile in readfiles]
    # else:
    #     pass
    #     readfiles = ('1.html',)
    #     chatnames = ('1',)
    # if len(sys.argv) >= 3: writefile = sys.argv[2]
    # else: writefile = '_'.join(chatnames) + '.txt' if len(chatnames) > 1 else chatnames[0] + '.txt'
    # if len(sys.argv) >= 4: delimiter = sys.argv[3]
    # else: delimiter = CHAT_DELIMITER
    #
    # process_html_to_chatlog(readfiles, writefile, delimiter)

    pass