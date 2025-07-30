def load_grid():
    # Check grid size
    with open('input.txt') as f:
        num_cols = len(f.readline()) - 1
        num_rows = sum(1 for line in f) + 1

    # initialize a grid of the appropriate size
    forest = [[None] * num_cols for _ in range(num_rows)]
    # load input into grid
    with open('input.txt') as f:
        for x, line in enumerate(f):
            for y, char in enumerate(line):
                if char == '\n':
                    break
                forest[x][y] = char
    return forest


def count_trees(forest, col_step, row_step):
    i, j, trees = 0, 0, 0
    while i < len(forest):
        # col pattern repeats indefinately
        if forest[i][j % len(forest[i])] == '#':
            trees += 1
        i += row_step
        j += col_step
    return trees


def main():
    forest = load_grid()

    # Part 1
    # Right 3, down 1.
    print(count_trees(forest, 3, 1))

    # Part 2
    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    steps = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    accumulator = 1
    for values in steps:
        accumulator *= count_trees(forest, values[0], values[1])
    print(accumulator)

main()