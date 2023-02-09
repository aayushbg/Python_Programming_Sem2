def check():
    r = float(input("Enter the Radius of the circle: "))
    x1 = float(input("Enter x-coordinate of the center: "))
    y1 = float(input("Enter y-coordinate of the center: "))
    x = float(input("Enter x-coordinate of the point: "))
    y = float(input("Enter y-coordinate of the point: "))
    val = ((x-x1)**2) + ((y-y1)**2)
    if(val<(r*r)):
        print("The point lies inside the circle.")
    elif(val==(r*r)):
        print("The point lies on the circle.")
    else:
        print("The point lies outside the circle.")
check()
    