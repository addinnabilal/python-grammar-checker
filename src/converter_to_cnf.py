RULE_DICT = {} # Kamus untuk menyimpan cnf

def write_cnf(grammar):
    # Menulis hasil convert ke dalam file txt
    file = open('grammarcnf.txt', 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()


def read_grammar(filename):
    # Baca cfg dari file
    with open(filename) as cfg:
        lines = cfg.readlines()
    return [x.replace("->", "").split() for x in lines]

def add_rule(rule):
    # Menambah aturan ke kamus
    global RULE_DICT

    if rule[0] not in RULE_DICT:
        RULE_DICT[rule[0]] = []
    RULE_DICT[rule[0]].append(rule[1:])

def convert_grammar(grammar):
    # Meng-convert cfg menjadi cnf
    global RULE_DICT

    unit_prod, result = [], []
    idx = 0

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            unit_prod.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    rule[item[1]] = f"{rule[0]}{str(idx)}"
                    new_rules += [f"{rule[0]}{str(idx)}", item[0]]
                idx += 1
            while len(rule) > 3:
                new_rules.append([f"{rule[0]}{str(idx)}", rule[1], rule[2]])
                rule = [rule[0]] + [f"{rule[0]}{str(idx)}"] + rule[3:]
                idx += 1
        if rule:
        	add_rule(rule)
        	result.append(rule)
        if new_rules:
        	for i in range(len(new_rules)):
           		result.append(new_rules[i])

    while unit_prod:
        rule = unit_prod.pop()
        if rule[1] in RULE_DICT:
            for item in RULE_DICT[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.append(new_rule)
                else:
                    unit_prod.append(new_rule)
                add_rule(new_rule)
    return result

def makeCnf(filename):
    cfg = read_grammar(filename)
    cnf = convert_grammar(cfg)
    write_cnf(cnf)

if __name__ == '__main__':
    makeCnf('testcfg.txt')
