def ls():
    num1 = int(input("Enter Value 1: "))
    num2 = int(input("Enter Value 2: "))
    num3 = int(input("Enter Value 3: "))
    if(num1>num2 and num1>num3):
        if(num2>num3):
            print("Largest:",num1)
            print("Smallest:",num3)
        else:
            print("Largest:",num1)
            print("Smallest:",num2)
    elif(num2>num3 and num2>num1):
        if(num1>num3):
            print("Largest:",num2)
            print("Smallest:",num3)
        else:
            print("Largest:",num2)
            print("Smallest:",num1)
    elif(num3>num1 and num3>num2):
        if(num1>num2):
            print("Largest:",num3)
            print("Smallest:",num2)
        else:
            print("Largest:",num3)
            print("Smallest:",num1)
    else:
        print("All Three Values are Same.")
ls()


