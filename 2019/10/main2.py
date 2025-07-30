import math
from collections import defaultdict

asteroids = []
with open('input.txt') as f:
    row = 0
    for line in f:
        for num, char in enumerate(line):
            if char == '#':
                asteroids.append((num, row))
        row += 1


pos = (17, 23)
asteroids.remove(pos)


angles = defaultdict(list)
for asteroid in asteroids:
    delta_x = asteroid[0] - pos[0]
    delta_y = asteroid[1] - pos[1]
    theta_radians = math.atan2(-delta_y, delta_x)
    angles[theta_radians].append(asteroid)

# first quadrant
q1 = sorted(list(filter(lambda x: x <= math.pi/2 and x >= 0, angles.keys())), reverse=True)
# second and third quadrant
q23 = sorted(list(filter(lambda x: x < 0 and x > -math.pi, angles.keys())), reverse=True)
# fourth quadrant
q4 = sorted(list(filter(lambda x: x <= math.pi and x > math.pi/2, angles.keys())), reverse=True)

# append quadrants in clockwise order
q = q1 + q23 + q4

print('total angles', len(angles))
print('total sum of angles in quadrants', len(q1) + len(q23)+len(q4))

# select 200th angle
# 280 groups in total, so no need for iteration
ast = angles[q[199]]
# from the 200th select the closest asteroid
asteroid = sorted(ast, key=lambda x: math.sqrt(((x[0]-pos[0])**2)+((x[1]-pos[1])**2)))[0]
print(asteroid[0] * 100 + asteroid[1])

