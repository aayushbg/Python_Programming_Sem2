import random
def pos():
    rand_list = [random.randint(0,10) for i in range(20)]
    print("Generated Random List:",rand_list)
    num = int(input("Enter the Integer: "))
    positions = []
    c=0
    for i in rand_list:
        if(i==num):
            positions.append(c)
        c+=1
    if (len(positions)==0):
        print("No such Number in the List.")
    else:
        print("Positions(Index) of Integer",num,"in List:",positions)
pos()
