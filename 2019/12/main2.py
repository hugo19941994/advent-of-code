import itertools
import json
import copy

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

moons = {}

with open('input.txt') as f:
    for num, line in enumerate(f):
        moons[num] = {'pos': {}, 'vel':{}}
        moons[num]['pos']['x'] = int(line[line.find('x') + 2:line.find(',', line.find('x'))])
        moons[num]['pos']['y'] = int(line[line.find('y') + 2:line.find(',', line.find('y'))])
        moons[num]['pos']['z'] = int(line[line.find('z') + 2:line.find('>')])

        moons[num]['vel']['x'] = 0
        moons[num]['vel']['y'] = 0
        moons[num]['vel']['z'] = 0

initial = copy.deepcopy(moons)

values = []
# Compute cycle in x y and z separately, then LCM the results
for i in ['x', 'y', 'z']:
    count = 0
    while True:
        for pair in itertools.combinations(moons.keys(), 2):
            moon1 = moons[pair[0]]
            moon2 = moons[pair[1]]
            # Apply gravity
            if moon1['pos'][i] > moon2['pos'][i]:
                moon1['vel'][i] -= 1
                moon2['vel'][i] += 1
            elif moon1['pos'][i] < moon2['pos'][i]:
                moon1['vel'][i] += 1
                moon2['vel'][i] -= 1

        # Apply velocity
        for moon in moons.keys():
            moons[moon]['pos'][i] += moons[moon]['vel'][i]

        count += 1
        if moons == initial:
            print(i, count)
            values.append(count)
            break

print(int(lcm(values[0], lcm(values[1], values[2]))))
