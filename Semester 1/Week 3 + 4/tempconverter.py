degrees_f = float(input("What is the temperature in Fahrenheit? "))
degrees_c = (degrees_f - 32) * 5 / 9

print(f"The temperature in Celsius is {degrees_c:.1f} degrees.")
print()

degreesc = float(input("What is the temperature in Celsius? "))
degreesf = (degreesc * (9 / 5)) + 32

print(f"The temperature in Fahrenheit is {degreesf:.1f} degrees.")
print()