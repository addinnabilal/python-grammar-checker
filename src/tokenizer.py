
import sys
from rules import *

def tokenizer(text):
    tokens = imp_lex(text)
    output=[]
    for token in tokens:
        output.append(token[1])
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
       