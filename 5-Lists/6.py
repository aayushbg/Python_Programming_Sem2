def convert():
    temp=[]
    for i in range(5):
        temp.append(float(input("Enter Temperature: ")))
    c=0
    for i in temp:
        temp[c]=(5/9)*(i-32)
        c+=1
    print("Converted Temperatures:",temp)
convert()