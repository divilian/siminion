
from deck import *
from victories import Estate

if __name__ == "__main__":
    print("1. Demonstrate deck construction and draw.")
    ratDeck = Deck("Lord Rattington", None)   # No need for Player object
    print("===========================================")
    print("Original deck:")
    print(ratDeck)
    print("===========================================")
    print(f"The deck has {ratDeck.getVPTotal()} VPs.")
    print("===========================================")
    print("After initial draw:")
    ratDeck.drawHand()
    print(ratDeck)
    input("\n(Press ENTER to continue.)")
    while len(ratDeck.drawPile) > 0:
        print("After next draw:")
        ratDeck.draw()
        print(ratDeck)
        input("\n(Press ENTER to continue.)")

    print("\n\n")
    print("2. Calculate empirical probability of 3/4 vs. 2/5 initial split.")
    NUM_TRIALS = 100000
    two_fives = 0
    three_fours = 0
    for _ in range(NUM_TRIALS):
        deck = Deck("test", None)   # No need for Player object
        deck.drawHand()
        numEstates = sum([ type(x) is Estate for x in deck.hand ])
        if numEstates in [0,3]:
            two_fives += 1
        elif numEstates in [1,2]:
            three_fours += 1
        else:
            stop(f"WHOA! Got {numEstates} estates in initial draw.")
    print(f"There were {(two_fives/NUM_TRIALS*100):.1f}% 2/5 splits.")
