
print('Enter a list of numbers, type 0 when finished.\n')

numberlist = []

number = 1
while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numberlist.append(number)

sum = sum(numberlist)
print(f'\nThe sum is: {sum}')

count = len(numberlist)
ave = sum / count
print(f'The average is: {ave:.2f}')

largest = 0
for number in numberlist:
    if number > largest:
        largest = number
print(f'The largest number is: {largest}')

sortedlist = sorted(numberlist)
smallest = numberlist[0]
for number in numberlist:
  if number < smallest and number > 0:
    smallest = number
print('The smallest positive number is:', smallest)

print('The sorted list is:')
list = ', '.join(map(str, sortedlist))
print(list)

count = 0
for number in numberlist:
    count += 1
print(f'There are {count} numbers in your list.\n')

