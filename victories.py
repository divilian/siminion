
from card import *

GREEN_ANSI_CODE = "\u001b[32m"
RESET_ANSI_CODE = "\u001b[0m"

class Province(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return f"{GREEN_ANSI_CODE}Province{RESET_ANSI_CODE}"
    def play(self):
        raise ValueError("Province can't be played")
    @classmethod
    def cost(self):
        return 8
    def VPs(self):
        return 6

class Duchy(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return f"{GREEN_ANSI_CODE}Duchy{RESET_ANSI_CODE}"
    def play(self):
        raise ValueError("Duchy can't be played")
    @classmethod
    def cost(self):
        return 5
    def VPs(self):
        return 3

class Estate(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return f"{GREEN_ANSI_CODE}Estate{RESET_ANSI_CODE}"
    def play(self):
        raise ValueError("Estate can't be played")
    @classmethod
    def cost(self):
        return 2
    def VPs(self):
        return 1
