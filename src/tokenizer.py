import sys
from rules import *
from expression_checker import *

def tokenizer(text):
    tokens = imp_lex(text)
    output=[]
    for token in tokens:
        checkExpression(token)
        for lexemme in token:
            output.append(lexemme[1])
    joined = " ".join(output)

    output_file=open("tokenized.txt","w")
    output_file.write(joined)
    output_file.close
    

if __name__== "__main__":
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokenizer(characters)