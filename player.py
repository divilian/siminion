
import random
from deck import Deck

class Player():
    def __init__(self, playerName):
        self.playerName = playerName
        self.deck = Deck(playerName)
    def doActionPhase(self):
        actionCards = self.deck.cardsWithKeyword("Action")
        print(f"Here are the acs: {actionCards}")
        for ac in actionCards:
            ac.play()
    def doBuyPhase(self):
        treasureCards = self.deck.cardsWithKeyword("Treasure")
        print(f"Here are the tcs: {treasureCards}")
        for tc in treasureCards:
            tc.play()

if __name__ == "__main__":
    lr = Player("Lord Rattington")
    lr.deck.drawHand()
    lr.doActionPhase()
    lr.doBuyPhase()
