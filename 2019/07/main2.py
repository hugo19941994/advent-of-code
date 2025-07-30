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


class pc():
    def __init__(self, program):
        self.sp = 0
        self.prog = program
        self.inputs = []

    def push(self, inp):
        self.inputs.insert(0, inp)

    def run(self):
        while True:
            opcode = str(self.prog[self.sp]).zfill(5)
            mode = opcode[:-2]
            inst = int(opcode[-2:])

            if inst == 1:
                p1 = get_val(mode[2], self.prog[self.sp+1], self.prog)
                p2 = get_val(mode[1], self.prog[self.sp+2], self.prog)
                self.prog[self.prog[self.sp+3]] = p1 + p2

                self.sp += 4
                continue

            if inst == 2:
                p1 = get_val(mode[2], self.prog[self.sp+1], self.prog)
                p2 = get_val(mode[1], self.prog[self.sp+2], self.prog)
                self.prog[self.prog[self.sp+3]] = p1 * p2

                self.sp += 4
                continue

            if inst == 3:
                #inp = int(input("input: "))
                inp = self.inputs.pop()
                print('input', inp)

                self.prog[self.prog[self.sp+1]] = inp
                self.sp += 2
                continue

            if inst == 4:
                val = get_val(mode[2], self.prog[self.sp+1], self.prog)
                print('OUTPUT', val)
                self.sp += 2
                return val
                continue

            if inst == 5:
                p1 = get_val(mode[2], self.prog[self.sp+1], self.prog)
                if p1 != 0:
                    self.sp = get_val(mode[1], self.prog[self.sp+2], self.prog)
                else:
                    self.sp += 3
                continue

            if inst == 6:
                p1 = get_val(mode[2], self.prog[self.sp+1], self.prog)
                if p1 == 0:
                    self.sp = get_val(mode[1], self.prog[self.sp+2], self.prog)
                else:
                    self.sp += 3
                continue

            if inst == 7:
                p1 = get_val(mode[2], self.prog[self.sp+1], self.prog)
                p2 = get_val(mode[1], self.prog[self.sp+2], self.prog)
                if p1 < p2:
                    self.prog[self.prog[self.sp+3]] = 1
                else:
                    self.prog[self.prog[self.sp+3]] = 0
                self.sp += 4
                continue

            if inst == 8:
                p1 = get_val(mode[2], self.prog[self.sp+1], self.prog)
                p2 = get_val(mode[1], self.prog[self.sp+2], self.prog)
                if p1 == p2:
                    self.prog[self.prog[self.sp+3]] = 1
                else:
                    self.prog[self.prog[self.sp+3]] = 0
                self.sp += 4
                continue

            if inst == 99:
                print('HALT')
                # exit(0)
                return None
                break

            else:
                print('ERROR')
                exit(0)


a = [5, 6, 7, 8, 9]


results = []
for s in list(set(itertools.permutations(a))):
    amps = [pc(or_opcodes.copy()), pc(or_opcodes.copy()), pc(
        or_opcodes.copy()), pc(or_opcodes.copy()), pc(or_opcodes.copy())]

    # Set phases
    for num, i in enumerate(s):
        amps[num].push(i)

    val = 0
    cont = True
    count = 0
    while cont:
        count += 1
        print('count', count)
        for num, i in enumerate(s):
            amps[num].push(val)
            val_l = amps[num].run()
            if val_l is None:
                cont = False
                break
            val = val_l

    print(s, val)
    results.append((s, val))

print(max(results, key=lambda x: x[1]))
