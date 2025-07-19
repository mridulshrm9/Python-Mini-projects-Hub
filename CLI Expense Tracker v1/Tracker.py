print("Welcome to the Tracker!")
name = input("Enter your name: ")
age = input("Enter your age: ")
goods = []
bool = True
spendings = 0

while (bool == True):
    print("1. Add a new expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Please enter your choice (1-3): ")

    if choice == '1':
        amount = int(input("Enter the amount you have spent: "))
        type = input("Enter the type of item you purchased: ")
        goods.append(type)
        spendings = spendings + amount
        print(f"Added expense of {amount} for {type}. Total spendings: {spendings}")

    if choice == '2':
        print("Your expenses:")
        for item in goods:
            print(f"- {item}")
        print(f"Total spendings: {spendings}")
    
    if choice == '3':
        print("Exiting the Tracker. Goodbye!")
        bool = False


