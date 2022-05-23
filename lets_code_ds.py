
# Your task now is to write a Python program which accepts the radius of a circle from the user and computes area.
import math
def cal_areaofcir(radius):
    return math.pi * radius * radius
radius = float(input("Enter the radius of circle : "))
area = cal_areaofcir(radius)
print(f"The area of the circle with radius {radius} is: " + str(area))

# Your second task now is to write a Python program to accept a filename from the user and print the extension of that.

fname = input("Enter the name of file : ")

if(fname.endswith(".py")):
    print("The extension of the file is : python")
if(fname.endswith(".c")):
    print("The extension of the file is : c")
if(fname.endswith(".html")):
    print("The extension of the file is : html")
if(fname.endswith(".text")):
    print("The extension of the file is : text")
if(fname.endswith(".js")):
    print("The extension of the file is : javascript")