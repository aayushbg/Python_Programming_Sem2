def result():
    m1 = float(input("Enter Marks of Subject 1: "))
    m2 = float(input("Enter Marks of Subject 2: "))
    m3 = float(input("Enter Marks of Subject 3: "))
    print("Total Marks: ",m1+m2+m3)
    print("Average Marks: ",(m1+m2+m3)/3)
    r = [m1,m2,m3]
    if(min(r)<=39):
        print("Result: Fail")
    else:
        print("Result: Pass")
    c=0
    for i in r:
        c+=1
        if(i<40):
            print("Grade in Subject",c,":","F")
        elif(40<=i<45):
            print("Grade in Subject",c,":","P")
        elif(45<=i<50):
            print("Grade in Subject",c,":","C")
        elif(50<=i<55):
            print("Grade in Subject",c,":","B")
        elif(55<=i<60):
            print("Grade in Subject",c,":","B+")
        elif(60<=i<70):
            print("Grade in Subject",c,":","A")
        elif(70<=i<80):
            print("Grade in Subject",c,":","A+")
        else:
            print("Grade in Subject",c,":","O")
result()
