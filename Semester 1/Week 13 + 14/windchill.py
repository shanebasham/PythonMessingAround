
# find wind chill for fahrenheit
def find_windchill(temp, wind):
    windchill = 35.74 + (0.6215 * temp) - 35.75 * (wind ** 0.16) + (0.4275 * temp) * (wind ** 0.16)
    return windchill

# convert celsius to fahrenheit
def c_to_f(temp):
    temp = temp * (9/5) + 32
    return temp

# find wind chill for celsius
def find_celsius(temp, wind):
    windchill = 35.74 + (0.6215 * c_to_f(temp)) - 35.75 * (wind ** 0.16) + (0.4275 * c_to_f(temp)) * (wind ** 0.16)
    return windchill

# get tempurature in fahrenheit or celsius, loop to make sure f or c is typed
def findtemp():
    temp = float(input('What is the temperature? '))
    f_or_c = input('Fahrenheit or Celsius (F/C)? ').lower()
    while f_or_c != 'f' or f_or_c != 'c':
        if f_or_c == 'f':
            for wind in range(5, 65):
                if wind % 5 == 0:
                    print(f'At temperature {temp}F, and wind speed {wind}mph, the windchill is: {find_windchill(temp, wind):.2f}F')
            break
        elif f_or_c == 'c':
            print(f'{temp}C is equal to {c_to_f(temp)}F')
            for wind in range(5, 65):
                if wind % 5 == 0:
                    print(f'At temperature {c_to_f(temp)}C, and wind speed {wind}mph, the windchill is: {find_celsius(temp, wind):.2f}F')
            break
        else:
            f_or_c = input('Please enter Fahrenheit or Celsius (F/C): ')

# loop to ask user to search again
yes = 'yes'
while yes.lower().startswith('y'):
    findtemp()
    yes = input('Would you like to search again? ')
print('Ok bye!')
