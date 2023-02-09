#x1(y2-y3)+x2(y3-y1)+x3(y1-y2)=0
def line():
    x1 = float(input("x-coordinate of point-1: "))
    y1 = float(input("y-coordinate of point-1: "))
    x2 = float(input("x-coordinate of point-2: "))
    y2 = float(input("y-coordinate of point-2: "))
    x3 = float(input("x-coordinate of point-3: "))
    y3 = float(input("y-coordinate of point-3: "))
    if(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)==0):
        print("All the three points are collinear.")
    else:
        print("The three points are not collinear.")
line()
