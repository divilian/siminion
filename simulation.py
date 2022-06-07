
from pile import Pile
from player import Player
import random
import logging
from strategies import *
from kingdom import Kingdom, empty3PlyrBaseKingdom

class Simulation():

    def __init__(self, players, kingdom):
        '''players is a set of Player objects. kingdom is a Kingdom.'''
        self.MAX_TURNS = 5   # After more turns than this, force-stop sim.
        self.players = list(players)
        random.shuffle(self.players)   # Players start in random order
        self.kingdom = kingdom

    def play(self):
        '''Run one simulated game, returning a dict from player names to final
        scores.'''

        # Draw initial hands.
        for player in self.players:
            player.deck.drawHand()
        
        numTurns = 0
        playerTurn = 0

        logging.info("==========================================")
        while (numTurns < self.MAX_TURNS and
                not self.kingdom.finished(len(self.players))):
            player = self.players[playerTurn]
            logging.info(f"Beginning player {playerTurn}'s " +
                f"({player.playerName}'s) turn {numTurns}")
            player.doActionPhase()
            player.doBuyPhase()
            logging.debug(f"{player.playerName}'s deck is now:\n{player.deck}")
            playerTurn = (playerTurn + 1) % len(self.players)
            if playerTurn == 0:
                logging.info("==========================================")
                numTurns += 1

    def __str__(self):
        return f"a {len(self.players)}-player simulation"



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sim = Simulation([ Player(name, ActionLayer(), BuyLayer())
        for name in ['Lord Rattington', 'Lord Voldebot', 'Revenge Witch']],
        empty3PlyrBaseKingdom)
    sim.play()
