from ArrayList import Array
from expense import Expense

class ExpenseTracker(Array):

    def __init__(self, capacity):
        super().__init__(capacity)

    def add_expense(self,description, amount, date):
        new_expense = Expense(description,amount,date)
        self.append(new_expense)
        print(f"Storing expense of $ {new_expense.get_amount()}")

    def get_average(self):
        if self.isEmpty():
            return 0
        avg = 0
        for i in range(len(self)):
            avg += self[i].get_amount()
        return avg/len(self)
        

    def search_expense(self, amount):
        found = ""
        counter = 0
        for i in range(len(self)):
            if self[i].get_amount() == amount:
                counter +=1
                found += " "+(self[i].get_description())
        if counter == 0:
            return f"No expense of ${amount}"
    
        return f"Expenses of ${amount}: {found}"
