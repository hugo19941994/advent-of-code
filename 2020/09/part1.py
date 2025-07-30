from itertools import combinations

def load():
    with open('input.txt') as f:
        return [int(line.strip()) for line in f]

nums = load()

# Part 1
for i in range(25, len(nums)):
    found = False
    for comb in combinations(nums[i-25:i], 2):
        add = comb[0] + comb[1]
        if add == nums[i]:
            found = True
            break
    if found is False:
        print(nums[i])
        num_to_find = nums[i]
        break


# Part 2
def getAllWindows(nums):
    for w in range(2, len(nums) + 1):
        for i in range(len(nums) - w + 1):
            yield nums[i:i + w]


for comb in getAllWindows(nums):
    if sum(comb) == num_to_find:
        sorted_comb = sorted(comb)
        print(sorted_comb[0] + sorted_comb[len(sorted_comb) - 1])
        break
