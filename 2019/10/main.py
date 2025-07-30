import math

asteroids = []
with open('input.txt') as f:
    row = 0
    for line in f:
        for num, char in enumerate(line):
            if char == '#':
                asteroids.append((num, row))
        row += 1

print(asteroids)

results = []
for asteroid1 in asteroids:
    angles = set()
    for asteroid2 in asteroids:
        if asteroid1 == asteroid2:
            continue
        delta_x = asteroid1[0] - asteroid2[0]
        delta_y = asteroid1[1] - asteroid2[1]
        theta_radians = math.atan2(-delta_y, delta_x)
        angles.add(theta_radians)
    results.append((len(angles), asteroid1))

print(max(results, key=lambda x: x[0]))
