
import random
from treasures import *
from victories import *

# A populator is a function which, when called, returns a list of fresh copies
# of Card objects, typically to initialize a player's hand at start of game.

def basePopulator():
    '''Base game populator: 7 coppers and 3 estates.'''
    cards = [ Copper() for _ in range(7) ] + \
        [ Estate() for _ in range(3) ]
    random.shuffle(cards)
    return cards
