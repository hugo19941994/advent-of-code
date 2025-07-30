from collections import defaultdict
from datetime import datetime
start_time = datetime.now()

input = [19, 20, 14, 0, 9, 1]
#input = [0,3,6]
#memory = defaultdict(list) # a bit slower (44 vs 30 seconds)
memory = {}
turn = 0
current_num = -1


def add_to_dict(key, val):
    old_val = memory.get(key)
    if old_val is None:
        memory[key] = (-1, val)
    else:
        memory[key] = (old_val[1], val)


for idx, i in enumerate(input):
    turn += 1
    add_to_dict(i, idx+1)
    #memory[i].append(idx+1)
    current_num = i

# turn 6
while True:
    turn += 1
    if memory[current_num][0] == -1:
        current_num = 0
    else:
        #old_current_num = current_num
        current_num = memory[current_num][1] - memory[current_num][0]
        #memory[old_current_num].pop(0)  # we don't need it anymore

    add_to_dict(current_num, turn)
    #memory[current_num].append(turn)

    if turn == 2020:
        print(current_num)

    # takes a while...
    if turn == 30000000:
        print(current_num)
        end_time = datetime.now()
        print(end_time - start_time)
        exit()
