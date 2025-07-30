def calc_cubes_to_check(active_cubes):
    cubes_to_check = set()
    for cube in active_cubes:
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    cubes_to_check.add((cube[0] + x, cube[1] + y, cube[2] + z))
    return cubes_to_check


active_cubes = set()
with open('input.txt') as f:
    for row, line in enumerate(f):
        for col, char in enumerate(line.strip()):
            if char == '#':
                active_cubes.add((col, 0, row))

print(f'iteration: 0, active cubes {len(active_cubes)}')
for iteration in range(1, 7):
    iteration_active_cubes = set()
    for cube in calc_cubes_to_check(active_cubes):
        amount_neighbors = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if x == 0 and y == 0 and z == 0:
                        continue
                    if (cube[0] + x, cube[1] + y, cube[2] + z) in active_cubes:
                        amount_neighbors += 1
        # check if current_cube is active
        if cube in active_cubes and 2 <= amount_neighbors <= 3:
            iteration_active_cubes.add(cube)
        elif cube not in active_cubes and amount_neighbors == 3:
            iteration_active_cubes.add(cube)
    active_cubes = iteration_active_cubes
    print(f'iteration: {iteration}, active cubes {len(active_cubes)}')
print(active_cubes)
