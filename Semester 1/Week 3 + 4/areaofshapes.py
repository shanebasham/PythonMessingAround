# Area of square
side = float(input('Enter the length of a side of the square in cm: '))
if side == 0:
    side = float(input(('Please enter a new number: ')))
area = side ** 2
print(f'The area of the square is {area} cm^2 or {area / 10000} m^2')
print()
# Area of rectangle
length = float(input('Enter the length of rectangle in cm: '))
width = float(input('Enter the width of the rectangle in cm: '))
area = length * width
print(f'The area of the rectangle is {area} cm^2 or {area / 10000} m^2')
print()
# Area of circle
import math
radius = float(input('Enter the radius of a circle: '))
area = math.pi * (radius ** 2)
print(f'The area of the circle is {area:.3f} cm^2 or {area / 10000:.3f} m^2')
print()
# One value
x = float(input('Enter a lenth: '))
area_square = x ** 2
area_circle = math.pi * (x ** 2)
volume_cube = x ** 3
volume_sphere = (4 / 3) * math.pi * (x ** 3)
print(f'Area of square: {area_square}')
print(f'Area of circle: {area_circle:.3f}')
print(f'Volume of cube: {volume_cube}')
print(f'Volume of sphere: {volume_sphere:.3f}')
print()
print('YAY MATH!')
print()