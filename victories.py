
from card import *

class Estate(Card):
    def __init__(self, deck):
        super().__init__(deck)
        self.keywords |= { "Victory" }
    def __str__(self):
        return "Estate"
    def VPs(self):
        return 1
