def ls():
    a = int(input("Enter Value 1: "))
    b = int(input("Enter Value 2: "))
    largest=a
    if(a>b):
        print("Largest:",a)
        print("Smallest:",b)
    elif(b>a):
        print("Largest:",b)
        print("Smallest:",a)
    else:
        print("Both Values are equal.")
ls()
        