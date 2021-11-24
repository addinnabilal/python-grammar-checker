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
    

    # CYK Algorithm
    def parse(self):
        animation = "|/-\\"
        i = 0
        l = len(self.input)
        self.parsetable = [[[] for x in range(l-y)] for y in range(l)]
        # Substrings of length 1
        for i, word in enumerate(self.input):
            for rule in self.grammar:
                if f"'{word}'" == rule[1]:
                    self.parsetable[0][i].append(Node(rule[0], word))
                    
        # Substrings 2 and greater
        for sub in range(2, l+1):
            for start in range(0, l-sub+1):
                for left_part in range(1,sub):
                    right_part = sub - left_part
                    lcell = self.parsetable[left_part-1][start]
                    rcell = self.parsetable[right_part-1][start+left_part]
                    
                    # Check the form of S -> AB
                    for rule in self.grammar:
                        lNodes = [n for n in lcell if n.sym == rule[1]]
                        if lNodes:
                            rNodes = [n for n in rcell if n.sym == rule[2]]
                            self.parsetable[sub-1][start].extend([Node(rule[0], left, right) for left in lNodes for right in rNodes])
                    
                    # Loading prompts
                    sys.stdout.write("\rParsing.." + animation[i % len(animation)])
                    sys.stdout.flush()
                    i += 1

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

    def parsev2(self):
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

    def resultv2(self):
        n = len(self.input)
        if len(self.parsetable[0][n-1]) != 0:
            print("Accepted.")
        else:
            print("Syntax error.")

    # Open grammar from file
    def grammarFromFile(self, g):
        cfg = converter_to_cnf.read_grammar(g)
        self.grammar = converter_to_cnf.convert_grammar(cfg)

    # Result decider according to the CYK formula
    def result(self):
        startSymbol = self.grammar[0][0]
        if len(self.input):
            nodes = [n for n in self.parsetable[-1][0] if n.sym == startSymbol]
            if nodes:
                print("Accepted.")
            else:
                print("Syntax error.")
        else:
            print("Accepted.")


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("grammar")
    arg.add_argument("sentence")

    args = arg.parse_args()
    start = time()
    TestParser = Parser(args.grammar, args.sentence)
    TestParser.parsev2()
    TestParser.resultv2()
    # TestParser.parse()
    # print()
    # TestParser.result()
    timeTaken = time()-start
    print(f"Time taken: {timeTaken} s")
