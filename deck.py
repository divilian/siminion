
import random
import populators


class Deck():
    """
    The "deck" for a particular player, which is comprised of a hand, a draw
    pile, and a discard pile. The first of these is a set, and the other two
    are lists. (The first card in each list is the top card of that pile.)
    """
    def __init__(self, player_name, populator=populators.basePopulator):
        super().__init__()
        self.player_name = player_name
        self.discard_pile = []
        self.hand = set()
        if populator:
            self.draw_pile = populator()
        else:
            self.draw_pile = []

    def draw_hand(self):
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
        drawn_cards = []
        for _ in range(num):
            if len(self.draw_pile) == 0:
                self.draw_pile = self.discard_pile
                random.shuffle(self.draw_pile)
                self.discard_pile = []
            drawn_cards.append(self.draw_pile.pop(0))
        self.hand |= set(drawn_cards)
        return drawn_cards

    def __str__(self):
        ret_val = self.player_name + "'s deck:\n" + \
            "  Hand:\n" + self.render(self.hand) + "\n" + \
            "  Draw pile:\n" + self.render(self.draw_pile) + "\n" + \
            "  Discard pile:\n" + self.render(self.discard_pile)
        return ret_val

    def render(self, cards):
        if not cards:
            return "     (empty)"
        if type(cards) is list:
            return "\n".join([ f"{place:6d}. {card}" 
                for place, card in enumerate(cards, start=1) ])
        if type(cards) is set:
            return "     " + ",".join([ f"{card}" for card in cards ])

