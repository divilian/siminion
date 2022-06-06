
class ActionLayer():
    def __init__(self):
        pass
    def play(self, numStartingActions=1):
        '''Complete this player's entire current action phase, deferring to
           lower layers if necessary.'''
        return True

class RandomActionLayer(ActionLayer):
    def __init__(self):
        pass
    def play(self, numStartingActions=1):
        '''Play action cards at random until no more actions remain.'''
        actionCards = self.deck.cardsWithKeyword("Action")
        numActions = numStartingActions
        for ac in actionCards:
            ac.play()
            numActions -= 1
            if numActions <= 0:
                return


class BuyLayer():
    def __init__(self):
        pass
    def play(self):
        '''Complete this player's entire current buy phase, deferring to
           lower layers if necessary.'''
        return True

class RandomBuyLayer(BuyLayer):
    def __init__(self):
        pass
    def play(self, numStartingBuys=1):
        '''What should this do?'''
        pass
