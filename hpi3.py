def calculate_monthly_expenses():
    # Dictionary to store categories with preset expenses
    expenses = {
        "Rent": 600,
        "Utilities": 150,
        "Food": 250,
        "Transport": 100,
        "Entertainment": 80,
        "Other": 50
    }

    print("=== Monthly Expenses Calculation ===\n")

    # Print each category's monthly expense
    print("Monthly expense details:")
    for category, amount in expenses.items():
        print(f"{category}: €{amount:.2f}")

    # Calculate the total monthly expenses
    total_monthly_expenses = sum(expenses.values())
    print(f"\nTotal monthly expenses: €{total_monthly_expenses:.2f}")

    # Calculate the total annual expenses
    total_annual_expenses = total_monthly_expenses * 12
    print(f"Total annual expenses: €{total_annual_expenses:.2f}")

    # Calculate and display the percentage of each category relative to the monthly total
    print("\nPercentage of each category relative to the monthly total:")
    for category, amount in expenses.items():
        percentage = (amount / total_monthly_expenses) * 100
        print(f"{category}: {percentage:.2f}%")


# Run the function
calculate_monthly_expenses()
