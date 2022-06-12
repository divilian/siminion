
from pile import Pile
from player import Player
import random
import logging
from strategies import *
from kingdom import Kingdom, empty3PlyrBaseKSpec, empty2PlyrBaseKSpec
import sys
from sortedcollections import ValueSortedDict
import json
from pathlib import Path


class Simulation():

    def __init__(self, playerSpecs, kingdomSpec, maxTurns=5):
        '''players is a set of JSON filenames, each of which holds the
           specification for a Player object. kingdomSpec is a dict of Card
           classes and quantities, suitable as the constructor arg to the
           Kingdom class.'''
        self.maxTurns = maxTurns   # After more than this, force-stop sim.
        self.playerSpecs = list(playerSpecs)
        self.kingdomSpec = kingdomSpec

    def play(self):
        '''Run one simulated game. This returns a tuple with two pieces of
           information: (1) a dict from player names to final scores. (2) a
           boolean indicating whether the game actually legally finished (as
           opposed to being prematurely truncated by MAX_TURNS, e.g.)'''
        self.kingdom = Kingdom(self.kingdomSpec)
        Player.playerNames = set()
        self.players = [ Player.fromJsonFile(spec, self.kingdom)
            for spec in self.playerSpecs ]
        random.shuffle(self.players)   # Players start in random order

        # Draw initial hands.
        for player in self.players:
            player.deck.drawHand()
        
        numTurns = 0
        playerTurn = 0

        logging.info("==========================================")
        while (numTurns < self.maxTurns and
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
                logging.info(", ".join(
                    [ f"{p.playerName}: {p.deck.getVPTotal()}"
                      for p in self.players ]))
                logging.info("==========================================")
                numTurns += 1
            logging.info("------------------------------------------")

        return { p.playerName:p.deck.getVPTotal() for p in self.players }, \
            self.kingdom.finished(len(self.players))

    def __str__(self):
        return f"a {len(self.players)}-player simulation"


def printResults(results, players):
    '''Pretty print the tuple returned from sim() that has two pieces of
       information: (1) a dict from player names to final scores. (2) a
       boolean indicating whether the game actually legally finished (as
       opposed to being prematurely truncated by maxTurns, e.g.)
       If in debug logging mode, print entire players at end of game.'''
    print("\n")
    if results[1]:
        print("Official match results:")
    else:
        print("Truncated (and unofficial) match results:")
    maxNameLen = max([ len(pn) for pn in results[0].keys() ])
    for playerName in reversed(ValueSortedDict(results[0])):
        print(f"  {playerName:<{maxNameLen}}: {results[0][playerName]:3d}")
    print("\n")
    for player in players:
        logging.debug(player)
        logging.debug("\n")


def printUsage():
    print("Usage: simulation.py player1[.json], player2[.json] ...\n"
        "    [log_level=INFO|DEBUG]\n"
        "    [maxTurns=#].")

if __name__ == "__main__":
    log_level = logging.INFO
    maxTurns = 1e9   # We'll call this "infinity" (i.e., never stop sim)
    playerSpecs = []
    for arg in sys.argv[1:]:
        if "=" not in arg:
            if not arg.endswith(".json"):
                arg += ".json"
            path = Path(Player.PLAYERS_DIR / arg)
            assert path.is_file(), f"No such player file {path}."
            playerSpecs += [arg]
        elif arg.startswith("log_level"):
            log_level = getattr(logging, arg.split("=")[1])
        elif arg.startswith("maxTurns"):
            maxTurns = int(arg.split("=")[1])
        else:
            printUsage()
            sys.exit(f"Bad arg '{arg}'")
    if len(playerSpecs) < 2:
        printUsage()
        sys.exit(f"Fewer than two players specified.")
                
    logging.basicConfig(level=log_level)

    sim = Simulation(playerSpecs, empty2PlyrBaseKSpec, maxTurns)
    results = sim.play()
    printResults(results, sim.players)
