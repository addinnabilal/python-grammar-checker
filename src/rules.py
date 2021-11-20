import lexer

# blm bisa handle multiline string
rules = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'\"\"\"[\w\W\n+]*\"\"\"', None),
    (r'\'\'\'[\w\W\n+]*\'\'\'', None),
    (r'\:=',"ASSIGN"),
    (r'\:==',"ISEQ"),
    (r'\(',"LP"),
    (r'\)',"RP"), #rigth parantheses
    (r'\;', "SC"), #semicolon
    (r'\:', "COLON"),
    (r'\+',"ADD"),
    (r'-',"SUB"),
    (r'\*',"MUL"),
    (r'/',"DIV"),
    (r'<=',"LEQ"),
    (r'<',"LESS"),
    (r'>=',"GEQ"),
    (r'>',"GREATER"),
    (r'=',"EQ"), #
    (r'!=',"NEQ"),
    (r'/=',"DIVEQ"), 
    (r'\*=',"MULEQ"),    
    (r'\+=',"ADDEQ"), 
    (r'!=',"NEQ"),
    (r'\.',"POINT"), 
    (r'\,',"COMMA"),
    (r'\%',"MOD"), 
    (r'\*\*,',"POWER"),
    (r'\->,',"ARROW"),
    (r'\[',"LAB"), #left angle bracket 
    (r'\],',"RAB"), #right angle bracket
    (r'\{',"LCB"), #left curly bracket 
    (r'\},',"RCB"), #right curly bracket
    (r'\band\b',"AND"),
    (r'\bor\b', "OR"),
    (r'\bnot\b',"NOT"),
    (r'\bif\b', "IF"),
    (r'\bthen\b',"THEN"),
    (r'\belse\b', "ELSE"),
    (r'\bwhile\b',"WHILE"),
    (r'\bdo\b',"DO"),
    (r'\bend\b',"END"),
    (r'\bFalse\b',"FALSE"),
    (r'\bclass\b', "CLASS"),
    (r'\bis\b',"IS"),
    (r'\bcontinue\b',"CONTINUE"),
    (r'\bfor\b',"FOR"),
    (r'\bTrue\b',"TRUE"),
    (r'\bdef\b', "DEF"),
    (r'\bfrom\b',"from"),
    (r'\bwith\b',"WITH"),
    (r'\bas\b',"AS"),
    (r'\belif\b',"ELIF"),
    (r'\bimport\b',"IMPORT"),
    (r'\bpass\b', "PASS"),
    (r'\bbreak\b',"BREAK"),
    (r'\bin\b',"IN"),
    (r'\braise\b',"RAISE"),
    (r'[\+\-]?[0-9]+', "NUM"),
    (r'[\+\-]?[0-9]+\.[0-9]+', "NUM"),
    (r'\"[^\n]*\"', "STRING"),
    (r'\'[^\n]*\'', "STRING"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
]

def imp_lex(characters):
    return lexer.lex(characters, rules)
