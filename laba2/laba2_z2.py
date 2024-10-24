class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
            
    def total_expenses(self, category):
        return self.expenses.get(category, 0)
    
    def all_categories(self):
        return list(self.expenses.keys())
    
tracker = ExpenseTracker()

tracker.add_expense("Кафе", 100)
tracker.add_expense("Транспорт", 50)
tracker.add_expense("Книги", 50)
tracker.add_expense("Развлечения", 200)

print(f"Общие расходы на транспорт: {tracker.total_expenses('Транспорт')}")

print(f"Все категории: {tracker.all_categories()}")