with open('input.txt') as f:
    opcodes = [int(i) for i in f.read().split(',')]

opcodes[1] = 12
opcodes[2] = 2

i = 0
while True:
    if opcodes[i] == 1:
        p1 = opcodes[opcodes[i+1]]
        p2 = opcodes[opcodes[i+2]]
        p3 = opcodes[i+3]
        opcodes[p3] = p1 + p2

        i += 4
        continue

    if opcodes[i] == 2:
        p1 = opcodes[opcodes[i+1]]
        p2 = opcodes[opcodes[i+2]]
        p3 = opcodes[i+3]
        opcodes[p3] = p1 * p2

        i += 4
        continue

    if opcodes[i] == 99:
        print('HALT')
        break

    else:
        print('ERROR')
        break


print(opcodes[0])
