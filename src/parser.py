import os
import argparse
import converter_to_cnf
import tokenizer
import sys
from time import time

class Node:
    # Initialize the node with two child nodes, right node can be empty
    def __init__(self, sym, left, right=None):
        self.sym = sym
        self.left = left
        self.right = right

    def __repr__(self):
        return self.sym

class Parser:
    # Initialize parser attributes
    def __init__(self, grammar, sentence):
        self.parsetable = None
        self.productions = {}
        self.grammar = None
        self.grammarFromFile(grammar)
        self.__call__(sentence)
    
    # Initialize sentence parsing
    def __call__(self, sentence, parse=False):
        if os.path.isfile(sentence):
            file = open(sentence)
            text = file.read()
            file.close()
            tokenizer.tokenizer(text)
            with open('tokenized.txt') as stream:
                self.input = stream.readline().split()
                if parse:
                    self.parse()
        else:
            tokenizer.tokenizer(sentence)
            with open('tokenized.txt') as stream:
                self.input = stream.readline().split()
    

    def toDict(self, grammar):
        ans = {}
        for g in grammar:
            ans[str(g[0])] = []

        for g in grammar:
            prod = []
            for i in range(1,len(g)):
                temp = g[i]
                prod.append(temp)
            ans[str(g[0])].append(prod)
        return ans

    # CYK Algorithm
    def parse(self):
        animation = "|/-\\"
        n = len(self.input)
        R = self.toDict(self.grammar)
        # Initialize the table
        self.parsetable = [[set([]) for j in range(n)] for i in range(n)]

        # Filling in the parsetable
        for j in range(0, n):

            # Check form S -> a
            for left, rule in R.items():
                for right in rule:
                    # If a terminal is found
                    if len(right) == 1 and right[0] == ("'" + self.input[j] + "'"):
                        self.parsetable[j][j].add(left)


            # Check form S -> AB
            for i in range(j, -1, -1):      
                for k in range(i, j):   
                    # Iterate over rules
                    for left, rule in R.items():
                        for right in rule:
                            # Checking for terminals
                            if len(right) == 2 and right[0] in self.parsetable[i][k] and right[1] in self.parsetable[k + 1][j]:
                                self.parsetable[i][j].add(left)
                                
                    sys.stdout.write("\rParsing.." + animation[k % len(animation)])
                    sys.stdout.flush()
        print()

    # Result decider according to the CYK formula
    def result(self):
        n = len(self.input)
        if len(self.parsetable[0][n-1]) != 0:
            print("Accepted.")
        else:
            print("Syntax error.")

    # Open grammar from file
    def grammarFromFile(self, g):
        cfg = converter_to_cnf.read_grammar(g)
        self.grammar = converter_to_cnf.convert_grammar(cfg)


def printASCII():
    print('''welcome to....
_____     _   _              _____                     
|  _  |_ _| |_| |_ ___ ___   |  _  |___ ___ ___ ___ ___ 
|   __| | |  _|   | . |   |  |   __| .'|  _|_ -| -_|  _|
|__|  |_  |_| |_|_|___|_|_|  |__|  |__,|_| |___|___|_|  
    |___|                                             
    ''')

# Main driver
if __name__ == "__main__":
    # Arguments Parser
    arg = argparse.ArgumentParser()
    arg.add_argument("grammar")
    arg.add_argument("sentence")
    printASCII()
    args = arg.parse_args()

    # Main program
    start = time()
    TestParser = Parser(args.grammar, args.sentence)
    TestParser.parse()

    # Output
    TestParser.result()
    timeTaken = time()-start

    print(f"Time taken: {timeTaken} s")
