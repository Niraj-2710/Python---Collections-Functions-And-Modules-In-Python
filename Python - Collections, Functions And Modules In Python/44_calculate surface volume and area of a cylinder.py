import math

R = float(input("Enter cylinder the radius  : "))
H = float(input("Enter cylinder the height  : "))

surface_area = 2 * math.pi * R * (R + H)

volume = math.pi * R ** 2 * H

print("Surface Area : ", surface_area)
print("Volume : ", volume)