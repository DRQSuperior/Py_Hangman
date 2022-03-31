from concurrent.futures import wait
import random

vars = {
    'word_list': ['apple', 'banana', 'orange', 'pear', 'pineapple', 'strawberry', 'watermelon'],
    'guesses': [],
    'guess_limit': 6,
    'guess_count': 0,
    'word': '',
    'word_length': 0,
    'guess_input': '',
}

def generate_word():
    vars['word'] = random.choice(vars['word_list'])
    vars['word_length'] = len(vars['word'])

generate_word()

def creategame():
    print('The word starts with: ' + vars['word'][0])
    print('The word ends with: ' + vars['word'][-1])
    vars['guess_input'] = input('Guess a word: ')
    if vars['guess_input'] == vars['word']:
        print('Correct!')
    else:
        print('Incorrect!')
        vars['guess_count'] += 1
        if vars['guess_count'] == vars['guess_limit']:
            print('The word was: ' + vars['word'])
            print('You ran out of guesses!')
            playagain = input('Would you like to play again? (y/n) ')
            if playagain == 'y':
                generate_word()
                creategame()
            else:
                print('Thanks for playing!')
                exit()
        else:
            print('You have ' + str(vars['guess_limit'] - vars['guess_count']) + ' guesses left.')
            creategame()


creategame()
