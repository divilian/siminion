
from suite import Suite
import sys
import logging
from pathlib import Path
from player import Player
from simulation import Simulation
from kingdom import empty2PlyrBaseKSpec, empty3PlyrBaseKSpec


# Run an entire suite of sims.

def printUsage():
    print("Usage: main.py\n"
        "    player1[.json], player2[.json] ...\n"
        "    [numMatches=100]\n"
        "    [log_level=DEBUG|INFO]\n"
        "    [maxTurns=#]\n"
        "    [startSeed=#].")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            printUsage()
            sys.exit(f"Only {len(sys.argv)} args given.")
        numMatches = 100
        log_level = logging.INFO
        startSeed = 1
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
            elif arg.startswith("startSeed"):
                startSeed = int(arg.split('=')[1])
            elif arg.startswith("numMatches"):
                numMatches = int(arg.split('=')[1])
            else:
                printUsage()
                sys.exit(f"Bad arg '{arg}'")
        if len(playerSpecs) < 2:
            printUsage()
            sys.exit(f"Fewer than two players specified.")
    except Exception as e:
        print(e)
        printUsage()
        sys.exit()

    logging.basicConfig(level=log_level)

    sim = Simulation(playerSpecs, empty2PlyrBaseKSpec, int(maxTurns))
    suite = Suite(sim, startSeed, numMatches, log_level)
    bob = suite.run()
