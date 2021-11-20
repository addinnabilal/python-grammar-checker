import sys
import re

def lex(textinput, token_exprs):
    pos = 0
    tokens = []
    line=1
    while pos < len(textinput):
        match = None
        if (textinput[pos]=="\n"):
            line+=1
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(textinput, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s at line %d \n' % (text[pos],line))
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens