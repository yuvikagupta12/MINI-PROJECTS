# ATM Machine Program

balance = 10000  # Initial Balance

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            balance += amount
            print("Deposit Successful!")
            print("Updated Balance: ₹", balance)
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "3":
        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Withdrawal Successful!")
                print("Remaining Balance: ₹", balance)

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "4":
        print("Thank You for Using ATM!")
        break

    else:
        print("Invalid Choice!")