class BankAccount:
    def __init__(self, owner, balance, account_type):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        
    def deposit(self, amount):
        if amount <= 0:
            print("Некорректная сумма для пополнения.")
        else:
            self.balance += amount
            print(f"Счет {self.owner} пополнен на {amount}. Новый баланс: {self.balance}")
            
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("Недостаточно средств на счете или некорректная сумма снятия.")
        else:
            self.balance -= amount
            print(f"Со счета {self.owner} снята сумма {amount}. Новый баланс: {self.balance}")
            
    def account_info(self):
        print(f"Владелец: {self.owner}, Баланс: {self.balance}, Тип счета: {self.account_type}")
    
account1 = BankAccount("Чел Первый", 1000.0, "Сберегательный")
account2 = BankAccount("Чел Второй", 500.0, "Текущий")

account1.account_info()
account2.account_info()

account1.deposit(2000)
account2.deposit(-1000)

account1.withdraw(150)
account2.withdraw(600)

account1.account_info()
account2.account_info()