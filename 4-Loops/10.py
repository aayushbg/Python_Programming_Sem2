def fibonacci():
    first = 0
    second = 1
    n = int(input("Enter N: "))
    str1 = "0, 1"
    for i in range(n-2):
        str1+=(", "+str(first+second))
        t = first+second
        first=second
        second=t
    print(str1)
fibonacci()