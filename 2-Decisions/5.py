def min_maj():
    age = int(input("Enter your age in years: "))
    status = "Minor" if (age<18) else "Major"
    print("The person is:",status)
min_maj()