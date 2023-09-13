import random
playagain = "yes"
while playagain == "yes":
    magicnumber = random.randint(1, 100)
    guesscount = 0
    guess = -1
    while guess != magicnumber:
        guess = int(input("What is your guess? "))
        guesscount += 1
        if guess < magicnumber:
            print("Higher")
            print()
        elif guess > magicnumber:
            print("Lower")
            print()
        else:
            print("You guessed it!")
            print()
    print(f"It took you {guesscount} guesses")
    playagain = input("\nWould you like to play again? ")
print("\nThank you for playing!")