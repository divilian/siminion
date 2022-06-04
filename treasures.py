
from card import *


class Gold(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Gold"

class Silver(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Silver"

class Copper(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Copper"

