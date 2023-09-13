
import random

hangman = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = ('fig kiwi plum pear cherry apple peach grape guava orange lemon lime mango banana\
    apricot honeydew blueberry blackberry rasberry strawberry pinneapple watermelon pomegranate\
    cantaloupe grapefruit lychee coconut cranberry papaya').split()

def getRandomWord(wordlist):
    word = random.randint(0, len(wordlist) - 1)
    return wordlist[word]

def displayBoard(missedLetters, correctLetters, secretword):
    print(hangman[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretword)
    for i in range(len(secretword)): # Replace blanks with correctly guessed letters.
        if secretword[i] in correctLetters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the
    # player entered a single letter and not something else.
    while True:
        guess = input('Guess a letter. ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
        
def playagain():
    print('Do you want to play again? ')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretword = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretword)
    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretword:
        correctLetters = correctLetters + guess
        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' + secretword + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(hangman) - 1:
            displayBoard(missedLetters, correctLetters, secretword)
            print('You have run out of guesses!\nAfter ' +
              str(len(missedLetters)) + ' missed guesses and ' +
              str(len(correctLetters)) + ' correct guesses, the word was "' + secretword + '"')
            gameIsDone = True

    if gameIsDone:
        if playagain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretword = getRandomWord(words)
        else:
            print('\nThanks for playing!\n')
            break