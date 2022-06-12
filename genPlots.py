
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# Given the CSV file produced from a Siminion suite, create various plots of
# its statistics.
def printUsage():
    print("Usage: genPlots.py siminionOutputFile[.csv].")


if len(sys.argv) != 2:
    printUsage()
    sys.exit()
if not sys.argv[1].endswith(".csv"):
    csvFilename = sys.argv[1] + ".csv"
else:
    csvFilename = sys.argv[1]
csvPath = Path(csvFilename)
if not csvPath.is_file():
    printUsage()
    sys.exit(f"No such file {csvPath}.")
df = pd.read_csv(csvPath).set_index('seed')

# Known column names that label general statistics in the DataFrame. Any column
# not in this list must be a player name.
NON_PLAYER_COLS = set()
PLAYER_COLS = list(set(df.columns) - NON_PLAYER_COLS)

scoresWide = df[PLAYER_COLS].copy()

##############################################################################
# Scores box plot.
scores = pd.melt(scoresWide, var_name='player', value_name='score')
scores.score = scores.score.astype(int)
scores.plot(kind='box',by='player')
plt.title("Final scores")
plotFilename = csvFilename.replace(".csv","scores.png")
plt.savefig(plotFilename)
print(f"(Scores box plot written to {plotFilename}.)")


##############################################################################
# Wins box plot.
# Ick!
winners = np.empty(len(scoresWide),dtype="object")
for rownum in range(len(scoresWide)):
    for pn in PLAYER_COLS:
        if all([ scoresWide.iloc[rownum][p] <= scoresWide.iloc[rownum][pn]
                                                for p in PLAYER_COLS]):
            winners[rownum] = pn
scoresWide['winner'] = winners
plt.clf()
fig, _ = plt.subplots(nrows=1,ncols=1)
winnerTotals = scoresWide.winner.value_counts()
for pn in PLAYER_COLS:
    if pn not in winnerTotals:
        winnerTotals[pn] = 0
winnerTotals.plot(kind='bar')
plt.title(f"Number of wins ({len(scoresWide)} matches)")
fig.tight_layout()
plotFilename = csvFilename.replace(".csv","wins.png")
plt.savefig(plotFilename)
print(f"(Wins bar chart written to {plotFilename}.)")
