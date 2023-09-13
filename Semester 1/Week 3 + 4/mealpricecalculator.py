import math
pchild = float(input('What is the price of a childs meal? '))
padult = float(input('What is the price of an adults meal? '))
pdrinkl = float(input('What is the price of a large drink? '))
pdrinks = float(input('What is the price of a small drink? '))
nchild = int(input('How many children are there? '))
nadult = int(input('How many adults are there? '))
ndrinkl = float(input('How many large drinks did you buy? '))
ndrinks = float(input('How many small drinks did you buy? '))
str = float(input('What is the sales tax rate? '))
print()

subtotal = (pchild * nchild) + (padult * nadult) + (pdrinkl * ndrinkl) + (pdrinks * ndrinks)
salestax = (subtotal * str) / 100
total = subtotal + salestax

print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${salestax:.2f}')
print(f'Total: ${total:.2f}')
print()
yes = input(f'Would you like to add a tip? ')
if yes.lower() == 'yes':
    tippercent = input('What percent would you like to tip? ')
    tip = float(tippercent.strip('%'))
    tiptotal = ((tip / 100) * total)  + total
    print()
    print(f'Total with tip: ${tiptotal:.2f}')
    print()
    cash = float(input('What is the payment amount? '))
else:
    print('OK :(')
    cash = float(input('What is the payment amount? '))
    print()
    change = cash - total
    while change < 0:
        print('You need more money! :/')
        cash = float(input('Please enter new payment amount: '))
        change = cash - total
        if change >= 0:
            print()
            print(f'Your change is: ${change:.2f}')
            print()
            print('Enjoy your meal! :)')
            print()
            exit()
change = cash - tiptotal
while change < 0:
    print('You need more money! :/')
    newcash = float(input('Please enter new payment amount: '))
    newchange = newcash - tiptotal
    if newchange >= 0:
        print()
        print(f'Your change is: ${newchange:.2f}')
        print()
        print('Enjoy your meal! :)')
        print()
        exit()