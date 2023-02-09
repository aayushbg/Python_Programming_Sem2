def check():
    length = float(input("Enter Length of Rectangle: "))
    breadth = float(input("Enter Breadth of Rectangle: "))
    if((length*breadth)>(2*(length+breadth))):
        print("Area of the Rectangle is greater than its perimeter.")
    elif((length*breadth)<(2*(length+breadth))):
        print("Area of the Rectangle is less than its perimeter.")
    else:
        print("Area and Perimeter of the Rectangle are equal.")
check()