import math
def pnc():
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    ncr = (math.factorial(n))/math.factorial(n-r)
    npr = (math.factorial(n))/(math.factorial(r) * math.factorial(n-r))
    print("nCr:",ncr)
    print("nPr",npr)
pnc()