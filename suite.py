
from pile import Pile
from player import Player
import random
import logging
import subprocess
from simulation import Simulation
from strategies import *
from kingdom import Kingdom, empty2PlyrBaseKSpec, empty3PlyrBaseKSpec
import sys
import random
from pathlib import Path
import math
import pandas as pd


class Chunk():
    def __init__(self, seeds):
        self.seeds = seeds
    def run(self, sim):
        outcomes = []
        for seed in seeds:
            logging.debug(f'Running seed {seed}...')
            results = sim.play(seed)
            outcomes.append(results)
        return outcomes



class Suite():

    NUM_CORES = 12

    def __init__(self, sim, baseSeed=1, numMatches=100):
        '''sim is an entire Simulation object, instantiated in the usual 
           way. baseSeed is the first random seed to be used in the sequence
           of matches; others follow sequentially. numMatches is the total
           number of faceoffs to simulate.'''
        self.sim = sim
        self.baseSeed = baseSeed
        self.numMatches = numMatches

    def run(self):
        numRunsPerCore = math.ceil(self.numMatches / Suite.NUM_CORES)
        startingSeedsForCore = [ self.baseSeed + i*numRunsPerCore
            for i in range(Suite.NUM_CORES) ]
        procs = []
        outputFiles = []
        for startSeed in startingSeedsForCore:
            endSeed = min(self.baseSeed + self.numMatches - 1,
                startSeed + numRunsPerCore - 1)
            logging.warning(f"Running seeds {startSeed}:{endSeed}...")
            outputFile = f"/tmp/output{startSeed:04d}.csv"
            cmdLine = [ 'python', './suite.py', f"{startSeed}:{endSeed}" ] +\
                [ p for p in self.sim.playerSpecs ] + \
                [ 'maxTurns='+str(self.sim.maxTurns) ]
            procs.append(subprocess.Popen(cmdLine))
            outputFiles.append(outputFile)

        print(f'Waiting for {self.numMatches}-match suite completion...')
        [ p.wait() for p in procs ]
        print('...done.')

        cols = ['seed'] + self.sim.playerSpecs + ['numTurns']
        results = pd.DataFrame({ col:[] for col in cols })
        results = pd.concat([ pd.read_csv(ofile, encoding="utf-8")
            for ofile in outputFiles ])
        results.to_csv(f"/tmp/siminion{self.baseSeed}.csv",mode="w",
            encoding="utf-8", index=None)
        logging.critical(f"Results in /tmp/siminion{self.baseSeed}.csv.")
        return results



# Note: this main() only runs one chunk, not an entire suite. To run an entire
# suite, use main.py.

def printUsage():
    print("Usage: suite.py player1[.json], player2[.json] ...\n"
        "    [log_level=INFO|DEBUG]\n"
        "    [maxTurns=#].")

if __name__ == "__main__":
    print(f"Running: {sys.argv}.")
    try:
        if len(sys.argv) < 4:
            printUsage()
            sys.exit(f"Only {len(sys.argv)} args given.")
        log_level = logging.INFO
        maxTurns = 1e9   # We'll call this "infinity" (i.e., never stop sim)
        playerSpecs = []
        start,end = [ int(s) for s in sys.argv[1].split(':') ]
        seeds = range(start,end+1)
        for arg in sys.argv[2:]:
            print(f"Checking {arg}...")
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
    except:
        printUsage()
        sys.exit()

                
    logging.basicConfig(level=log_level)

    chunk = Chunk(seeds)
    sim = Simulation(playerSpecs, empty2PlyrBaseKSpec, maxTurns)
    outcomes = chunk.run(sim)
    outputFile = f'/tmp/output{start:04d}.csv'
    with open(outputFile, 'w', encoding='utf-8') as f:
        print('seed,'+','.join([ pn.replace('.json','')
             for pn in sim.playerSpecs ]),file=f)
        for outcome in outcomes:
            print(f"{outcome['seed']}," +
                str(",".join([ str(outcome[pn.replace('.json','')])
                    for pn in sim.playerSpecs ])),file=f)
