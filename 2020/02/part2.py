def is_valid(pos_1, pos_2, letter, password):
    return (password[pos_1] == letter) ^ (password[pos_2] == letter)


with open('input.txt') as f:
    inputs = []
    total_valid = 0
    for l in f:
        parts = l.split(" ")

        pos_1 = int(parts[0].split("-")[0]) - 1
        pos_2 = int(parts[0].split("-")[1]) - 1
        letter = parts[1][0]
        password = parts[2]
        inputs.append(is_valid(pos_1, pos_2, letter, password))
    res = sum([1 for i in inputs if i is True])
    print(res)




