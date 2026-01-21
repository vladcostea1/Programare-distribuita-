class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Suma depusă trebuie să fie pozitivă.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Suma retrasă trebuie să fie pozitivă.")
        if amount > self._balance:
            raise ValueError("Fonduri insuficiente.")
        self._balance -= amount

    def get_balance(self):
        return self._balance



if __name__ == "__main__":
    account = BankAccount(1000)

    try:
        account.deposit(500)
        print("După depunere, sold:", account.get_balance())

        account.withdraw(300)
        print("După retragere, sold:", account.get_balance())

    except ValueError as e:
        print("Eroare:", e)
