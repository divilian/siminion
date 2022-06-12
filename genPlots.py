
import pandas as pd
import sys
from pathlib import Path

# Given the CSV file produced from a Siminion suite, create various plots of
# its statistics.
def printUsage():
    print("Usage: genPlots.py siminionOutputFile[.csv].")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        printUsage()
        sys.exit()
    if not sys.argv[1].endswith(".csv"):
        sys.argv[1] += ".csv"
    path = Path(sys.argv[1])
    if not path.is_file():
        printUsage()
        sys.exit(f"No such file {path}.")
    df = pd.read_csv(path)
