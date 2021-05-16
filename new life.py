#finding area of the circle

from math import pi
r = float(input("enter the radius of a circle = "))
A = pi*r**2
print("Area of the circle is = ",A)


#print extension of the file

File_name = input("Enter the file name: ")
print("The file name:",File_name)
File_ex = File_name.split(".")
print("The extension of the file: " + repr(File_ex[-1]))

 
