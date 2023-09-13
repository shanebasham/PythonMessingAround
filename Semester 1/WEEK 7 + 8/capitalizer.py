
# word = 'commitment'
# favletter = input('What is your favorite letter? ')

# for letter in word:
#     if letter.lower() == favletter.lower():
#         print(letter.upper(), end='')
#     else:
#         print(letter.lower(), end='')
# print()

# for letter in word:
#     if letter.lower() == favletter.lower():
#         print('_', end='')
#     else:
#         print(letter.lower(), end='')
# print()

quote = '\nIn coming days, it will not be possible to survive spiritually without\
the guiding, directing, comforting, and constant influence of the Holy Ghost.\n'

#complicated
playagain = 'yes'
while playagain == 'yes':
    number = int(input('\nPlease enter a number: '))
    for character, letter in enumerate(quote):
        if character % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()
    playagain = input('Would you like to enter another number? ')
print('\nOK Goodbye!')

#functions
def capquote(quote):
    number = int(input('\nPlease enter a number: '))
    newquote = ''
    for letter in range(1, len(quote) + 1):
        if letter % number == 0:
            newquote += quote[letter-1].upper()
        else:
            newquote += quote[letter-1].lower()
    return newquote

playagain = 'yes'
while playagain == 'yes':
    print(capquote(quote))
    playagain = input('Would you like to enter another number? ')
print('\nOK Goodbye!')

#simple
playagain = 'yes'
while playagain == 'yes':
    number = int(input('\nPlease enter a number: '))
    newquote = ''
    for letter in range(1, len(quote) + 1):
        if letter % number == 0:
            newquote += quote[letter-1].upper()
        else:
            newquote += quote[letter-1].lower()
    print(newquote)
    playagain = input('Would you like to enter another number? ')
print('\nOK Goodbye!')
