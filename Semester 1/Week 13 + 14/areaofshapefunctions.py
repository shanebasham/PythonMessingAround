import math

# Easy one value for all!
x = float(input('Enter a lenth: '))
area_square = x * x
area_circle = math.pi * x * x
volume_cube = x ** x
volume_sphere = (4 / 3) * math.pi * (x ** 3)
print(f'Area of square: {area_square}')
print(f'Area of circle: {area_circle:.3f}')
print(f'Volume of cube: {volume_cube}')
print(f'Volume of sphere: {volume_sphere:.3f}')
print('YAY MATH!')

# Area of square
def areaofsquare(side):
    return side * side

# Area of rectangle
def areaofrectangle(length, width):
    return length * width

# Area of circle
def areaofcircle(radius):
    return math.pi * radius * radius

# Main loop
shapes = ['square', 'rectangle', 'circle']
shape = ''
while shape != 'q':
    shape = input('\nWhat is your shape? ').lower()
    if shape.startswith('q'):
        print('Ok goodbye!')
        break
    while shape not in shapes:
        shape = input('Try a different shape: ').lower()
    if shape == 'square':
        side = float(input('Enter the length of a side of the square in cm:  '))
        while side <= 0:
            side = input('Please enter a different length: ')
        area = areaofsquare(side)
        print(f'The area is {area}')
    elif shape == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        area = areaofrectangle(length, width)
        print(f'The area of the rectangle is {area} cm^2 or {area / 10000} m^2')
    elif shape == 'circle':
        radius = float(input('What is the radius? '))
        area = areaofcircle(radius)
        print(f'The area of the circle is {area:.3f} cm^2 or {area / 10000:.3f} m^2')

                    # STRETCH #
# Make it complicated for some reason
def findarea(shape, value1, value2=0):
    area = 0
    if shape == 'square':
        area = areaofsquare(value1)
    elif shape == 'circle':
        area = areaofcircle(value1)
    elif shape == 'rectangle':
        area = areaofrectangle(value1, value2)
    return area

# Main loop
shape = ''
while shape != 'q':
    shape = input('\nWhat is your shape? ').lower()
    if shape.startswith('q'):
        print('Ok goodbye!')
        break
    while shape not in shapes:
        shape = input('Try a different shape: ').lower()
    if shape == 'square':
        side = float(input('Enter the length of a side of the square in cm:  '))
        while side <= 0:
            side = input('Please enter a different length: ')
        area = findarea(side)
        print(f'The area is {area}')
    elif shape == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        area = findarea(length, width)
        print(f'The area of the rectangle is {area} cm^2 or {area / 10000} m^2')
    elif shape == 'circle':
        radius = float(input('What is the radius? '))
        area = findarea(radius)
        print(f'The area of the circle is {area:.3f} cm^2 or {area / 10000:.3f} m^2')

