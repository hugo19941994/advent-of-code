with open('input.txt') as f:
    modules_mass = [int(i) for i in f.read().splitlines()]

total_fuel = sum(map(lambda x: (x // 3) - 2, modules_mass))

print(f"Total fuel required: {total_fuel}")
