# HPI3
Open-Source Software

# **Expense Tracker Summary**

## **Overview**
This project is a simple yet effective tool built in Python to calculate and analyze monthly expenses. It allows users to:
- Understand their spending habits through a detailed breakdown of expenses by category.
- View total monthly and annual spending.
- Identify the percentage contributions of each expense category.
- Visualize their spending patterns through a pie chart.

The project is designed to be lightweight and user-friendly, making it ideal for anyone who wants to manage their finances without the complexity of traditional budgeting tools.

---

## **Features**
1. **Expense Categories**:
   - Predefined categories: Rent, Utilities, Food, Transport, Entertainment, and Other.
   - Easy to modify or expand for custom use.
2. **Financial Summary**:
   - Calculates total monthly and annual expenses.
   - Computes the percentage contribution of each category.
3. **Data Visualization**:
   - Generates a pie chart for a quick overview of spending patterns.
4. **Accessible and Open Source**:
   - Easy to run on Google Colab or locally.
   - Licensed under the MIT License for flexibility and reuse.

---

## **How It Works**
### **1. Input**
The program starts by storing predefined monthly expenses in a dictionary:
```python
expenses = {
    "Rent": 600,
    "Utilities": 150,
    "Food": 250,
    "Transport": 100,
    "Entertainment": 80,
    "Other": 50
}
```
---

## 2. Processing
The code performs the following operations:
- **Total Monthly Expenses**: Calculates the sum of all category expenses.
- **Total Annual Expenses**: Multiplies the monthly total by 12.
- **Percentage Contribution**: Computes the percentage of each category relative to the monthly total.

---

## 3. Output
The results are:
1. Printed in the console in a user-friendly format.
2. Visualized as a pie chart showing the expense distribution.

---

## Code Explanation

### Key Functions and Logic

#### **Dictionary of Expenses**
Stores the monthly expenses for each category:
```python
expenses = {
    "Rent": 600,
    "Utilities": 150,
    "Food": 250,
    "Transport": 100,
    "Entertainment": 80,
    "Other": 50
}
```
Total Calculations:
Calculates the total monthly and annual expenses:

```python
total_monthly_expenses = sum(expenses.values())
total_annual_expenses = total_monthly_expenses * 12
Percentage Breakdown:
Computes the percentage contribution of each category:
```
```python
for category, amount in expenses.items():
    percentage = (amount / total_monthly_expenses) * 100
    print(f"{category}: {percentage:.2f}%")
Pie Chart Visualization:
Generates a pie chart to display the expense distribution:
```
```python
labels = list(expenses.keys())
sizes = list(expenses.values())
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Monthly Expenses Breakdown")
plt.show()
```
How to Run
Clone this repository:

```
git clone https://github.com/daliaxx/ExpenseTracker.git
```
OR Run the project in Google Colab:
Link:


=== Monthly Expenses Calculation ===

Monthly expense details:
Rent: €600.00
Utilities: €150.00
Food: €250.00
Transport: €100.00
Entertainment: €80.00
Other: €50.00

Total monthly expenses: €1230.00
Total annual expenses: €14760.00

Percentage of each category relative to the monthly total:
Rent: 48.78%
Utilities: 12.20%
Food: 20.33%
Transport: 8.13%
Entertainment: 6.50%
Other: 4.07%
Pie Chart



Future Enhancements
Add support for user-defined categories via a CSV file.
Enable integration with financial APIs to fetch real-time expense data.
Add bar and line charts to display expense trends over time.
Create a user-friendly graphical interface for non-coders.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code for personal or commercial purposes, provided you include the original copyright notice.

Contributors
4Real
Contact
If you have any questions or suggestions, feel free to open an issue in this repository.
