
import math

#find storage efficiency (se) and print all cans
def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#2"
    radius = 8.73
    height = 11.59
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#5"
    radius = 13.02
    height = 14.29
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#6Z"
    radius = 5.4
    height = 8.89
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#10"
    radius = 15.72
    height = 17.78
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#211"
    radius = 6.83
    height = 12.38
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#300"
    radius = 7.62
    height = 11.27
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

    name = "#303"
    radius = 8.1
    height = 11.11
    volume = find_v(radius, height)
    sa = find_sa(radius, height)
    se = volume / sa
    print(f"{name} {se:.2f}")

#function to find volume(v)
def find_v(radius, height):
    volume = math.pi * radius**2 * height
    return volume

#function to find surface area(sa)
def find_sa(radius, height):
    sa = 2 * math.pi * radius * (radius + height)
    return sa

main()