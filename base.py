'''
                  ___
                 /   \
                | . . |
                 \ o /
                  | |
             
                 ?????
                 
Welcome to the ??? Chatbot

Created on ???
@author: ???
'''
from __future__ import print_function
import sys

def reply(fulltext):
    '''
        Function takes a text string and calculates an appropriate reply
    '''

    text = fulltext.lower()

    if text.startswith('hello') or text.startswith('hi'):
        return 'Hi'

    if text[-1] == '?':
        return "I don't know"

    else:
        return "I don't understand"
    

print(
r'''
                  ___
                 /   \
                | . . |
                 \ o /
                  | |
             
                 ?????

Say something!
''')
try:
    while True:
        # Prompt for user input
        # Note: Python 2 and 3 deal with user input slightly differently. The lines below make
        # sure that the code runs the same on both versions.
        if sys.version.startswith('2'):
            fulltext = raw_input('')
        else:
            fulltext = input('')
        # Calculate the reply and print it in the terminal
        print('>>> ' + reply(fulltext) + '\n')
except KeyboardInterrupt:
    print('>>> Goodbye\n')
