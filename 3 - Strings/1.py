def count():
    str1 = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    c=0
    for i in str1:
        if(i in vowels):
            c+=1
    print("Number of vowels in the string:",c)
count()