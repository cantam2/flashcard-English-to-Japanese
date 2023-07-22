
import random

from termcolor import colored

d = {
    'apple': 'りんご',
    'banana': 'バナナ',
    'peach': 'もも'
}

template = '*'*15 + '\nEnglish:{}\nJapanese\n' + '*'*15

while True:

    word = random.choice(
        list(d.keys())
        )
    print(colored(
       template.format(word), 'yellow'
       ))
       
    answer = input()
    print(answer)


    if answer == '0':
        print('Perfect! take your time:)')
        break
    if answer == d[word]:
        print(colored('correct', 'green'))
    else:
        print(colored('uncorrect', 'red'))
