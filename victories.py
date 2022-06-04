
from card import *

class Estate(Card):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "Estate"
    def VPs(self):
        return 1
