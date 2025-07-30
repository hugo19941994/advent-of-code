with open('input.txt') as f:
    inputs = [int(l.strip()) for l in f]

for x in inputs:
    for y in inputs:
        if x + y == 2020:
            print(x*y)

seen = {}
for x in inputs:
    seen[2020-x] = True
    for y in inputs:
        if y in seen:
            print(x, y, x*y)
            exit()
