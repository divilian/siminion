
from card import *

class Province(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return "Province"
    def play(self):
        raise ValueError("Province can't be played")
    def cost(self):
        return 8
    def VPs(self):
        return 6

class Duchy(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return "Duchy"
    def play(self):
        raise ValueError("Duchy can't be played")
    def cost(self):
        return 5
    def VPs(self):
        return 3

class Estate(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return "Estate"
    def play(self):
        raise ValueError("Estate can't be played")
    def cost(self):
        return 2
    def VPs(self):
        return 1
