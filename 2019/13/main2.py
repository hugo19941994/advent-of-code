import matplotlib.pyplot as plt

with open('input.txt') as f:
    or_opcodes = [int(i) for i in f.read().split(',')]


class pc():
    def __init__(self, program):
        self.sp = 0
        self.relative_base = 0
        self.inputs = []
        self.memory = [0] * 50000

        self.output_buf = []
        self.score = 0
        self.ball_pos = (0, 0)
        self.paddle_pos = (0, 0)

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
            print(inst)

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
                if self.ball_pos[0] < self.paddle_pos[0]:
                    inp = -1
                elif self.ball_pos[0] > self.paddle_pos[0]:
                    inp = 1
                else:
                    inp = 0

                self.write_val(mode[2], self.sp+1, inp)
                self.sp += 2
                continue

            if inst == 4:
                val = self.get_val(mode[2], self.memory[self.sp+1])

                if len(self.output_buf) != 3:
                    self.output_buf.append(val)

                if len(self.output_buf) == 3:
                    x = self.output_buf[0]
                    y = self.output_buf[1]
                    tid = self.output_buf[2]
                    if tid == 4:
                        self.ball_pos = (x, y)
                    if tid == 3:
                        self.paddle_pos = (x, y)

                    if x == -1 and y == 0:
                        print('score', tid)
                        self.score = tid
                    else:
                        pass

                    self.output_buf = []

                print('OUTPUT', val)

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
                print('score', self.score)
                exit(0)
                #return None
                break

            else:
                print('ERROR')
                exit(0)


p = pc(or_opcodes.copy())
p.memory[0] = 2
p.run()
