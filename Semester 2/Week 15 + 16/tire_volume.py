
# New tire loop
def yes():
    # Get variables and make them global
    global width
    global ratio
    global diameter
    global volume

    width = int(input('Enter the width of the tire in mm (ex 205): '))
    ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
    diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    # Import math, find volume and print
    import math
    volume = ((math.pi*(width**2)*ratio) * ((width*ratio) + (2540*diameter))) / 10000000000
    print(f'\nThe approximate volume is {volume:.2f} liters\n')

# Loop until user wants to buy tires
def loop():
    y = 'yes'
    while y.startswith('y'):
        y = input('Would you like to buy tires with the dementions you have entered? ').lower()
        if y.startswith('y'):
            global number
            number = input('Ok, what is your phone number? ')
            print('\nThank you! Open volumes.text to view the results. \n')

            # Import datetime and call the now() 
            from datetime import datetime
            current_date_and_time = datetime.now()

            # Open text file volumes.txt in append mode
            with open('volumes.txt', 'at') as volumes_file:
                # Print info
                print(f'{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}', file=volumes_file)
                print(f'Phone number: {number}', file=volumes_file)
            exit()
        else:
            print('\nOk, enter the dementions for a different tire.')
            yes()
            loop()

# Main loops
print('Hello!')
yes()
loop()