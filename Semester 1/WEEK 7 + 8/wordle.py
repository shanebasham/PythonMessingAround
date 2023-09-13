import random

CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RED = "\033[0;31m"
END = "\033[0m"

print(f'{CYAN}------------------------------------------------------')
print('Welcome to Wordle!')

playagain = 'yes'
while playagain == 'yes':
    secretword = ('kiwi plum cherry apple peach grape orange lemon lime mango apricot banana\
    honeydew blueberry blackberry rasberry strawberry pinneapple watermelon pomegranate\
    cantaloupe grapefruit pear guava lychee fig coconut cranberry papaya').split()
    hintword = random.choice(secretword)
    hint = '_ ' * len(hintword)

    guesscount = 0
    guess = ''
    
    while guess.lower() != hintword:
        guesscount += 1
        print(f'\n{CYAN}Your hint is: {hint}')
        guess = input(f'\n{CYAN}What is your guess? ')
        if len(guess) == len(hintword):
            if guess == hintword:
                print(f'\nCongrats! The word is {GREEN}{hintword}{END}!')
                print(f'{GREEN}You guessed it in {guesscount} attempts!{END}')
                break
            else:
                hint = ''
                for letter in range(len(hintword)):
                    if guess[letter] == hintword[letter]:
                        hint = hint + GREEN + guess[letter].upper() + END + ' '
                    elif guess [letter] in hintword:
                        hint = hint + YELLOW + guess[letter].lower() + END + ' '
                    else:
                        hint = hint + '_ '
        else:
            print(f'{RED}Your guess is not the same length as the secret word.{END}')
    playagain = input(f'\n{CYAN}Would you like to play again? ')
print('\nThanks for playing!')
print(f'------------------------------------------------------{END}')