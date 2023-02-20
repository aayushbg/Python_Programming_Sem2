def check():
    num = int(input("Enter the Number: "))
    prime = 1
    perfect = 0
    armstrong = 0
    palindrome = 0
    automorphic = 0
    for i in range(2,num):
        if(num%i==0):
            prime=0
            break
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if(sum==num):
        perfect=1
    cubes=0
    digs = str(num)
    for i in digs:
        cubes=cubes+((int(i))**3)
    if(cubes==num):
        armstrong=1
    if(digs[::-1]==digs):
        palindrome=1
    square = str(num*num)
    if(digs==square[len(digs)*-1:]):
        automorphic=1
    print(num,"is a Prime Number") if prime==1 else print(num,"is not a Prime Number.")
    print(num,"is a Perfect Number") if perfect==1 else print(num,"is not a Perfect Number.")
    print(num,"is a Armstrong Number") if armstrong==1 else print(num,"is not a Armstrong Number.")
    print(num,"is a Palindrome.") if palindrome==1 else print(num,"is not a Palindrome.")
    print(num,"is Automorphic") if automorphic==1 else print(num,"is not Automorphic.")
check()