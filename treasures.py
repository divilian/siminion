
from card import *


class Gold(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Gold"
    def cost(self):
        return 6
    def play(self):
        super().play()
        self.deck.player.numCoins += 3

class Silver(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Silver"
    def cost(self):
        return 3
    def play(self):
        super().play()
        self.deck.player.numCoins += 2

class Copper(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return "Copper"
    def cost(self):
        return 0
    def play(self):
        super().play()
        self.deck.player.numCoins += 1

