class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.total_expenses = 0

    def add_expense(self, amount):
        self.expenses.append(amount)
        self.total_expenses += amount

    def get_total_expenses(self):
        return self.total_expenses

    def clear_expenses(self):
        self.expenses = []
        self.total_expenses = 0


# Example usage:
tracker = ExpenseTracker()

# Adding expenses
tracker.add_expense(10)
tracker.add_expense(20)
tracker.add_expense(15)

# Getting total expenses
total_expenses = tracker.get_total_expenses()
print(f"Total expenses: ${total_expenses}")

# Clearing expenses
tracker.clear_expenses()
print("Expenses cleared.")
