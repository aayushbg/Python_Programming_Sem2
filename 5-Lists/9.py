def func():
    l1=[]
    l2=[]
    l3=[]
    for i in range(5):
        l1.append(int(input("Enter Number for List 1:")))
        l2.append(int(input("Enter Number for List 2:")))
    for i in l1:
        if i not in l2:
            l3.append(i)
    print("Third List:",l3)
func() 