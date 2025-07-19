print("Welome to the Password Vault!")
user_list = []
pass_list = []

app = []
passw = []

bool = True

while bool == True:
    user = input("Are you a new user or an existing user? (new/existing) or you want to exit: ").strip().lower()

    if user == "new":
        print("Please create a new account.")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            exit()
    
        user_list.append(username)
        pass_list.append(password)
        print(f"Account created for {username}. You can now log in.")

    elif user == "existing":
        print("Please log in to your account.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username not in user_list or password not in pass_list:
            print("Invalid username or password. Please try again.")
        else:
            while True:
                action = input("Do you want to add a new app password or exit? (add/exit): ").strip().lower()
                if action == "exit":
                    print("Exiting the vault. Goodbye!")
                    break
                elif action == "add":
                    app_name = input("Enter the name of the app: ")
                    app_password = input("Enter the password for the app: ")
                    app.append(app_name)
                    passw.append(app_password)
                    print(f"Password for {app_name} has been saved successfully.")
                else:
                    print("Invalid action. Please type 'add' to add a new app password or 'exit' to exit.")
    
    elif user == "exit":
        print("Exiting the vault. Goodbye!")
        bool = False