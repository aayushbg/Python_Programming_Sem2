import math
def sin():
    s = float(input("Enter x in degrees for sin(x): "))
    rad = (math.pi/180)*s
    n = int(input("Upto how many terms you want to calculate: "))
    val=0
    c=0
    for i in range(1,(2*n),2):
        val+=(((-1)**c)*(rad**i)/(math.factorial(i)))
        c+=1
    print("The value of sin(x):",val)
sin()