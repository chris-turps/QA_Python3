import datetime

class Transaction:
    def __init__(self, drinkName, cost, payment) -> None:
        self.time = datetime.datetime.now()
        self.drink = drinkName
        self.cost = cost
        self.payment = payment
    
    def __str__(self) -> str:
        return f'Time: {self.time.strftime("%d/%m/%Y %H:%M:%S")}\nDrink: {self.drink}\nCost: {self.cost}\nPaid: {self.payment}'