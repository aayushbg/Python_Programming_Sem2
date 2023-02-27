import random

def pos_neg():
    l1 = [random.randint(-50,50) for i in range(30)]
    pos=[]
    neg=[]
    print("Generated List",l1)
    for i in l1:
        if(i>0):
            pos.append(i)
        elif(i<0):
            neg.append(i)
    print("List Having Positive Numbers:",pos)
    print("List Having Negative Numbers",neg)
pos_neg()