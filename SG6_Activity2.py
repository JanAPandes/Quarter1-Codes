# Libraries for Math Operations Activity #2
import math

def x_axis_points(x1,x2):

    '''

    The x axis in calculating Euclidean distance

    d = sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

    '''
    
    xformula = math.pow(x2 - x1, 2)
    return xformula

def y_axis_points(y1,y2):
    '''
    
    The y axis in calculating Euclidean distance

    d = sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)
    
    '''

    yformula = math.pow(y2 - y1, 2)
    return yformula

# --- Main Program ---
x1_input = float(input("Enter x1:"))
y1_input = float(input("Enter y1:"))

x2_input = float(input("Enter x2:"))
y2_input = float(input("Enter y2:"))

final_x = x_axis_points(x1_input,x2_input)
final_y = y_axis_points(y1_input,y2_input)

d = math.sqrt(final_x + final_y)

d_round = round(d,2)
print("The distance between the two points is:", d_round)