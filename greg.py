'''
                 .___.
                //|||\\
                (-@-@-)
                 \ o /
                  | |
             
                 GREG~
                 
Welcome to the Greg Chatbot

Created on 31/07/17
@author: Emma Tattershall and Greg Corbett
'''
from __future__ import print_function
import sys
import random

def reply(fulltext):
    '''
        Function takes a text string and calculates an appropriate reply
    '''

    text = fulltext.lower()

    if text.startswith('hello') or text.startswith('hi'):
        return 'Hello'

    for question in ["whats your name",
                     "what's your name",
                     "who are you",
                     "what are you called"]:
        if question in text:
            return 'Greg~'

    for question in ["how old are you",
                     "what's your age",
                     "whats your age"]:
        if question in text:
            return 'Older than you'

    if text[-1] == '?':
        if random.random() < 0.33:
            return "~Science~"
        elif random.random() < 0.66:
            return "Compute!"
        else:
            return "Let me get back to you about that"

    else:
        if random.random() < 0.2:
            return "Mmmh-hmmm"
        elif random.random() < 0.4:
            return "Hmmm"
        elif random.random() < 0.6:
            return "It's confusing!"
        else:
            return "Oooooh"
    

print(
r'''
                 .___.
                //|||\\
                (-@-@-)
                 \ o /
                  | |
             
                 GREG~

Say something
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
