import math

def circumference(radius):
    return 2 * math.pi * radiusr
try:
    r = float(input("Enter the radius of the circle: "))
    if r < 0:
        print(" cant be negative.")
    else:
        circumference2 = circumference(r)
        print(f"The circumference is: {circumference2f}")