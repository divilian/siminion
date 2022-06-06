
import random
from deck import Deck
from strategies import *
from populators import basePopulator
import logging

class Player():
    def __init__(self, playerName, topActionLayer, topBuyLayer,
        populator=basePopulator):
        '''playerName is a string. topActionLayer and topBuyLayer are each the
           top item in two Decorator-pattern hierarchies, specifying the
           player's strategy.'''
        self.playerName = playerName
        self.topActionLayer = topActionLayer
        self.topBuyLayer = topBuyLayer
        self.deck = Deck(populator)
    def doActionPhase(self):
        logging.debug(f"Doing {self.playerName}'s action phase...")
        self.topActionLayer.play()
    def doBuyPhase(self):
        logging.debug(f"Doing {self.playerName}'s buy phase...")
        self.topBuyLayer.play()
    def getVPTotal(self):
        return self.deck.getVPTotal()
    def __str__(self):
        return self.playerName + ", with deck:\n" + str(self.deck)


if __name__ == "__main__":
    lr = Player("Lord Rattington")
    lr.deck.drawHand()
    lr.doActionPhase()
    lr.doBuyPhase()
