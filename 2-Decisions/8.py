def triangle():
    angle1 = float(input("Enter Angle 1 of Triangle(in degrees): "))
    angle2 = float(input("Enter Angle 2 of Triangle(in degrees): "))
    angle3 = float(input("Enter Angle 3 of Triangle(in degrees): "))
    if(angle1+angle2+angle3==180):
        print("The triangle is valid according to the given values.")
    else:
        print("Triangle is not valid according to given angles.")
triangle()