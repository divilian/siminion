
from card import *

class Province(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return "Province"
    def VPs(self):
        return 6

class Duchy(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return "Duchy"
    def VPs(self):
        return 3

class Estate(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return "Estate"
    def VPs(self):
        return 1
