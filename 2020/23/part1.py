#input = list(map(int, list('253149867')))
input = list(map(int, list('389125467')))
print(input)

current_cup_idx = 0
for idx, _ in enumerate(range(100)):
    #current_cup_idx = idx % len(input)
    current_cup = input[current_cup_idx]

    # Remove the three adjacent cups
    selected_cups = []
    for _ in range(1, 4):
        selected_cups.append(input.pop((idx + 1) % len(input)))

    min_cup = min(input)
    max_cup = max(input)
    # select destination cup
    destination_num = current_cup - 1
    while destination_num in selected_cups:
        destination_num -= 1
        if destination_num < min_cup:
            destination_num = max_cup

    # get the destination cup index
    destination_cup_idx = input.index(destination_num)

    # place selected cups at the right of the destination cup
    for i, cup in enumerate(selected_cups):
        input.insert(destination_cup_idx + i + 1, cup)

    current_cup_idx = (current_cup_idx + 1) % len(input)
print(input)
