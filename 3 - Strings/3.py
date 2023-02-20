def check():
    s1 = input("Enter String 1: ")
    s2 = input("Enter String 2: ")
    if(s1 in s2):
        print(s1,"is present in",s2)
    elif(s2 in s1):
        print(s2,"is present in",s1)
    else:
        print("Either of the strings is not present in the other string.")
check()