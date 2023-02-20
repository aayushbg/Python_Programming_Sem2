def rev():
    n = int(input("Enter a Number: "))
    c=1
    for i in range(1,n+1):
       print(i+n-c,end=", ")
       c+=2
rev()