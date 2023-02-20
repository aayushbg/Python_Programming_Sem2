def hours():
    for i in range(1,25):
        if(0<=i<12):
            print(str(i)+":00 AM")
        elif(12<i<24):
            print(str(i)+":00 PM")
        elif(i==12):
            print(str(i)+":00 Noon")
        elif(i==24):
            print("0:00 Midnight")
hours()