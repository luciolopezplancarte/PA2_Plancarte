from ExpenseTracker import ExpenseTracker

tracker = ExpenseTracker(2)

tracker.add_expense("Netflix", 9.99, "01-05-2025")
tracker.add_expense("Walmart", 45.89, "01-10-2025")
tracker.add_expense("Hulu", 5.99, "01-10-2025")
tracker.add_expense("Walmart", 9.99, "01-11-2025")
tracker.add_expense("Dollar Tree", 14.45, "01-12-2025")

average_expenses = tracker.get_average()
print("Average Expenses this month:", round(average_expenses, 2)) #14.45

print(tracker.search_expense(50)) #No expense of 50
print(tracker.search_expense(9.99)) #Netflix Walmart

