# This program simulates a single transaction -
# either a deposit or a withdrawal - at a bank.

balance = 1000
user_choice = input("Deposit or withdrawal: ").lower()

if user_choice == "deposit":
    amount = int(input("Enter amount: "))
    balance += amount
    print(f"Final balance: {balance}")
        
elif user_choice == "withdrawal":
    amount = int(input("Enter amount: "))
    if amount > balance:
        print("You cannot have a negative balance!")
    else:
        balance -= amount
        print(f"Final balance: {balance}")

else:
    print("Invalid transaction.")