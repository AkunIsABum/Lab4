import math

def degreeToRadian():
    d = float(input("Input degree: "))
    r = math.radians(d)

    print("Output radian: ", r)

def areaTrapezoid():
    h = float(input("Height: "))
    b1 = float(input("Base, first value: "))
    b2 = float(input("Base, second value: "))
    area = 0.5 * (b1 + b2) * h

    print("Expected Output: ", area)

def areaPolygon():
    sides = int(input("Input number of sides: "))
    side_length = float(input("Input the length of a side: "))
    area = (sides * side_length**2) / (4 * math.tan(math.pi / sides))

    print("The area of the polygon is: ", area)

def areaParall():
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))

    print("Expected Output:", base * height)
