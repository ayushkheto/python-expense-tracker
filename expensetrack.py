expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter Expense Amount: "))
        category = input("Enter Category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        with open("expenses.txt", "a") as file:
            file.write(f"{amount},{category}\n")

        print("Expense Added Successfully!")

    elif choice == 2:
        try:
            with open("expenses.txt", "r") as file:
                data = file.readlines()

                if len(data) == 0:
                    print("No expenses found!")
                else:
                    print("\nExpenses List:")

                    for line in data:
                        amount, category = line.strip().split(",")

                        print(
                            "Amount:", amount,
                            "| Category:", category
                        )

        except FileNotFoundError:
            print("No expenses found!")

    elif choice == 3:
        total = 0

        try:
            with open("expenses.txt", "r") as file:

                for line in file:
                    amount, category = line.strip().split(",")

                    total += float(amount)

            print("Total Expense:", total)

        except FileNotFoundError:
            print("No expenses found!")

    elif choice == 4:
        print("Thank You for using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Please try again.")