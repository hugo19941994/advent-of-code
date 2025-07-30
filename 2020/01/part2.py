
with open('input.txt') as f:
    inputs = [int(l.strip()) for l in f]

for x in inputs:
    for y in inputs:
        for z in inputs:
            if x + y + z == 2020:
                print(x, y, z, x*y*z)
