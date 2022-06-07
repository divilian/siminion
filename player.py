
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
        self.topActionLayer.player = self   # Add reverse pointer
        self.topBuyLayer = topBuyLayer
        self.topBuyLayer.player = self      # Add reverse pointer
        self.deck = Deck(self, populator)
        self.numCoins = 0   # The currently "played" number of coins this turn
    def doActionPhase(self):
        logging.debug(f"Doing {self.playerName}'s action phase...")
        self.topActionLayer.play()
    def doBuyPhase(self):
        logging.debug(f"Doing {self.playerName}'s buy phase...")
        self.topBuyLayer.play()
    def getVPTotal(self):
        return self.deck.getVPTotal()
    def setKingdom(self, kingdom):
        self.kingdom = kingdom
    def __str__(self):
        return self.playerName + ", with deck:\n" + str(self.deck)

