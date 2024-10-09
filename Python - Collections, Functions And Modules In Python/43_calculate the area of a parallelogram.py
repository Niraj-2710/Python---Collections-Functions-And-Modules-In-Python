def calculate_parallelogram_area(B, H):
    if B <= 0 or H <= 0:
        raise ValueError("Base and height must be positive numbers.")
    area = B * H
    return area

B = float(input("Enter the B of the parallelogram : "))
H = float(input("Enter the height of the parallelogram : "))

try:
    area = calculate_parallelogram_area(B, H)
    print(f"The area of the parallelogram is",area,"square units....")
except ValueError as e:
    print(e)