# Libraries for Input/Output (I/O) Operations Code #2
import math

def circle_area():
    '''

    Get the radius in square units.

    Uses the formula πr^2

    '''

    radius = float(input("Input the radius of the circle:"))
    if radius < 0:
        print("Error, radius cannot be negative.")
        return
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f} square units.")
    return area

circle_area()


