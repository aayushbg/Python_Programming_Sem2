def stack_program():
    stack = [] 
    while True:  
        print("\nSELECT APPROPRIATE CHOICE")                    
        print("1. PUSH Element into the Stack")  
        print("2. POP Element from the Stack") 
        print("3. Display Elements of the Stack")  
        print("4. Exit")  
        choice = int(input("Enter the Choice:"))
        if choice == 1:   
            stack.append(input("Enter Element you want to PUSH into stack: "))   
        elif choice == 2:
            if len(stack) == 0:
                print('The STACK is EMPTY ,No element can POP out')                
            else:       
                print('\nElement POP out from the STACK is:')  
                print(stack.pop())
        elif choice == 3:
            if len(stack) == 0:                       
                print('The STACK is initially EMPTY')
            else:
                print("The Size of the STACK is: ",len(stack))            
                print('\nSTACK elements are as follows:')            
                print(stack)    
        elif choice == 4:  
            break  
        else:  
            print("Incorrect Choice")
stack_program()