# ------------------------------------------------------------
# Name: anshu panwar
# Date: October 10, 2025
# Lab Title: Simple Expense Tracker
# Course: Foundations of Programming using Python (ETCCPP103)
# ------------------------------------------------------------
# Description:
# This program allows users to record daily expenses under categories
# such as Food, Travel, etc. It then displays a summary with total and
# average expenses. It demonstrates the use of lists, loops, arithmetic
# operations, string formatting, and basic file handling (bonus).
# ------------------------------------------------------------

# Task 1: Setup & Introduction
print("------------------------------------------------------------")
print("        Welcome to the Simple Expense Tracker App!          ")
print("------------------------------------------------------------")
print("This tool helps you record your daily expenses by category,")
print("and shows your total and average spending.\n")

# Task 2: Input & Data Collection
categories = []  # list to store categories
amounts = []     # list to store amounts

while True:
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))

    categories.append(category)
    amounts.append(amount)

    more = input("Do you want to add more? (yes/no): ").strip().lower()
    if more != 'yes':
        break

# Task 3: Expense Calculations
total_expense = sum(amounts)
average_expense = total_expense / len(amounts) if amounts else 0

# Task 4: Neatly Formatted Output
print("\nExpenses Record")
print("---------------")
for i in range(len(categories)):
    print(f"{categories[i]} - {amounts[i]:.2f}")

print(f"\nTotal Expense: {total_expense:.2f}")
print(f"Average Expense: {average_expense:.2f}")

# Bonus Task: Save data to a file
with open("expense_record.txt", "w") as file:
    file.write("Expenses Record\n")
    file.write("---------------\n")
    for i in range(len(categories)):
        file.write(f"{categories[i]} - {amounts[i]:.2f}\n")
    file.write(f"\nTotal Expense: {total_expense:.2f}\n")
    file.write(f"Average Expense: {average_expense:.2f}\n")

