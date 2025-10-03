class Expense:

    def __init__ (self,description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date


    def get_description(self):
        return self.description

    def get_amount(self):
        return self.amount

    def get_date(self):
        return self.date
