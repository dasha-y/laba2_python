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
        
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance, "Текущий счет")
        
    def deposit(self, amount):
        if amount > 5000:
            bonus = amount * 0.01
            self.balance += bonus
            print(f"Начислен бонус в размере {bonus} за пополнение на сумму {amount}.")
        super().deposit(amount)
        
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance, "Текущий счет")

    def deposit(self, amount):
        if amount > 5000:
            bonus = amount * 0.01
            self.balance += bonus  # Начисление бонуса
            print(f"Начислен бонус в размере {bonus} за пополнение на сумму {amount}.")
        super().deposit(amount)
                
account1 = BankAccount("Чел Первый", 1000.0, "Сберегательный")
account2 = BankAccount("Чел Второй", 500.0, "Текущий")
account3 = CheckingAccount("Чел Третий", 3000.0)

account1.account_info()
account2.account_info()
account3.account_info()

account1.deposit(2000)
account2.deposit(-1000)
account3.deposit(6000)

account1.withdraw(150)
account2.withdraw(600)
account3.withdraw(1500)

account1.account_info()
account2.account_info()
account3.account_info()