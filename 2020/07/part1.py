# load rules
rules = {}


def load_rule(line):
    color, rest = line.strip().split(' bags contain ')
    internal_rules = rest.replace(' bags', '').replace(' bag', '').replace('.', '').split(', ')
    if internal_rules == ['no other']:
        internal_rules = []
    print(color)
    print(internal_rules)
    rules[color] = internal_rules


with open('input.txt') as f:
    for line in f:
        load_rule(line)

print(rules)


def count_color(key):
    to_return = 0
    for val in rules[key]:
        amount = int(val[:1])
        color = val[2:]
        if color == 'shiny gold':
            to_return += amount
        else:
            to_return += amount * count_color(color)
    return to_return

shiny_gold = {}
for color in rules.keys():
    shiny_gold[color] = count_color(color)

print(shiny_gold)
print(len([x for x in shiny_gold.values() if x != 0]))

print()