
import random
from deck import Deck
import strategies
from populators import basePopulator
import logging
import json
from pathlib import Path

class Player():
    PLAYERS_DIR = Path("players")
    playerNames = set()
    def __init__(self, playerName, topActionLayer, topBuyLayer, kingdom,
        populator=basePopulator):
        '''playerName is a string. topActionLayer and topBuyLayer are each the
           top item in two Decorator-pattern hierarchies, specifying the
           player's strategy.'''
        ext = 2
        finalPlayerName = playerName
        while finalPlayerName in Player.playerNames:
            finalPlayerName = playerName + str(ext)
            ext += 1
        Player.playerNames |= { finalPlayerName }
        self.playerName = finalPlayerName
        self.topActionLayer = topActionLayer
        self.topActionLayer.setPlayer(self)   # Add reverse pointer
        self.topBuyLayer = topBuyLayer
        self.topBuyLayer.player = self      # Add reverse pointer
        self.deck = Deck(self, populator)
        self.numCoins = 0   # The currently "played" number of coins this turn
        self.kingdom = kingdom

    @classmethod
    def fromJsonFile(cls, filename, kingdom):
        if not filename.endswith(".json"):
            filename += ".json"
        with open(Player.PLAYERS_DIR / filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        actionLayers = Player.buildLayers(data['actionLayers'])
        buyLayers = Player.buildLayers(data['buyLayers'])
        return Player(data['playerName'], actionLayers, buyLayers, kingdom)
    @classmethod
    def buildLayers(cls, layerNames):
        lowerLayer = None
        for name, args in reversed(layerNames):
            newLayer = getattr(strategies,name)(args)
            newLayer.setNextLayer(lowerLayer)
            lowerLayer = newLayer
        return lowerLayer

    def doActionPhase(self):
        logging.debug(f"Doing {self.playerName}'s action phase...")
        self.topActionLayer.play()
    def doBuyPhase(self):
        logging.debug(f"Doing {self.playerName}'s buy phase...")
        self.topBuyLayer.play()
    def getVPTotal(self):
        return self.deck.getVPTotal()
    def __str__(self):
        return ("Player " + self.playerName + "\n" +
            "ActionLayers: " + str(self.topActionLayer) + "\n" +
            "BuyLayers: " + str(self.topBuyLayer) + "\n" +
            "Current deck:\n" + str(self.deck))


if __name__ == "__main__":
    p = Player.fromJsonFile("doNothing")
    print(p)
