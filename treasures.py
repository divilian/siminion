
from card import *

YELLOW_ANSI_CODE = "\u001b[33m"
RESET_ANSI_CODE = "\u001b[0m"

class Gold(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Treasure" }
    def __str__(self):
        return f"{YELLOW_ANSI_CODE}Gold{RESET_ANSI_CODE}"
    @classmethod
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
        return f"{YELLOW_ANSI_CODE}Silver{RESET_ANSI_CODE}"
    @classmethod
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
        return f"{YELLOW_ANSI_CODE}Copper{RESET_ANSI_CODE}"
    @classmethod
    def cost(self):
        return 0
    def play(self):
        super().play()
        self.deck.player.numCoins += 1

