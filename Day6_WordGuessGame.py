# Hangman Game

# Pick a random number
from random_word import RandomWords
r = RandomWords()
# get a single word # r.get_random_words() to get a list of random words
word = r.get_random_word()
n = len(word)
# print(word, n)
a = 5


def listToString(s):
    str1 = " "
    return (str1.join(s))


display_list = []
for x in range(n):
    display_list.append('_ ')

display = listToString(display_list)
print(display)

b = 0

while a > 0:
    if '_ ' not in display_list:
        b = 1
        break
    # Remember to lower the cases
    char = input(f'Please guess a character ({a} chances):\n').lower()
    if char in word:
        for x in range(n):
            if display_list[x] == '_ ' and word[x] == char:
                display_list[x] = char + ' '
            else:
                continue
        display = ''
        display = listToString(display_list)
        print(display)
    else:
        a -= 1
        print(f'Failed Guess. {a} chances left.\n{display}')

if b == 1:
    print('You Win!')
else:
    print(f'You Lost. The word is {word}.')

# Another listToString method:
# print(f'{' '.join(display)}')
# string.join(iterable)
