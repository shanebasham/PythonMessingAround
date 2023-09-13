
import random

#main function calls other functions and prints results
def main():
    #print numbers
    numbers = [16.2, 75.1, 52.3]
    print(f'numbers = {numbers}')
    append_random_numbers(numbers)
    print(f'numbers = {numbers}')
    append_random_numbers(numbers, 3)
    print(f'numbers = {numbers}')
    #stretch print words
    words = []
    append_random_words(words)
    print(f'words = {words}')
    append_random_words(words, 5)
    print(f'words = {words}')

#choose and append random numbers
def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)

#choose and append random words from list
def append_random_words(words_list, quantity=1):
    words = ('kiwi plum cherry apple peach grape orange lemon lime mango apricot banana\
    honeydew blueberry blackberry rasberry strawberry pinneapple watermelon pomegranate\
    cantaloupe grapefruit pear guava lychee fig coconut cranberry papaya').split()
    for _ in range(quantity):
        word = random.choice(words)
        words_list.append(word)

main()