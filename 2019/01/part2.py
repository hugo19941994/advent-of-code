def calc_total_fuel(mass):
    fuel = (mass // 3) - 2

    if fuel <= 0:
        return 0
    else:
        return fuel + calc_total_fuel(fuel)


with open('input.txt') as f:
    modules_mass = [int(i) for i in f.read().splitlines()]

total_fuel = sum(map(calc_total_fuel, modules_mass))
print(f"Total fuel required: {total_fuel}")
