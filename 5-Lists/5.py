def convert():
    l1 = []
    for i in range(5):
        l1.append(str(input("Enter A String: ")))
    c=0
    for i in l1:
        l1[c]=str(i).upper()
        c+=1
    print("Converted List:",l1)
convert()