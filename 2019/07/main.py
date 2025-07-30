import itertools

with open('input.txt') as f:
    or_opcodes = [int(i) for i in f.read().split(',')]


def get_val(mode, d, prog):
    if mode == "0":
        return prog[d]
    elif mode == "1":
        return d
    else:
        print("MODE ERROR")
        exit(0)


def run(prog, input1, input2):
    i = 0
    inp = input1
    while True:
        opcode = str(prog[i]).zfill(5)
        mode = opcode[:-2]
        inst = int(opcode[-2:])

        #print('opcode', opcode)
        #print('mode', mode)
        #print('inst', inst)

        if inst == 1:
            p1 = get_val(mode[2], prog[i+1], prog)
            #print('p1', p1)
            p2 = get_val(mode[1], prog[i+2], prog)
            #print('p2', p2)
            prog[prog[i+3]] = p1 + p2
            #print('res', prog[prog[i+3]])

            i += 4
            continue

        if inst == 2:
            p1 = get_val(mode[2], prog[i+1], prog)
            #print('p1', p1)
            p2 = get_val(mode[1], prog[i+2], prog)
            #print('p2', p2)
            prog[prog[i+3]] = p1 * p2
            #print('res', prog[prog[i+3]])

            i += 4
            continue

        if inst == 3:
            #inp = int(input("input: "))
            prog[prog[i+1]] = inp
            inp = input2
            i += 2
            continue

        if inst == 4:
            val = get_val(mode[2], prog[i+1], prog)
            #print('OUTPUT', val)
            return val
            i += 2
            continue

        if inst == 5:
            p1 = get_val(mode[2], prog[i+1], prog)
            if p1 != 0:
                # Maybe don't check val
                i = get_val(mode[1], prog[i+2], prog)
            else:
                i += 3
            continue

        if inst == 6:
            p1 = get_val(mode[2], prog[i+1], prog)
            if p1 == 0:
                # Maybe don't check val
                i = get_val(mode[1], prog[i+2], prog)
            else:
                i += 3
            continue

        if inst == 7:
            p1 = get_val(mode[2], prog[i+1], prog)
            p2 = get_val(mode[1], prog[i+2], prog)
            if p1 < p2:
                prog[prog[i+3]] = 1
            else:
                prog[prog[i+3]] = 0
            i += 4
            continue

        if inst == 8:
            p1 = get_val(mode[2], prog[i+1], prog)
            p2 = get_val(mode[1], prog[i+2], prog)
            if p1 == p2:
                prog[prog[i+3]] = 1
            else:
                prog[prog[i+3]] = 0
            i += 4
            continue

        if inst == 99:
            print('HALT')
            break

        else:
            print('ERROR')
            exit(0)


a = [0, 1, 2, 3, 4]
b = itertools.permutations(a)
results = []
for s in list(set(itertools.permutations(a))):
    val = 0
    print(s)
    for i in s:
        opcodes = or_opcodes.copy()
        val = run(opcodes, i, val)
    print(val)
    results.append((s, val))

print(max(results, key=lambda x: x[1]))
