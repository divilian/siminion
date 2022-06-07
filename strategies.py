
from victories import *
from treasures import *
import logging

class ActionLayer():
    def __init__(self):
        pass
    def setPlayer(self, player):
        '''This is somewhat awkward...after the layer's Player object has been
           instantiated, the layer -- and all Decorator-enclosed ones -- must
           be told who that player is.'''
        self.player = player
    def play(self, numStartingActions=1):
        '''Complete this player's entire current action phase, deferring to
           lower layers if necessary.'''
        return True

class RandomActionLayer(ActionLayer):
    def __init__(self):
        super().__init__()
    def play(self, numStartingActions=1):
        '''Play action cards at random until no more actions remain.'''
        actionCards = self.player.deck.cardsInHandWithKeyword("Action")
        numActions = numStartingActions
        for ac in actionCards:
            ac.play()
            numActions -= 1
            if numActions <= 0:
                return


class BuyLayer():
    def __init__(self):
        pass
    def setPlayer(self, player):
        '''This is somewhat awkward...after the layer's Player object has been
           instantiated, the layer -- and all Decorator-enclosed ones -- must
           be told who that player is.'''
        self.player = player
    def play(self):
        '''Complete this player's entire current buy phase, deferring to
           lower layers if necessary.'''
        return True


class GreedyBuyLayer(BuyLayer):
    def play(self, numStartingBuys=1):
        '''Play all treasure cards.'''
        treasureCards = self.player.deck.cardsInHandWithKeyword("Treasure")
        for tc in treasureCards:
            tc.play()
        numBuys = numStartingBuys
        targets = self.getBuyTargets()
        for target in targets:
            while (numBuys >= 1 and target.cost() <= self.player.numCoins
                    and self.player.kingdom.available(target) > 0):
                logging.debug(
                    f"{self.player.playerName} buys a {target.__name__}")
                self.player.deck.gain(self.player.kingdom.take(target,
                    self.player.deck))
                self.player.numCoins -= target.cost()
                numBuys -= 1
    def getBuyTargets(self):
        '''Return an ordered (prioritized) list of Card objects to try and buy.
           This layer will play all treasure cards, then buy as many copies of
           each card in the list as can be afforded, in order, until running
           out of buys.'''
        return [ ]    # (Default behavior: buy nothing.)

class PreferProvincesBuyLayer(GreedyBuyLayer):
    def getBuyTargets(self):
        return [ Province, Gold, Duchy, Silver ]

