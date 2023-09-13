
a = ['food', 'water', 'snak', 'dog']
b = ['5', '2', '1', '10']

# print('The contents of the shopping cart are:')
# number = 0
# for item in range(len(a)):
#     number += 1
#     print(f'{number}. {a[item].capitalize()} - ${b[item]}')

# for i in range(len(a)):
#     if a[i] == 0:
#         a.remove(a[i])
#         b.remove(b[i])
#     else:
#         pass

delete = input('Which item would you like to remove? ')
for delete in range(len(a)):
    if a[delete] == a[delete]:
        a.remove(a[delete])
        b.remove(b[delete])
        print('Item removed.')
    break
print(a)
print(b)