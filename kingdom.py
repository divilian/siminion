
from pile import Pile
from victories import *
from treasures import *

class Kingdom():
    def __init__(self, cardClasses):
        '''cardClasses is to be a dict from Card subclasses to quantities.'''
        '''piles is a dict from Card names (strings) to piles.'''
        self.piles = {}
        for cardClass, amount in cardClasses.items():
            self.piles[cardClass.__name__] = Pile(cardClass, amount)

    def finished(self, numPlayers):
        '''Returns True only if the game is completed.'''
        if (sum([ p.numRemaining==0 for p in self.piles.values() ]) >
                                                            numPlayers + 1):
            return True
        elif self.piles['Province'].numRemaining == 0:
            return True
        else:
            return False

    def take(self, card, toDeck):
        '''Take a card of the Card class passed from this Kingdom, assuming
           one still exists. (Assertion exception raised if not.)'''
        return self.piles[card.__name__].take(toDeck)

    def available(self, card):
        '''Return the number of cards left of the Card class passed.'''
        return self.piles[card.__name__].numRemaining

empty2PlyrBaseKingdom = Kingdom(
    { Province:8, Duchy:8, Estate:8,
      Gold:30, Silver:40, Copper:46 })
      
empty3PlyrBaseKingdom = Kingdom(
    { Province:12, Duchy:12, Estate:12,
      Gold:30, Silver:40, Copper:40 })
      
