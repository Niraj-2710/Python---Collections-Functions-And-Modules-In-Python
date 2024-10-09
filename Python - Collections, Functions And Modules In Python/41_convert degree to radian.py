import math

def deg_to_rad(deg):
    R = D * (math.pi / 180)
    return R

D = float(input("Enter a degree value : "))
R = deg_to_rad(D)
print(D,"degrees is equal to",R,"radians")