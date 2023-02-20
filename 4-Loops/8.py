def fact():
    num = int(input("Enter the Number: "))
    factorial = 1
    for i in range(1,num+1):
        factorial*=i
    print("Factorial of",num,"=",factorial)
fact()