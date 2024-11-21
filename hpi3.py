import matplotlib.pyplot as plt

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

    # Display the percentage of each category relative to the monthly total
    print("\nPercentage of each category relative to the monthly total:")
    for category, amount in expenses.items():
        percentage = (amount / total_monthly_expenses) * 100
        print(f"{category}: {percentage:.2f}%")

    # Plot a pie chart
    labels = list(expenses.keys())
    sizes = list(expenses.values())
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Monthly Expenses Breakdown")
    plt.show()


# Run the function
calculate_monthly_expenses()
