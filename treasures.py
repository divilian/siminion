
from card import *


class Gold(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Gold"
    def playable_during_buy_phase(self):
        return True

class Silver(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Silver"
    def playable_during_buy_phase(self):
        return True

class Copper(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Copper"
    def playable_during_buy_phase(self):
        return True

