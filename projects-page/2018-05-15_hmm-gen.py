import argparse
import sys
import math
import random

def parse_args(args):
    parser = argparse.ArgumentParser(description="Check help flag")
    parser.add_argument("-n", "--numberOfFlips", required=True, type=int, help="Number of flips to generate")
    parser.add_argument("-e", "--emissionProbability_loaded", required=True, type=float, help="If the coin is \
    loaded, what is the probability of a Heads?")
    parser.add_argument("-p", "--initialProbability", required=False, type=float, help="Probability that the \
    first coin is a fair coin")
    parser.add_argument("-ft", "--fairTransition", required=False, type=float, help="Probability that if \
    a fair coin was used, the next coin will be a loaded coin")
    parser.add_argument("-lt", "--loadedTransition", required=False, type=float, help="Probability that if \
    a loaded coin was used, the next coin will be a fair coin")
    parser.add_argument("-t", "--noOfTrials", required=False, type=int, help="Number of trials to run with the\
    given parameters")
    return parser.parse_args()

def flipCoin(e):
    flip = random.randint(1,100)
    if flip <= e:
        return "H"
    return "T"

def main():
    parseargs = sys.argv[1:]
    args = parse_args(parseargs)
    if args.noOfTrials == None:
        noOfTrials = 0
    else: noOfTrials = args.noOfTrials
    coinFlips = []
    realStates = []
    states = ['F', 'L']
    startingState = random.randint(1,100)
    if startingState <= args.initialProbability:
        startState = 'F'
    else:
        startState = 'L'
    emissionProbabilities = {'F':50, 'L':args.emissionProbability_loaded}
    transitionProbabilities = {'F':args.fairTransition, 'L':args.loadedTransition}
    currState = startState
    for flips in range(args.numberOfFlips):
        realStates.append(currState)
        coinFlips.append(flipCoin(emissionProbabilities[currState]))
        currentStateProb = random.randint(1,100)
        if currentStateProb <= transitionProbabilities[currState]:
            currState = states[states.index(currState)-1]
        else:
            pass
    print(realStates)
    print(coinFlips)
if __name__=="__main__":
    main()
