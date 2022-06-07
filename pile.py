
class Pile():
    def __init__(self, cardClass, amount):
        self.cardClass = cardClass
        self.numRemaining = amount
    def take(self, toDeck):
        assert self.numRemaining >= 1, f"No cards left in {cardClass} pile"
        self.numRemaining -= 1
        return self.cardClass(toDeck)
