# can_sizes.py
import math 
import itertools


def main():
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    radius_of_can = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height_of_can = [10.16, 11.91, 11.59, 11.91, 17.76, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    for x in range(len(radius_of_can)):
        can_r = radius_of_can[x]
        can_h = height_of_can[x]
        # print(can_names[x], radius_of_can[x], height_of_can[x])
        can_volume = compute_volume(can_r, can_h)
        can_sa = compute_surface_area(can_r, can_h)
        efficiency = float(can_volume) / float(can_sa)
        print(f'{can_names[x]} {efficiency:.2f}')

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

if __name__ == "__main__":
    main()