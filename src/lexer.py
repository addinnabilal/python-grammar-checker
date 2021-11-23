import sys
import re

def lex(textinput, token_exprs):
    pos = 0
    tokens = [[]]
    line=0
    while pos < len(textinput):
        match = None
        if (textinput[pos]=="\n"):
            line+=1
            tokens.append([])
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(textinput, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens[line].append(token)
                break
        if not match:
            print("Syntax Error")
            sys.stderr.write('Illegal character  %s found at line %d\n' % (textinput[pos],line+1)) # masih error
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens