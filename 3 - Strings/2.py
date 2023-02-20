def convert():
    s1 = input("Enter a String: ")
    lower=""
    upper=""
    toggle=""
    for i in s1:
        uni=ord(i)
        if i.isalpha()==False:
            lower+=i
            upper+=i
        if i.isalpha() and i.islower():
            lower+=i
            upper+=(chr(uni-32))
        if i.isalpha() and i.isupper():
            lower+=(chr(uni+32))
            upper+=i
    first=ord(s1[0])
    if (s1[0].isalpha() and s1[0].isupper()):
        toggle+=chr((first+32))
    else:
        toggle+=(chr(first))
    c=0
    for i in s1:
        if(c==0):
            c+=1
            continue
        uni=ord(i)
        if i.isalpha() and (s1[c-1]==" "):
            c+=1
            if(i.isupper()):
                toggle+=(chr(uni+32))
                continue
            else:
                toggle+=i
                continue
        c+=1
        if i.isalpha()==False:
            toggle+=i
        if i.isalpha() and i.islower():
            toggle+=(chr(uni-32))
        if i.isalpha() and i.isupper():
            toggle+=i
    print("Lower Case:",lower)
    print("Upper Case:",upper)
    print("Toggle Case:",toggle)
convert()