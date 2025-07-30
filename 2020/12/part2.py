instructions = []
with open('input.txt') as f:
    for line in f:
        instructions.append((line[0], int(line[1:].strip())))
print(instructions)

#  N
# W E
#  S

# waypoint starts at 10E 1N relative to ship
waypoint = [1, 10]

#        N, E NE positive, SW negative
dists = [0, 0]
for ins in instructions:
    if ins[0] == 'N':
        waypoint[0] += ins[1]
    elif ins[0] == 'S':
        waypoint[0] -= ins[1]
    elif ins[0] == 'E':
        waypoint[1] += ins[1]
    elif ins[0] == 'W':
        waypoint[1] -= ins[1]
    elif ins[0] == 'L':
        # 2 1
        # 1 -2
        # -2 -1
        # -1 2
        amount = int(ins[1]/90)
        for i in range(amount):
            x, y = waypoint
            if x < 0 and y < 0:
                waypoint = [-abs(y), abs(x)]
            elif x < 0:
                waypoint = [abs(y), abs(x)]
            elif y < 0:
                waypoint = [-abs(y), -abs(x)]
            else:
                waypoint = [abs(y), -abs(x)]
    elif ins[0] == 'R':
        # 2 1
        # -1 2
        # -2 -1
        # 1 -2
        amount = int(ins[1]/90)
        for _ in range(amount):
            x, y = waypoint
            if x < 0 and y < 0:
                waypoint = [abs(y), -abs(x)]
            elif x < 0:
                waypoint = [-abs(y), -abs(x)]
            elif y < 0:
                waypoint = [abs(y), abs(x)]
            else:
                waypoint = [-abs(y), abs(x)]
    elif ins[0] == 'F':
        amount = ins[1]
        dists[0] += (waypoint[0] * amount)
        dists[1] += (waypoint[1] * amount)


print(abs(dists[0]) + abs(dists[1]))