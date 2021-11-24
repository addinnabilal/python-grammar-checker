import tokenizer
import sys
def checkExpression(token):
    index=0
    while index <len(token):
        if index==0:
            if (token[index][1]=="OR" or token[index][1]=="AND" or token[index][1]=="ISEQ" or token[index][1]=="NEQ" or token[index][1]=="EQ" or token[index][1]=="ADD" or token[index][1]=="SUB" or token[index][1]=="MUL" or token[index][1]=="POWER" or token[index][1]=="DIV" or token[index][1]=="DIVEQ" or token[index][1]=="MULEQ" or token[index][1]=="ADDEQ" or token[index][1]=="POWEREQ" or token[index][1]=="MODEQ" or token[index][1]=="LESS" or token[index][1]=="LEQ" or token[index][1]=="GREATER"  or token[index][1]=="GEQ" or token[index][1]=="XOR" or token[index][1]=="BLS" or token[index][1]=="BRS" or token[index][1]=="COLON" or token[index][1]=="SEMICOLON" or token[index][1]=="RAB" or token[index][1]=="RCB" or token[index][1]=="LP" or token[index][1]=="POINT" or token[index][1]=="COMMA" or token[index][1]=="MOD" or token[index][1]=="ASSIGN" or token[index][1]=="ARROW"):
                print_error(token)
        if token[index][1]=="NEWLINE":
            if index+1<len(token):
                if (token[index+1][1]=="OR" or token[index+1][1]=="AND" or token[index+1][1]=="ISEQ" or token[index+1][1]=="NEQ" or token[index+1][1]=="EQ" or token[index+1][1]=="ADD" or token[index+1][1]=="SUB" or token[index+1][1]=="MUL" or token[index+1][1]=="POWER" or token[index+1][1]=="DIV" or token[index+1][1]=="DIVEQ" or token[index+1][1]=="MULEQ" or token[index+1][1]=="ADDEQ" or token[index+1][1]=="POWEREQ" or token[index+1][1]=="MODEQ" or token[index+1][1]=="LESS" or token[index+1][1]=="LEQ" or token[index+1][1]=="GREATER"  or token[index+1][1]=="GEQ" or token[index+1][1]=="XOR" or token[index+1][1]=="BLS" or token[index+1][1]=="BRS" or token[index+1][1]=="COLON" or token[index+1][1]=="SEMICOLON" or token[index+1][1]=="RAB" or token[index+1][1]=="RCB" or token[index+1][1]=="LP"  or token[index+1][1]=="MOD" or token[index+1][1]=="ASSIGN" or token[index+1][1]=="ARROW"):
                    print_error(token)
        if (token[index][1]=="ID" or token[index][1]=="NUM" or token[index][1]=="STRING" or token[index][1]=="RAB" or token[index][1]=="RCB"or token[index][1]=="RP"):
            if (index+1)<len(token):
                if (token[index+1][1]=="OR" or token[index+1][1]=="AND" or token[index+1][1]=="ISEQ" or token[index+1][1]=="NEQ" or token[index+1][1]=="EQ" or token[index+1][1]=="ADD" or token[index+1][1]=="SUB" or token[index+1][1]=="MUL" or token[index+1][1]=="POWER" or token[index+1][1]=="DIV" or token[index+1][1]=="DIVEQ" or token[index+1][1]=="MULEQ" or token[index+1][1]=="POWEREQ" or token[index+1][1]=="MODEQ" or token[index+1][1]=="ADDEQ" or token[index+1][1]=="LESS" or token[index+1][1]=="LEQ" or token[index+1][1]=="GREATER"  or token[index+1][1]=="GEQ" or token[index+1][1]=="XOR" or token[index+1][1]=="BLS" or token[index+1][1]=="BRS" or token[index+1][1]=="MOD" or token[index+1][1]=="ASSIGN" or token[index+1][1]=="ARROW"):
                    if (index+2)<len(token):
                        if not(token[index+2][1]=="TYPE" or token[index+2][1]=="LP" or token[index+2][1]=="LAB" or token[index+2][1]=="LCB" or token[index+2][1]=="NUM" or token[index+2][1]=="STRING" or token[index+2][1]=="ID" or token[index+2][1]=="TRUE" or token[index+2][1]=="FALSE" or token[index+2][1]=="NONE"): 
                            print_error(token)

                        else:
                            if (index+3)<len(token):
                                if (token[index+3][1]=="EQ"):
                                    print_error(token)
                    else:
                        print_error(token)
        if token[index][1]=="NUM":
            if (index+1)<len(token):
                if token[index+1][1]=="ID":
                    print_error(token)
        index+=1

def print_error(token):
    print("Syntax Error\nError at expression:", end=" ")
    for elmt in token:
        print(elmt[0], end="")
    sys.exit(1)

