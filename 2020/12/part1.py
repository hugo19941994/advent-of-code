instructions = []
with open('input.txt') as f:
    for line in f:
        instructions.append((line[0], int(line[1:].strip())))
print(instructions)

# ship starts facing east
#  N
# W E
#  S

#        N, E, S, W
dists = [0, 0, 0, 0]
direction = 1
for ins in instructions:
    if ins[0] == 'N':
        dists[0] += ins[1]
    elif ins[0] == 'S':
        dists[2] += ins[1]
    elif ins[0] == 'E':
        dists[1] += ins[1]
    elif ins[0] == 'W':
        dists[3] += ins[1]
    elif ins[0] == 'L':
        amount = int(ins[1]/90)
        direction = (direction - amount) % 4
    elif ins[0] == 'R':
        amount = int(ins[1]/90)
        direction = (direction + amount) % 4
    elif ins[0] == 'F':
        dists[direction] += ins[1]


print(abs(dists[0] - dists[2]) + abs(dists[1] - dists[3]))