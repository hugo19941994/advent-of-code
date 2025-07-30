with open('input.txt') as f:
    jolts = [int(line.strip()) for line in f]

# Add charging outlet
jolts.append(0)
jolts.sort()

# Add device's built-in adapter
jolts.append(jolts[-1] + 3)

print(jolts)

diffs = []
for i in range(len(jolts) - 1):
    diffs.append(jolts[i+1] - jolts[i])
print(diffs)

print(f"1: {(diff_1 := len([i for i in diffs if i == 1]))}")
print(f"3: {(diff_3 := len([i for i in diffs if i == 3]))}")
print(diff_1 * diff_3)

# Part 2

# dict to store already computed answers
DP = {}

def dp(i: int):
    # finished searching
    if i == jolts[-1]:
        return 1

    # pre-computed
    if i in DP:
        return DP[i]

    # search for the remaining values
    total = 0
    for j in [j for j in jolts if i + 3 >= j > i]:
        total += dp(j)
    DP[i] = total
    return total

print(dp(0))
