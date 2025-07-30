wires = []
with open('input.txt') as f:
    for line in f:
        wires.append(line.split(','))

p_positions = []
for wire in wires:
    positions = {}
    current = (0, 0)
    steps = 0
    for d in wire:
        direction = d[0]
        mag = int(d[1:])
        for i in range(mag):
            if direction == 'U':
                current = (current[0] + 1, current[1])
            elif direction == 'D':
                current = (current[0] - 1, current[1])
            elif direction == 'L':
                current = (current[0], current[1] - 1)
            elif direction == 'R':
                current = (current[0], current[1] + 1)
            steps += 1
            positions[current] = steps
    p_positions.append(positions)


#print(p_positions)
matches = []
for p1 in p_positions[0].keys():
    if p1 in p_positions[1].keys():
        p_positions[0][p1] += p_positions[1][p1]
        matches.append(p_positions[0][p1])
#print(matches)

# sort matches
sort_matches = sorted(matches)
print(sort_matches[0])
