def is_valid(t_min, t_max, letter, password):
    times = 0
    for l in password:
        if l == letter:
            times += 1
    if times < t_min or times > t_max:
        return False
    return True


with open('input.txt') as f:
    inputs = []
    total_valid = 0
    for l in f:
        parts = l.split(" ")

        t_min = int(parts[0].split("-")[0])
        t_max = int(parts[0].split("-")[1])
        letter = parts[1][0]
        password = parts[2]
        inputs.append(is_valid(t_min, t_max, letter, password))
    res = sum([1 for i in inputs if i is True])
    print(res)




