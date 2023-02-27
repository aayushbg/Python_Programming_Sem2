def queue():
    queue = [] 
    while True:  
        print("\nSELECT APPROPRIATE CHOICE")                    
        print("1. PUSH Element into the queue")  
        print("2. POP Element from the queue") 
        print("3. Display Elements of the queue")  
        print("4. Exit")  
        choice = int(input("Enter the Choice:"))
        if choice == 1:   
            queue.append(input("Enter Element you want to PUSH into queue: "))   
        elif choice == 2:
            if len(queue) == 0:
                print('The queue is EMPTY ,No element can POP out')                
            else:
                ele = queue[0]       
                print('\nElement POP out from the queue is:',ele)  
                queue.remove(ele)
        elif choice == 3:
            if len(queue) == 0:                       
                print('The queue is initially EMPTY')
            else:
                print("The Size of the queue is: ",len(queue))            
                print('\nqueue elements are as follows:')            
                print(queue)    
        elif choice == 4:  
            break  
        else:  
            print("Incorrect Choice")
queue()