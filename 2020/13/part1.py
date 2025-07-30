from math import prod

with open('input.txt') as f:
    ts = int(f.readline().strip())
    l = f.readline().strip().split(',')
    lines = [(idx, int(line)) for idx, line in enumerate(l) if line != 'x']
    #lines = [x for i, x in linesx]

print(ts)
print(lines)

line_result = []
for _, line in lines:
    ts_line = 0
    while ts_line < ts:
        ts_line += line
    line_result.append((line, ts_line - ts))

res = min(line_result, key=lambda x: x[1])
print(res[0] * res[1])

# Couldn't really quite figure it out. Googled a bit...
# Part 2. tip chinese remainder theorem
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Computation
total = 0
# multiply all lines (max possible value, repeats pattern afterwards)
N = prod([x[1] for x in lines])
for index, line in lines:
    base = N // line
    # modular multiplicative inverse
    total += (line - index) * base * pow(base, -1, line)
    total %= N
print(total)

# 100000000000000 at least
# 803025030761664
