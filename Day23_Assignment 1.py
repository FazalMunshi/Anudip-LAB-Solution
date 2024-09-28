import matplotlib.pyplot as plt

# Data for spending categories and monthly expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.figure(figsize=(8,6))
plt.bar(categories, expenses, color='skyblue')

# Add title and labels
plt.title('Monthly Expenses by Category')
plt.xlabel('Spending Categories')
plt.ylabel('Expenses (in USD)')

# Rotate the category labels for better readability
plt.xticks(rotation=45)

# Adjust layout for a better fit
plt.tight_layout()

# Show the chart
plt.show()
