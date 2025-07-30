import matplotlib.pyplot as plt

with open('input.txt') as f:
    or_opcodes = [int(i) for i in f.read().split(',')]


class pc():
    def __init__(self, program):
        self.sp = 0
        self.relative_base = 0
        self.inputs = []
        self.memory = [0] * 50000

        self.a = True
        self.grid = {}
        self.facing = 'U'
        self.pos = (0, 0)

        # load program into memory
        for i in range(len(program)):
            self.memory[i] = program[i]

    def push(self, inp):
        self.inputs.insert(0, inp)

    def get_val(self, mode, d):
        if mode == "0":
            return self.memory[d]
        elif mode == "1":
            return d
        elif mode == "2":
            return self.memory[d + self.relative_base]
        else:
            print("MODE ERROR")
            exit(0)

    def write_val(self, mode, mem_loc, val):
        if mode == "0":
            self.memory[self.memory[mem_loc]] = val
        elif mode == "1":
            self.memory[mem_loc] = val
        elif mode == "2":
            self.memory[self.memory[mem_loc] + self.relative_base] = val
        else:
            print("MODE ERROR")
            exit(0)

    def run(self):
        while True:
            opcode = str(self.memory[self.sp]).zfill(5)
            mode = opcode[:-2]
            inst = int(opcode[-2:])

            if inst == 1:
                p1 = self.get_val(mode[2], self.memory[self.sp+1])
                p2 = self.get_val(mode[1], self.memory[self.sp+2])
                self.write_val(mode[0], self.sp + 3, p1 + p2)

                self.sp += 4
                continue

            if inst == 2:
                p1 = self.get_val(mode[2], self.memory[self.sp+1])
                p2 = self.get_val(mode[1], self.memory[self.sp+2])
                self.write_val(mode[0], self.sp + 3, p1 * p2)

                self.sp += 4
                continue

            if inst == 3:
                #inp = int(input("input: "))
                #inp = self.inputs.pop()
                #print('input', inp)
                if len(self.inputs) != 0:
                    inp = self.inputs.pop()
                else:
                    try:
                        inp = self.grid[self.pos]
                    except Exception:
                        inp = 0


                self.write_val(mode[2], self.sp+1, inp)
                self.sp += 2
                continue

            if inst == 4:
                val = self.get_val(mode[2], self.memory[self.sp+1])
                #print('OUTPUT', val)
                # color
                if self.a:
                    self.grid[self.pos] = val

                # dir
                else:
                    # 0 left
                    # 1 right
                    if val == 0:
                        if self.facing == 'U':
                            self.facing = 'L'
                        elif self.facing == 'L':
                            self.facing = 'D'
                        elif self.facing == 'R':
                            self.facing = 'U'
                        elif self.facing == 'D':
                            self.facing = 'R'
                    elif val == 1:
                        if self.facing == 'U':
                            self.facing = 'R'
                        elif self.facing == 'R':
                            self.facing = 'D'
                        elif self.facing == 'D':
                            self.facing = 'L'
                        elif self.facing == 'L':
                            self.facing = 'U'

                    if self.facing == 'U':
                        self.pos = (self.pos[0], self.pos[1] + 1)
                    if self.facing == 'D':
                        self.pos = (self.pos[0], self.pos[1] - 1)
                    if self.facing == 'L':
                        self.pos = (self.pos[0] - 1, self.pos[1])
                    if self.facing == 'R':
                        self.pos = (self.pos[0] + 1, self.pos[1])

                self.a = not self.a
                self.sp += 2
                #return val
                continue

            if inst == 5:
                p1 = self.get_val(mode[2], self.memory[self.sp+1])
                if p1 != 0:
                    self.sp = self.get_val(mode[1], self.memory[self.sp+2])
                else:
                    self.sp += 3
                continue

            if inst == 6:
                p1 = self.get_val(mode[2], self.memory[self.sp+1])
                if p1 == 0:
                    self.sp = self.get_val(mode[1], self.memory[self.sp+2])
                else:
                    self.sp += 3
                continue

            if inst == 7:
                p1 = self.get_val(mode[2], self.memory[self.sp+1])
                p2 = self.get_val(mode[1], self.memory[self.sp+2])
                if p1 < p2:
                    self.write_val(mode[0], self.sp + 3, 1)
                else:
                    self.write_val(mode[0], self.sp + 3, 0)
                self.sp += 4
                continue

            if inst == 8:
                p1 = self.get_val(mode[2], self.memory[self.sp+1])
                p2 = self.get_val(mode[1], self.memory[self.sp+2])
                if p1 == p2:
                    self.write_val(mode[0], self.sp + 3, 1)
                else:
                    self.write_val(mode[0], self.sp + 3, 0)
                self.sp += 4
                continue

            # Adjust relative offset
            if inst == 9:
                p1 = self.get_val(mode[2], self.memory[self.sp+1])
                self.relative_base += p1
                #print('rel base', self.relative_base)
                self.sp += 2
                continue

            if inst == 99:
                print('HALT')
                # part 1
                print(len(self.grid))

                # part 2
                for i in self.grid:
                    if self.grid[i] == 0:
                        f = 'ks'
                    else:
                        f = 'ys'
                    plt.plot(i[0], i[1], f)

                plt.show()
                exit(0)
                #return None
                break

            else:
                print('ERROR')
                exit(0)


p = pc(or_opcodes.copy())
# Remove for part 1
p.push(1)
p.run()
