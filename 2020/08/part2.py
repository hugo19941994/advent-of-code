import copy

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
        # check infinite loops
        if i in i_visited:
            #print(f'{i} already visited - loop detected')
            #print(acc)
            return
        i_visited.append(i)

        # check program termination
        try:
            opcode = opcodes[i]
        except Exception as e:
            #print(f'{e} error')
            #print('finished execution')
            print(acc)
            exit()

        # execute opcodes
        if opcode[0] == 'acc':
            acc += int(opcode[1])
            i += 1
        if opcode[0] == 'jmp':
            i += int(opcode[1])
        if opcode[0] == 'nop':
            i += 1


def main():
    opcodes = load_opcodes()
    # fix the corrupted bootrom
    # exchange one nop for jmp or jmp to nop
    for i in range(len(opcodes)):
        mod_opcodes = copy.deepcopy(opcodes)
        if mod_opcodes[i][0] == 'nop':
            mod_opcodes[i][0] = 'jmp'
        elif mod_opcodes[i][0] == 'jmp':
            mod_opcodes[i][0] = 'nop'
        else:
            continue
        run_vm(mod_opcodes)
    print('bootrom not fixed')


main()
# 759 too low