bal=10000 
while True: 
    print("......Enter your choice......") 
    print("1. Deposite") 
    print("2. Withdrawal") 
    print("3. Check balance") 
    print("4. Exit") 
    choice=int(input("Enter your choice: ")) 
    if choice==1: 
        amt=int(input("Enter amount to deposit: ")) 
        bal += amt 
        print(amt,"is successfully deposited.Now your balance is ",bal) 
    elif choice==2: 
        amt=int(input("Enter amount to withdraw: ")) 
        if amt<=bal: 
            bal -= amt 
            print( amt, "has withdrawed. Now your balance is ",bal) 
        else: 
            print("Insufficient balance.") 
    elif choice==3: 
        print("Your balance is :", bal) 
    elif choice==4: 
        print("Thank you for visiting...") 
        break 
    else: 
        print("Enter valid choice.") 
 
 
 
