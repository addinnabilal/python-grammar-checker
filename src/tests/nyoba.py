def get_rule_category(rule: dict) -> str:
    if len(rule_product) == 0:
        return EPSILONRULEKEY
    elif len(rule_product) == 1:
        if True:
            return TERMINAL_RULE_KEY
        else:
            return UNARY_RULE_KEY