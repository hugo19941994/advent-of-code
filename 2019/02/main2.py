with open('input.txt') as f:
    opcodes = [int(i) for i in f.read().split(',')]


def run(prog):
    i = 0
    while True:
        if prog[i] == 1:
            p1 = prog[opcodes[i+1]]
            p2 = prog[opcodes[i+2]]
            p3 = prog[i+3]
            prog[p3] = p1 + p2

            i += 4
            continue

        if prog[i] == 2:
            p1 = prog[opcodes[i+1]]
            p2 = prog[opcodes[i+2]]
            p3 = prog[i+3]
            prog[p3] = p1 * p2

            i += 4
            continue

        if prog[i] == 99:
            print('HALT')
            break

        else:
            print('ERROR')
            exit(0)


for noun in range(0, 100):
    for verb in range(0, 100):
        prog = opcodes.copy()

        prog[1] = noun
        prog[2] = verb
        run(prog)
        if prog[0] == 19690720:
            print(noun)
            print(verb)
            exit(0)
