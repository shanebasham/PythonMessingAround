import random
import time

print('Lets roll some dice!')

dicetotal = []

yes = 'yes'
while yes == 'yes':
    dice1 = int(input('\nHow big is your dice? '))
    dicetotal.append(dice1)
    counter = 0
    another = yes
    while another == 'yes':
        counter += 1
        another = input('Would you like to add another dice? ')
        if another == 'yes':
            newdice = int(input('How big is your next dice? '))
            dicetotal.append(newdice)
        else:
            for dot in range(0,4):  
                rolling = ('Rolling ' + f'{counter} ' + 'dice' + '.' * dot)
                print(rolling, end='\r')
                time.sleep(.5)
            total = sum(dicetotal)
            roll = random.randint(0, total)
            print(f'\n\nThe dice roll is {roll}!\n')
    no = input('Would you like to roll again? ')
    if no == 'no':
        break
print('\nOk goodbye.\n')