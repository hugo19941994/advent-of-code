import itertools
moons = {}

with open('input.txt') as f:
    for num, line in enumerate(f):
        moons[num] = {'pos': {}, 'vel':{}}
        moons[num]['pos']['x'] = int(line[line.find('x')+2:line.find(',', line.find('x'))])
        moons[num]['pos']['y'] = int(line[line.find('y')+2:line.find(',', line.find('y'))])
        moons[num]['pos']['z'] = int(line[line.find('z')+2:line.find('>')])

        moons[num]['vel']['x'] = 0
        moons[num]['vel']['y'] = 0
        moons[num]['vel']['z'] = 0

print(moons)

for step in range(1000):
    for pair in itertools.combinations(moons.keys(), 2):
        print(pair)
        moon1 = moons[pair[0]]
        moon2 = moons[pair[1]]
        # Apply gravity
        for i in ['x', 'y', 'z']:
            if moon1['pos'][i] > moon2['pos'][i]:
                moon1['vel'][i] -= 1
                moon2['vel'][i] += 1
            elif moon1['pos'][i] < moon2['pos'][i]:
                moon1['vel'][i] += 1
                moon2['vel'][i] -= 1

    # Apply velocity
    for moon in moons.keys():
        for i in ['x', 'y', 'z']:
            moons[moon]['pos'][i] += moons[moon]['vel'][i]

    print(moons)

# calculate total system energy
total = 0
for m in moons.keys():
    moon = moons[m]
    potential = 0
    kinetic = 0
    for i in ['x', 'y', 'z']:
        potential += abs(moon['pos'][i])
        kinetic += abs(moon['vel'][i])
    print(potential)
    print(kinetic)
    total += potential * kinetic

print(total)





