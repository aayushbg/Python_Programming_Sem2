def remove():
    s1 = input("Enter the string you want to change: ")
    s2 = input("Enter the string you want to remove: ")
    len_remove = len(s2)
    i = s1.find(s2)
    print("Final String is:",s1[:i] + s1[i+len_remove:])
remove()