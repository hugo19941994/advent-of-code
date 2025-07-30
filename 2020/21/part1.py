from collections import defaultdict
from copy import deepcopy

ingredient_counts = defaultdict(int)
d_allergens = defaultdict(set)
with open('input.txt') as f:
    for line in f:
        line = line.strip()[:-1]  # remove )\n
        ingredients, allergens = line.split(' (contains ')

        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')

        # an ingredient will only be an allergen if it appears in all foods with that allergen
        for a in allergens:
            # filter out non possible ingredients
            if a in d_allergens:
                d_allergens[a].intersection_update(ingredients)
                continue

            # initialize possibilities
            for i in ingredients:
                d_allergens[a].add(i)

        # for easier counting later
        for i in ingredients:
            ingredient_counts[i] += 1

# todo: ugly
# filter out ingredients so that only 1 remain per allergen
stop = False
while not stop:
    stop = True  # only when all allergens have 1 unique ingredient

    for k, v in deepcopy(d_allergens).items():
        if len(v) == 1:  # candidate
            ingredient = list(v)[0]

            for kk, vv in d_allergens.items():
                if kk != k and ingredient in d_allergens[kk]:
                    d_allergens[kk].remove(ingredient)
        else:
            stop = False

# sort allergens in alphabetical order and store ingredient (for part 1 & 2)
s = [list(v)[0] for k, v in sorted(d_allergens.items())]

# now count total NON allergenic ingredients
total = 0
for k in ingredient_counts.keys():
    if k in s:  # skip allergenic ingredient
        continue
    total += ingredient_counts[k]
print('part 1', total)

# sort allergens in alphabetical order, then print ingredients
print('part 2', ','.join(s))
