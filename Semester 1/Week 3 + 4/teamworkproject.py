print('Welcome to the velocity calculator. Please enter the following:')
print()

mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter: '))
time = float(input('Time (in seconds): '))
density = float(input('Density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water): '))
cross_sectional_area = float(input('Cross sectional area of projectile (in square meters): '))
drag_constant = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

import math

#v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
inner_value = (1/2) * density * cross_sectional_area * drag_constant
velocity = math.sqrt((mass) * (gravity)/(inner_value)) * (1 - math.exp((- math.sqrt((mass) * (gravity) * (inner_value))/(mass)) * (time)))

#v_terminal = sqrt(mg/c)
velocity_terminal = math.sqrt((mass) * (gravity)/(inner_value))

print()
print(f'Inner value of c is {inner_value:.3f}')
print(f'The velocity after {time} seconds is {velocity:.3f} m/s')
print(f'The terminal velocity is {velocity_terminal:.3f} m/s')
time = .01
velocity = math.sqrt(mass*gravity/inner_value) * (1 - math.exp((- math.sqrt(mass * gravity * inner_value)/mass * time)))
while velocity != velocity_terminal:
    velocity = math.sqrt(mass*gravity/inner_value) * (1 - math.exp((- math.sqrt(mass * gravity * inner_value)/mass * time)))
    time =+.01
    print(f'The velocity after {time} seconds is: {velocity:.3f}')
    print()
    exit()