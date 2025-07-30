# load rules
rules = {}


def load_rule(line):
    color, rest = line.strip().split(' bags contain ')
    internal_rules = rest.replace(' bags', '').replace(' bag', '').replace('.', '').split(', ')
    if internal_rules == ['no other']:
        internal_rules = []
    rules[color] = internal_rules


with open('input.txt') as f:
    for line in f:
        load_rule(line)


def count_amount(key):
    to_return = 1
    for val in rules[key]:
        amount = int(val[:1])
        color = val[2:]
        to_return += amount * count_amount(color)
    return to_return


print(count_amount('shiny gold') - 1)
# 101 too low
# 108637 too high