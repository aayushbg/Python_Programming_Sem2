def count():
    s1 = input("Enter the string: ")
    alpha = 0
    dig = 0
    for i in s1:
        if(i.isalpha()):
            alpha+=1
        elif(i.isdigit()):
            dig+=1
    print("Number of Alphabets:",alpha)
    print("Number of Digits:",dig)
count()