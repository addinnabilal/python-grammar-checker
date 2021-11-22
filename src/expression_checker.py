import tokenizer
import sys
#conditionalnya masi perlu diperbaikin
def checkExpression(token):
    index=0
    while index <len(token):
        print(token[index])
        if token[index][1]=="ID":
            if (index+2)<len(token):
                if (token[index+1][1]=="EQ" or token[index+1][1]=="NEQ" or token[index+1][1]=="ISEQ"):
                    if token[index+2][1]!=("NUM" or "STRING"):
                        print("Illegal expression")
                        sys.exit
                elif (token[index+1][1]=="ADD" or token[index+1][1]=="SUB" or token[index+1][1]=="MUL" or token[index+1][1]=="POWER" or token[index+1][1]=="DIV" or token[index+1][1]=="DIVEQ" or token[index+1][1]=="MULEQ" or token[index+1][1]=="ADDEQ" or token[index+1][1]=="LESS" or token[index+1][1]=="LEQ" or "GREATER"  or token[index+1][1]=="GEQ"):
                    if (token[index+2][1]!="NUM"):
                        print("Illegal expression") #dia masuk ke sini mulu
                        sys.exit
            else:
                if (index-1)>=0:
                    if not(token[index-1][1]=="RETURN" or token[index-1][1]=="AS" or token[index-1][1]=="IMPORT" or token[index-1][1]=="LP" or token[index-1][1]=="LCB" or token[index-1][1]=="LAB" or token[index-1][1]=="IF" or token[index-1][1]=="ELIF"  or token[index+1][1]=="ARROW" or token[index+1][1]=="COLON"):
                        print("Illegal expression")
                        sys.exit
                else:
                    print("Illegal expression")
                    sys.exit

        if token[index][1]=="NUM":
            if (index+1)<len(token):
                if token[index+1][1]=="ID":
                        print("Illegal expression")
                        sys.exit
                if (token[index+1][1]=="ADD" or token[index+1][1]=="SUB" or token[index+1][1]=="MUL" or token[index+1][1]=="POWER" or token[index+1][1]=="DIV" or token[index+1][1]=="LESS" or token[index+1][1]=="LEQ" or token[index+1][1]=="GREATER"  or token[index+1][1]=="GEQ"):
                    if (index+2)<len(token):
                        if token[index+2][1]!=("NUM"):
                            print("Illegal expression")
                            sys.exit
                    else:
                        print("Illegal expression")
                        sys.exit

        index+=1
