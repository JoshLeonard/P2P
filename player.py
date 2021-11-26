

class Player:

    def __init__(self):
        self.cash = 100

    def getCashBalance(self):
        return self.cash

    def recieveCash(self, amount):
        self.cash += amount

    def transferFunds(self, player, amount):
        if self.cash > amount:
            self.cash -= amount
            player.recieveCash(amount)
