import getpass
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
balances = [1000.0, 2000.0, 3000.0]

def authenticate():
    """Handles user login and PIN verification."""
    print("\n--- ATM LOGIN ---")
    user = input("Enter Username: ").lower()
    
    if user not in users:
        print("Invalid Username.")
        return None
    
    index = users.index(user)
    attempts = 3
    
    while attempts > 0:
        
        pin = getpass.getpass("Enter PIN: ")
        
        if pin == pins[index]:
            print(f"Login Successful! Welcome, {user}.")
            return index
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempts remaining.")
            
    print("Card Locked due to too many failed attempts.")
    return None

def atm_menu(user_index):
    """Main transaction loop."""
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Select Option (1-5): ")
        
        if choice == '1':
            print(f"Current Balance: ${balances[user_index]:.2f}")
            
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > 0:
                    if amount <= balances[user_index]:
                        balances[user_index] -= amount
                        print(f"Withdrawal Successful! New Balance: ${balances[user_index]:.2f}")
                    else:
                        print("Insufficient Funds.")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balances[user_index] += amount
                    print(f"Deposit Successful! New Balance: ${balances[user_index]:.2f}")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == '4':
            new_pin = getpass.getpass("Enter New PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                confirm = getpass.getpass("Confirm New PIN: ")
                if new_pin == confirm:
                    pins[user_index] = new_pin
                    print("PIN Changed Successfully.")
                else:
                    print("PINs do not match.")
            else:
                print("Invalid PIN format. Must be 4 digits.")
                
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid Option.")


if __name__ == "__main__":
    user_idx = authenticate()
    if user_idx is not None:
        atm_menu(user_idx)   