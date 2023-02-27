import random
def sort():
    odd=[]
    even=[]
    for i in range(5):
        odd.append(2*(random.randint(0,49))+1)
    print("List of Odd Numbers:",odd)
    for i in range(4):
        even.append(2*(random.randint(0,50)))
    print("List of Even Numbers:",even)
    odd[2]=even
    print("List of Odd Numbers after replacing the third element:",odd)
    final_list=[]
    for i in odd:
        if i==even:
            for j in even:
                final_list.append(j)
        else:
            final_list.append(i)
    final_list.sort()
    print("Final List after Flattening and Sorting:",final_list)
sort()