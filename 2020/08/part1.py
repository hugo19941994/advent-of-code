def load_opcodes():
    opcodes = []
    with open('input.txt') as f:
        for line in f:
            opcodes.append(line.split(" "))
    return opcodes


def run_vm(opcodes):
    acc = 0
    i = 0
    i_visited = []
    while True:
        if i in i_visited:
            print(f'{i} already visited - loop detected')
            print(acc)
            return
        i_visited.append(i)
        try:
            opcode = opcodes[i]
        except Exception as e:
            print(f'{e} error')
            print(acc)
            return
        if opcode[0] == 'acc':
            acc += int(opcode[1])
            i += 1
        if opcode[0] == 'jmp':
            i += int(opcode[1])
        if opcode[0] == 'nop':
            i += 1


def main():
    opcodes = load_opcodes()
    run_vm(opcodes)

main()