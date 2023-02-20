def mul_table():
    n = int(input("Enter a Number: "))
    i = int(input("Print Multiplication Table Upto What Number: "))
    c=0
    while(c<=i):
        print(n,"x",c,"=",n*c)
        c+=1
mul_table()