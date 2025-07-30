import numpy as np

wires = []
with open('input.txt') as f:
    for line in f:
        wires.append(line.split(','))

p_positions = []
for wire in wires:
    positions = set()
    current = (0, 0)
    positions.add(current)
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
            positions.add(current)
    p_positions.append(positions)


matches = []
for p1 in p_positions[0]:
    if p1 in p_positions[1]:
        matches.append(p1)
print(matches)

# sort matches
sort_matches = sorted(matches, key=lambda x: abs(0 - x[0]) + abs(0 - x[1]))
print(sort_matches[1])
x = sort_matches[1]
print(abs(0 - x[0]) + abs(0 - x[1]))
