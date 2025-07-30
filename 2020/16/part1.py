def check_num_is_valid(rules, num):
    for rule in rules:
        if num in rule[1]:
            return 0
    return num

rules = []
with open('input.txt') as f:
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

    for _ in range(5):
        f.readline()

    error_rate = 0
    while line := f.readline():
        line = list(map(int, line.strip().split(',')))
        for num in line:
            error_rate += check_num_is_valid(rules, num)
    print(error_rate)
# 2481059 too high

