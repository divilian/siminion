
from pile import Pile
from player import Player
import random
import logging
from strategies import *
from kingdom import Kingdom, empty3PlyrBaseKingdom
import sys

class Simulation():

    def __init__(self, players, kingdom, max_turns=5):
        '''players is a set of Player objects. kingdom is a Kingdom.'''
        self.MAX_TURNS = max_turns   # After more than this, force-stop sim.
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
            player.deck.doCleanupPhase()
            player.deck.drawHand()
            logging.debug(f"{player.playerName}'s deck is now:\n{player.deck}")
            playerTurn = (playerTurn + 1) % len(self.players)
            if playerTurn == 0:
                logging.info("==========================================")
                numTurns += 1
            logging.info("------------------------------------------")

    def __str__(self):
        return f"a {len(self.players)}-player simulation"


def printUsage():
    print("Usage: simulation.py\n"
        "    [log_level=INFO|DEBUG]\n"
        "    [max_turns=#].")

if __name__ == "__main__":
    log_level = logging.INFO
    max_turns = 5
    for arg in sys.argv[1:]:
        if "=" not in arg:
            printUsage()
            sys.exit(f"Bad arg '{arg}'")
        elif arg.startswith("log_level"):
            log_level = getattr(logging, arg.split("=")[1])
        elif arg.startswith("max_turns"):
            max_turns = int(arg.split("=")[1])
        else:
            printUsage()
            sys.exit(f"Bad arg '{arg}'")
                
    logging.basicConfig(level=log_level)

    sim = Simulation([ Player(name, ActionLayer(), PreferProvincesBuyLayer())
        for name in ['Lord Rattington', 'Lord Voldebot', 'Revenge Witch']],
        empty3PlyrBaseKingdom, max_turns)
    sim.play()
