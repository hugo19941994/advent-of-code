with open('input.txt') as f:
    # Check grid size
    num_cols = len(f.readline()) - 1
    num_rows = sum(1 for line in f) + 1
    print(num_cols)
    print(num_rows)

# initialize a grid of the appropriate size
seats = [[None] * num_cols for _ in range(num_rows)]
seats_upd = [[None] * num_cols for _ in range(num_rows)]

with open('input.txt') as f:
    for x, line in enumerate(f):
        for y, char in enumerate(line):
            if char == '\n':
                continue
            seats[x][y] = char


def filled_seats(x, y):
    count = 0
    for xx in range(-1, 2):
        for yy in range(-1, 2):
            try:
                if xx == 0 and yy == 0:
                    continue
                if x + xx < 0 or y + yy < 0:
                    continue
                if seats[x + xx][y + yy] == '#':
                    count += 1
            except Exception as e:
                #print(e)
                pass
    return count


while True:
    for x, row in enumerate(seats):
        for y, tile in enumerate(row):
            # Floor always stays the same
            if tile == '.':
                seats_upd[x][y] = '.'
                continue

            # check how many seats are empty
            elif tile == 'L':
                if filled_seats(x, y) == 0:
                    seats_upd[x][y] = '#'
                else:
                    seats_upd[x][y] = 'L'
            elif tile == '#':
                if filled_seats(x, y) >= 4:
                    seats_upd[x][y] = 'L'
                else:
                    seats_upd[x][y] = '#'

    if seats_upd == seats:
        count = 0
        for x in seats:
            for y in x:
                if y == '#':
                    count += 1
        print(count)
        exit()

    seats = seats_upd.copy()
    seats_upd = [[None] * num_cols for _ in range(num_rows)]
    """
    for x in seats:
        for y in x:
            print(y, end='')
        print()
    """
