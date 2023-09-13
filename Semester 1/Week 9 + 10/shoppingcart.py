
print('Welcome to the Shopping Cart Program!')

shoppinglist = []
pricelist = []

def menu():
    print('\nPlease select one of the following:')
    print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
    action = input('Please enter an action: ')
    if action == '1':
        item = input('\nWhat item would you like to add? ')
        shoppinglist.append(item.lower())
        price = float(input(f'What is the price of "{item.capitalize()}"? '))
        pricelist.append(price)
        print(f'"{item.capitalize()}" has successfully been added to the cart. ')
        while 1 == 1:
            yes = input('\nWould you like to add another item? ')
            if yes.lower().startswith('y'):
                item = input('What item would you like to add? ')
                shoppinglist.append(item.lower())
                price = float(input(f'What is the price of "{item.capitalize()}"? '))
                pricelist.append(price)
                print(f'"{item.capitalize()}" has successfully been added to the cart. ')
            else:
                print('OK')
                menu()
    elif action == '2':
        if len(shoppinglist) == 0:
            print('Oops! Your cart is empty!\nTry adding items to your cart.')
            menu()
        print('The contents of the shopping cart are:')
        number = 0
        for i in range(len(shoppinglist)):
            newpricelist = [str(x) for x in pricelist]
            print(f'{i + 1}. {shoppinglist[i].capitalize()} - ${newpricelist[i]:.2f}')
        menu()
    elif action == '3':
        delete = int(input('\nEnter number of item you would like to remove. '))
        while delete > len(shoppinglist):
            print('You have entered a number not in the list, please try again.')
            delete = int(input('\nEnter number of item you would like to remove. '))
        shoppinglist.pop((delete-1))
        pricelist.pop((delete-1))
        print('Item removed.')
        menu()
    elif action == '4':
        total = sum(pricelist)
        itemcount = 0
        for i in enumerate(shoppinglist):
            itemcount += 1
        if itemcount == 1:
            item = 'item'
            print(f'\nThe total price of your {itemcount} {item} is ${total:.2f}.')
        else:
            item = 'items'
            print(f'\nYou have {itemcount} {item} in your shopping cart, the total price is ${total:.2f}')
        menu()
    elif action == '5':
        print('\nThank you, goodbye.\n')
        exit()
menu()