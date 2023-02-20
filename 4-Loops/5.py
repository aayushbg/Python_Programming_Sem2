def triplets():
    rec=[]
    for i in range(1,31):
        for j in range(1,31):
            for k in range(1,31):
                if((i*i)+(j*j)==(k*k)):
                    l1 = [i,j,k]
                    l1.sort()
                    if(l1 not in rec):
                        rec.append(l1)
                        print(i,",",j,",",k,"are Pythagorean Triplets.")
triplets()