# Question / Problem Statement: Create a console-based Expense Tracker
# program in Python that allows the user to record daily expenses and view
# summaries like total spending. Use only the concepts learned till Chapter 6
# (loops, conditionals, lists, dictionaries, and basic input/output).

# Expense tracker project

expensesList = []  # List of all the expenses in form of dictionary

print("Welcome to Expense Tracker!")

while True:
    print("=== MENU ===")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Please enter your choice : "))

    # 1. ADD Expense
    if(choice == 1):
        date = input("Please enter the Date (formate - dd/mm/yyyy) : ")
        category = input("Please enter the Category (Food, Travel, Statinary, etc..) : ")
        description = input("Please enter the short Description : ")
        amount = float(input("Please enter the Amount : "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount,
        }

        expensesList.append(expense)
        print("\n Done, Expense is added successfully!")

    # 2. View All Expenses
    elif(choice == 2):
        if len(expensesList) == 0:
            print("No Expenses Added.")
        else:
            print("=== This is your all expenses ===")
            
            count = 1
            
            for e in expensesList:
                print(f"Expense no {count} -> {e['date']}, {e['category']}, {e['description']}, {e['amount']}")
                count += 1

    # 3. View total Spending
    elif(choice == 3):
        total = 0
        for etotal in expensesList:
            total += etotal['amount']
        
        print("\n Total Spend = ", total)

    # 4. Exit  
    elif(choice == 4):
        print("Thank you for using Expense Tracker App.")
        break

    # 5. If use type any other then 1 to 4 numbers
    else:
        print("INVALID CHOICE. TRY AGAIN")