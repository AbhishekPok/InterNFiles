class BankAccount:
    bankName = "Abhishek International Bank."
    def __init__(self, user, balance):
        self.user = user #instance variable
        self.balance = balance #instance variable
        print(f"New customer {self.user} is registered with amount {self.balance}")

    def deposit(self, balance):
        self.balance += balance
        print(f"{self.balance} deposited to your account.")

    def withdrawal(self, balance):
        if balance >  self.balance:
            print(f"The balance in account is insufficient.\n{self.balance} present in account.\nTransaction terminated.")
        else:
            self.balance -= balance
            print(f"{balance} amount withdrawn.")

user = BankAccount("Abhishek", 10000)
# user1 = BankAccount("Abiral", 500)
user.deposit(12000)
user.withdrawal(5000)
# user1.deposit(12000)
# user1.withdrawal(5000)
