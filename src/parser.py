import os
import argparse
import converter_to_cnf
import tokenizer

class Node:
    # Initialize the node with two child nodes, right node can be empty
    def __init__(self, sym, left, right=None):
        self.sym = sym
        self.left = left
        self.right = right

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
        l = len(self.input)
        self.parsetable = [[[] for x in range(l-y)] for y in range(l)]

        # Substrings of length 1
        for i, word in enumerate(self.input):
            for rule in self.grammar:
                if f"'word'" == rule[1]:
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
                        lNodes = [n for n in lcell if n.symbol == rule[1]]
                        if lNodes:
                            rNodes = [n for n in rcell if n.symbol == rule[2]]
                            self.parsetable[sub-1][start].extend([Node(rule[0], left, right) for left in lNodes for right in rNodes])

    # Open grammar from file
    def grammarFromFile(self, g):
        cfg = converter_to_cnf.read_grammar(g)
        self.grammar = converter_to_cnf.convert_grammar(cfg)

    # Result decider according to the CYK formula
    def result(self):
        startSymbol = self.grammar[0][0]
        if len(self.input):
            nodes = [n for n in self.parsetable[-1][0] if n.symbol == startSymbol]
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

    TestParser = Parser(args.grammar, args.sentence)
    TestParser.parse()
    TestParser.result()
