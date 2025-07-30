# rows numbered 0 to 127
rows = [x for x in range(128)]

# cols numbered 0 to 7
cols = [x for x in range(8)]

boarding_passes_ids = [x for x in range(127*8 + 8)]
boarding_passes = []
with open('input.txt') as f:
    for line in f:
        boarding_passes.append(line.strip())

start_row = 0
start_col = 0
end_row = 127
end_col = 7
high_seat_id = 0
for boarding_pass in boarding_passes:
    for char in boarding_pass:
        if char == 'F':
            end_row = (end_row + start_row) // 2
        if char == 'B':
            start_row = (end_row + start_row) // 2 + 1
        if char == 'L':
            end_col = (end_col + start_col) // 2
        if char == 'R':
            start_col = (end_col + start_col) // 2 + 1

    if start_col != end_col:
        print("col mismatch")
    if start_row != end_row:
        print("row mismatch")

    seat_id = (end_row * 8) + start_col
    boarding_passes_ids.pop(boarding_passes_ids.index(seat_id))
    if seat_id > high_seat_id:
        high_seat_id = seat_id

    start_row = 0
    end_row = 127
    start_col = 0
    end_col = 7

print(high_seat_id)

# Calculate my seat (0 to 1024)
print(boarding_passes_ids)
for idx in range(len(boarding_passes_ids)):
    if boarding_passes_ids[idx] + 1 != boarding_passes_ids[idx + 1]:
        print(boarding_passes_ids[idx + 1])
        break

