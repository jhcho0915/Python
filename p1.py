# p1.py: Cylinder Geometry
# Created By: Jae Cho
# E-mail: jhcho@email.wm.edu
# Find volume and surface area of a cylinder from its radius, height, and width.
# Step 1: Prompt for a radius and echo print the radius.
# Step 2: Do the same for the height and width of the cylinder.
# Step 3: Apply the volume and surface area formulas
# Step 4: Print out the results. (Make sure to round to 3 decimal places)

import math

# Get the input
radius_str = input ("Please enter the cylinder's radius: ")
print (radius_str)
radius = float (radius_str)

height_str = input ("Please enter the cylinder's height: ")
print (height_str)
height = float (height_str)

width_str = input ("Please enter the cylinder's width: ")
print (width_str)
width = float (width_str)

# Calculate the values
volume = math.pi * (2 * radius + width) * width * height
surface_area = 2 * math.pi * (height + width) * (2 * radius + width)

# Output the following results
print()
print("-------------------------------------")
print()
print("   The cylinder's radius = %9.3f" % radius)
print("   The cylinder's height = %9.3f" % height)
print("    The cylinder's width = %9.3f" % width)
print("                  Volume = %9.3f" % volume)
print("            Surface area = %9.3f" % surface_area)
print()
print("-------------------------------------\n")
print("Thank you for using this program.")



       





