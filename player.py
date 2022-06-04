
import random
from deck import Deck

class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.deck = Deck(player_name)
    def do_action_phase(self):
        action_cards = self.deck.cards_with_keyword("Action")
        print(f"Here are the acs: {action_cards}")
        for ac in action_cards:
            ac.play()
    def do_buy_phase(self):
        treasure_cards = self.deck.cards_with_keyword("Treasure")
        print(f"Here are the tcs: {treasure_cards}")
        for tc in treasure_cards:
            tc.play()

if __name__ == "__main__":
    lr = Player("Lord Rattington")
    lr.deck.draw_hand()
    lr.do_action_phase()
    lr.do_buy_phase()
