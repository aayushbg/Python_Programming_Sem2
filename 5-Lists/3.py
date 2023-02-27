import random
def gen():
    lst = [random.randint(1,30) for i in range(50)]
    print("Original List:",lst)
    for i in lst:
        reps = lst.count(i)
        if(reps>1):
            for j in range(reps-1):
                lst.remove(i)
    lst.sort()
    print("After Deletion",lst)
gen()
