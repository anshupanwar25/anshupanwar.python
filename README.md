expenses = []  # list to store only amounts
#Initializes an empty list to hold all expense amounts entered by the user.


while True:
#Starts an infinite loop to keep showing the menu until the user chooses to exit.


    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Save to File")
    print("5. Exit")
#Displays the main menu options to the user.


    choice = input("Enter choice: ")
#Takes user input to choose an option from the menu.

#Option 1: Add Expense
    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added!")
#Prompts the user to enter an amount (converted to float).

#Adds it to the expenses list.

#Confirms that the expense has been added.

#Option 2: View Expenses
   elif choice == "2":
        print("\n--- All Expenses ---")
        for amt in expenses:
            print(f"₹{amt:.2f}")
#Prints all expenses added so far, formatted with two decimal places and a rupee symbol.

#Option 3: Show Summary
    elif choice == "3":
        if expenses:
            total = 0
            for amt in expenses:
                total += amt
            avg = total / len(expenses)
            print(f"\nTotal Expense = ₹{total:.2f}")
            print(f"Average Expense = ₹{avg:.2f}")
        else:
            print("No expenses yet.")
#Calculates:
Total by summing all expenses.
Average by dividing the total by the number of entries.
If no expenses are recorded, it notifies the user.

#Option 4: Save to File
    elif choice == "4":
        with open("expenses.txt", "w") as f:
            for amt in expenses:
                f.write(str(amt) + "\n")
            total = 0
            for amt in expenses:
                total += amt
            avg = total / len(expenses) if expenses else 0
            f.write(f"\nTotal = {total}\n")
            f.write(f"Average = {avg}\n")
        print("✅ Expenses saved to 'expenses.txt'")
#Saves all expenses to a file named expenses.txt
Also writes total and average at the end of the file.
If the list is empty, total and average will both be 0.

#Option 5: Exit
    elif choice == "5":
        print("Exiting...")
        break
#Breaks the loop and ends the program.

#Invalid Input Handling
    else:
        print("Invalid choice, try again.")
#If the user enters a number outside 1–5, this message is shown.
If the user enters a number outside 1–5, this message is shown.
