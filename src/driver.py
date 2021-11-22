
import sys
from rules import *

def tokenizer(text):
    tokens = imp_lex(text)
    for token in tokens:
        print(token)
    

if __name__== "__main__":
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokenizer(characters)