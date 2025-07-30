and_bitmask = 0
or_bitmask = 0
memory = {}

with open('input.txt') as f:
   for line in f:
       if 'mask' in line:
           and_bitmask = int(line[7:].replace('X', "1"), base=2)
           or_bitmask = int(line[7:].replace('X', "0"), base=2)
       else:
           addr = int(line[line.find('[') + 1:line.find(']')])
           value = int(line[line.find('=') + 2:])
           value |= or_bitmask
           value &= and_bitmask
           memory[addr] = value

total = 0
for val in memory.values():
    total += val
print(total)

bitmask = 0
or_bitmask = 0
memory = {}
# part 2
with open('input.txt') as f:
    for line in f:
        if 'mask' in line:
            bitmask = line[7:]
            or_bitmask = int(line[7:].replace('X', "0"), base=2)
        else:
            addr = int(line[line.find('[') + 1:line.find(']')])
            addr |= or_bitmask
            value = int(line[line.find('=') + 2:])
            addresses = [bin(addr)]
            x_idx = [i for i, x in enumerate([x == 'X' for x in bitmask]) if x]
            for idx in x_idx:
                for _ in range(len(addresses)):
                    a = addresses.pop(0)
                    a = bytearray(a, 'ascii')[2:].zfill(36)
                    a[idx] = ord('0')
                    addresses.append(bin(int(a, base=2)))
                    a[idx] = ord('1')
                    addresses.append(bin(int(a, base=2)))

            for addrFloating in set(addresses):
                memory[int(addrFloating, base=2)] = value

total = 0
for val in memory.values():
    total += val
print(total)

# 22998646173 too low
# 3219837697833