
# Your task now is to write a Python program which accepts the radius of a circle from the user and computes area.
import math
def cal_areaofcir(radius):
    return math.pi * radius * radius
radius = float(input("Enter the radius of circle : "))
area = cal_areaofcir(radius)
print(f"The area of the circle with radius {radius} is: {area}")

# Your second task now is to write a Python program to accept a filename from the user and print the extension of that.

filename = input("Enter the name of file : ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

