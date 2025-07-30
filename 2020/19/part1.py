from itertools import product


def parse_rules(rule):
    possibilities = []
    # first level - one or another rule
    for pos in rule:
        ps = []
        # second level - concatenate two or more rules
        for r in pos:
            if r in ('a', 'b'):
                return [r]
            ps.append(parse_rules(rule_book[r]))
        for p in product(*ps):
            possibilities.append(''.join(p))
    return possibilities


total = 0
rule_book = {}
with open('input.txt') as f:
    # load rules
    for line in f:
        if line != '\n':
            num, rules = line.strip().split(':')
            rules = list(map(str.strip, rules.replace('"', '').split('|')))
            rules = list(map(lambda x: x.split(' '), rules))
            rule_book[num] = rules
        else:
            break

    # parse rules and store all possible values
    rules = parse_rules(rule_book['0'])

    # check how many from the input are valid
    for line in f:
        if line.strip() in rules:
            total += 1

print(total)

