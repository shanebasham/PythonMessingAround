canride = False

age1 = int(input('What is the age of the first rider? '))
height1 = int(input('What is the height of the first rider? '))

if age1 >= 12 and age1 < 18:
    passport1 = input('Does this rider have a golden passport? ')

rider2 = input('Is there a second rider? ')

if rider2.lower() == 'yes':
    age2 = int(input('What is the age of the second rider? '))
    height2 = int(input('What is the height of the second rider? '))

    if 12 <= age2 <= 18:
        passport2 = input('Does this rider have a golden passport? ')
    if height1 < 36 or height2 < 36:
        canride = False
    else:
        if age1 >= 18 or age2 >= 18 or passport1.lower() == 'yes' or passport2.lower() == 'yes':
            canride = True
        else:
            if age1 >= 12 and height1 >= 52 and age2 >= 12 and height2 >= 52:
                canride = True
            elif (age1 >= 16 and age2 >= 14) or (age1 >= 14 and age2 >= 16):
                canride = True
            else:
                canride = False
else: 
    if (age1 >= 18 or passport1.lower() == 'yes') and height1 >= 62:
        canride = True
    else:
        canride = False

if canride:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you can not ride.')