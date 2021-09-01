# Python Program for Program to find area of a circle
radius = int(input("Enter Radius: "))

def area_of_circle(radius):
    area = 3.14*radius*radius
    return area

result = area_of_circle(radius)
print("Area of circle is whose radius {0} is:".format(radius),result)