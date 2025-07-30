from collections import defaultdict

def check_num_is_valid(rules, num):
    for rule in rules:
        if num in rule[1]:
            return True
    return False

rules = []
with open('input.txt') as f:
    # load rules
    for _ in range(20):
        line = f.readline().strip()
        line_s = line.split(':')
        name = line_s[0]
        valid_nums = []
        line_r = line_s[1].strip().split(' or ')
        for rule in line_r:
            r = rule.split('-')
            for i in range(int(r[0]), int(r[1]) + 1):
                valid_nums.append(i)

        rules.append((name, valid_nums))

    for _ in range(2):
        f.readline()

    # load my ticket
    my_ticket = list(map(int, f.readline().strip().split(',')))

    for _ in range(2):
        f.readline()

    # load nearby tickets and discard non valid ones
    valid_tickets = []
    while line := f.readline():
        line = list(map(int, line.strip().split(',')))
        valid = True
        for num in line:
            if not check_num_is_valid(rules, num):
                valid = False
                break
        if valid is True:
            valid_tickets.append(line)


print(valid_tickets)

# create a list of indexes and field possible field candidates (e.g 0: [a, b, c], 1: [b, c])
discarded = defaultdict(list)  # to keep track of removed elements
possibilities = defaultdict(set)
for ticket in valid_tickets:
    for idx, num in enumerate(ticket):
        for rule in rules:
            if num in rule[1] and rule[0] not in discarded[idx]:
                possibilities[idx].add(rule[0])
            else:
                if rule[0] in possibilities[idx]:
                    possibilities[idx].remove(rule[0])
                discarded[idx].append(rule[0])
print(possibilities)

# filter fields until each index only has one remaining field
already_filtered = []
while True:
    tracker = None
    candidate = None
    for idx, p in possibilities.items():
        if len(p) == 1 and p not in already_filtered:
            tracker = idx
            candidate = next(iter(p))
            already_filtered.append(p)

    # everything has been filtered
    if tracker is None:
        break

    print(candidate)
    for key in possibilities.keys():
        if key != tracker:
            if candidate in possibilities[key]:
                print(f'removing {candidate} for {key}')
                possibilities[key].remove(candidate)
    print(possibilities)

# multiply values of the departure fields from my ticket
answer = 1
for key, val in possibilities.items():
    if 'departure' in next(iter(val)):
        answer *= my_ticket[key]
print(answer)