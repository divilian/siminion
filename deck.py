
import random
import populators

class Deck():
    """
    The "deck" for a particular player, which is comprised of a hand, a draw
    pile, and a discard pile. The first of these is a set, and the other two
    are lists. (The first card in each list is the top card of that pile.)
    """
    def __init__(self, player, populator=populators.basePopulator):
        super().__init__()
        self.player = player
        self.discardPile = []
        self.playArea = set()
        self.hand = set()
        if populator:
            self.drawPile = populator(self)
        else:
            self.drawPile = []

    def cardsInHandWithKeyword(self, keyword):
        return [ c for c in self.hand if keyword in c.keywords ]

    def drawHand(self):
        '''
        Draw the requisite number of cards for a new hand, triggering a
        shuffle if necessary. Note that this method does not assume the hand
        is currently empty, nor does it make it so.
        '''
        self.draw(5)

    def draw(self, num=1):
        '''
        Draw some number of cards (default 1) to the user's hand, triggering
        a shuffle if necessary. Also return the cards in a list.
        '''
        drawnCards = []
        for _ in range(num):
            if len(self.drawPile) == 0:
                self.drawPile = self.discardPile
                random.shuffle(self.drawPile)
                self.discardPile = []
            drawnCards.append(self.drawPile.pop(0))
        self.hand |= set(drawnCards)
        return drawnCards

    def discardHand(self):
        '''Dump the hand into the discard pile.'''
        self.discardPile = list(self.hand) + self.discardPile
        self.hand = set()

    def discardPlayArea(self):
        '''Dump the cards in play area into the discard pile.'''
        self.discardPile = list(self.playArea) + self.discardPile
        self.playArea = set()

    def doCleanupPhase(self):
        '''Carry out "cleanup phase" in its entirety.'''
        # TODO: Ask TJ if this is the right procedure.
        self.discardHand()
        self.discardPlayArea()

    def getVPTotal(self):
        return sum([ c.VPs()
            for c in self.hand | self.playArea | set(self.discardPile) |
                set(self.drawPile) ])

    def gain(self, card):
        self.discardPile = [card] + self.discardPile

    def __str__(self):
        ret_val = "  Hand:\n" + self.render(self.hand) + "\n" + \
            "  Draw pile:\n" + self.render(self.drawPile) + "\n" + \
            "  Discard pile:\n" + self.render(self.discardPile)
        return ret_val

    def render(self, cards):
        if not cards:
            return "     (empty)"
        if type(cards) is list:
            return "\n".join([ f"{place:6d}. {card}" 
                for place, card in enumerate(cards, start=1) ])
        if type(cards) is set:
            return "     " + ",".join([ f"{card}" for card in cards ])

