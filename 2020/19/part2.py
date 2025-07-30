"""
like in day 13, part 2 was over my head
I knew being a infinite data structure (due to recursion) generators would be the way to go,
    but I couldn't really think of a good way of checking the ANDs sequentially
This great implementation is from https://www.youtube.com/watch?v=qo3ELw4yq_M&feature=youtu.be
"""""


def check_and(g_rules, rules, string):
    # the AND sequence of rules has been check in its entirety
    if not rules:
        yield string

    else:
        # check current rules
        idx, *rules = rules  # split [1, 2, 3] -> 1, [2, 3]
        for string in run(g_rules, idx, string):  # drill down and check the current rule (e.g. 1)
            yield from check_and(g_rules, rules, string)  # check the remaining rules (e.g [2, 3])


def run(g_rules, rule_idx, string):
    # if rule is a or b return the consumed string IF it's the same
    if rule_idx not in g_rules and rule_idx in ('a', 'b'):
        if string and string[0] == rule_idx:
            yield string[1:]
        # if not returns None, which terminates the loop (next run will have not string condition)
    else:
        # check the sequence of AND rules if it's not just a or b
        for rules in g_rules[rule_idx]:
            yield from check_and(g_rules, rules, string)


def check(string):
    # continues executing run until a None is returned or a '' is returned
    return any('' == x for x in run(rule_book, '0', string))


total = 0
rule_book = {}
with open('input_p2.txt') as f:
    # load rules
    for line in f:
        if line != '\n':
            num, rules = line.strip().split(':')
            rules = list(map(str.strip, rules.replace('"', '').split('|')))
            rules = list(map(lambda x: x.split(' '), rules))
            rule_book[num] = rules
        else:
            break
    # check how many from the input are valid
    for line in f:
        if check(line.strip()):
            total += 1

print(total)

