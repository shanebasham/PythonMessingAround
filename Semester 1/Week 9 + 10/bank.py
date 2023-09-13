
print('Enter the names and balances of bank accounts (type: quit when done)')

names = []
balances = []

name = ''
while not name.startswith('q'):
    name = input('What is the name of this account? ').lower()
    if not name.startswith('q'):
        balance = float(input('What is the balance? '))
        names.append(name.capitalize())
        balances.append(balance)

total = 0
print('\nAccount Information:')
for i in range(len(names)):
    print(f'{i+1}. {names[i]} - ${balances[i]:.2f}')
    total += balances[i]

average = (total/len(balances))

print(f'\nTotal: ${total:.2f}')
print(f'Average: ${average:.2f}')

highestname = None
highestbalance = -1
for i in range(len(names)):
    name = names[i].capitalize()
    balance = balances[i]
    if balance > highestbalance:
        highestbalance = balance
        highestname = name
print(f'Highest balance: {highestname} - ${highestbalance:.2f}')

change = 'yes'
while change.startswith('y'):
    change = input('\nDo you want to update an account? ')
    if change.lower().startswith('y'):
        index = int(input('Type number of account index you want to update. '))
        index -= 1
        newamount = float(input('What is the new amount? '))
        balances[index] = newamount
    print('\nAccount Information:')
    for i in range(len(names)):
        print(f'{i+1}. {names[i]} - ${balances[i]:.2f}')
print()