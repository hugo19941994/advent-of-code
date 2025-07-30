# works, but it's quite ugly...

from math import sqrt
from copy import deepcopy

class Image:
    def __init__(self, tile):
        self.tile = tile

    def rotate(self):
        # rotates anticlockwise
        self.tile = [[self.tile[j][i] for j in range(len(self.tile))] for i in range(len(self.tile) - 1, -1, -1)]

    def flip(self):
        # reverses all rows (horizontal flip)
        self.tile = [[self.tile[i][j] for j in range(len(self.tile) - 1, -1, -1)] for i in range(len(self.tile))]

    def to_string(self):
        string = ''
        for row in self.tile:
            for char in row:
                string += char
            string += '\n'

class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile  # 2d array

        # outer border attributes are filled by the Board
        self.outer_borders = []

    @property
    def is_border(self):
        return len(self.outer_borders) > 0

    @property
    def is_corner(self):
        return len(self.outer_borders) == 2

    def rotate(self):
        # rotates anticlockwise
        self.tile = [[self.tile[j][i] for j in range(len(self.tile))] for i in range(len(self.tile) - 1, -1, -1)]
        # rotate outer borders too
        new_borders = []
        for border in self.outer_borders:
            if border == 'top_row':
                new_borders.append('left_col')
            elif border == 'left_col':
                new_borders.append('bottom_row')
            elif border == 'bottom_row':
                new_borders.append('right_col')
            elif border == 'right_col':
                new_borders.append('top_row')
        self.outer_borders = new_borders

    def flip(self):
        old_outer_borders = self.outer_borders.copy()
        # reverses all rows (horizontal flip)
        self.tile = [[self.tile[i][j] for j in range(len(self.tile) - 1, -1, -1)] for i in range(len(self.tile))]
        self.outer_borders = old_outer_borders
        # flip borders
        if 'left_col' in self.outer_borders:
            self.outer_borders.append('right_col')
            self.outer_borders.remove('left_col')
        elif 'right_col' in self.outer_borders:
            self.outer_borders.append('left_col')
            self.outer_borders.remove('right_col')

    def top_row(self):
        return self.tile[0]

    def bottom_row(self):
        return self.tile[-1]

    def left_col(self):
        return [x[0] for x in self.tile]

    def right_col(self):
        return [x[-1] for x in self.tile]

    def borders(self):
        return [
            ('top_row', self.top_row()),
            ('right_col', self.right_col()),
            ('bottom_row', self.bottom_row()),
            ('left_col', self.left_col())
        ]


class Board:
    def __init__(self):
        self.tiles = {}
        self.places = {}

    def add_tile(self, tile: Tile):
        self.tiles[tile.id] = tile

    def place(self, id, coord):
        self.places[coord] = id

    def border_tiles(self):
        return (x for x in self.tiles.values() if x.is_border)

    def border_tiles_free(self):
        return (x for x in self.border_tiles() if x.id not in (y for y in self.places.values()))

    def inner_tiles(self):
        return (x for x in self.tiles.values() if not x.is_border)

    def inner_tiles_free(self):
        return (x for x in self.inner_tiles() if x.id not in (y for y in self.places.values()))

    def calculate_border_tiles(self):
        # the outer borders have no coincidences with any inner border
        for a in self.tiles.values():
            # go border to border instead of using any to store which "border" is in the outer border
            for border_name, border in a.borders():
                found = False
                for b in [x for x in self.tiles.values() if x != a]:  # exclude the "a" tile
                    for _ in range(4): # flips change depending on the current rotation...
                        b.rotate()
                        for _ in range(2):  # flipped & non-flipped
                            b.flip()
                            if border in [x[1] for x in b.borders()]:
                                found = True
                                break
                    if found:
                        break

                if not found:
                    a.outer_borders.append(border_name)
                    if len(a.outer_borders) > 2:
                        print(a)
                    assert not len(a.outer_borders) > 2  # sanity check

        # sanity checks
        assert (len([x for x in self.tiles.values() if x.is_border]) == sqrt(len(self.tiles)) * 4) - 4
        for t in self.tiles.values():
            if t.is_border:
                assert len(t.outer_borders) in (1, 2)


board = Board()
tiles = {}
with open('input.txt') as f:
    # to store current tile
    tile_buffer = []
    tile_num = None

    while (line := f.readline()):
        line = line.strip()
        if 'Tile' in line:
            tile_num = int(line.replace('Tile ', '').replace(':', ''))
            continue

        if len(line) == 0:
            # add current tile to buffer
            if len(tile_buffer) > 0:
                board.add_tile(Tile(tile_num, tile_buffer))

            # reset buffer
            tile_buffer = []
            continue

        tile_buffer.append(list(line.strip()))

# all the tiles are now loaded in the board
# let's find all the border tiles
board.calculate_border_tiles()

# find corners (only thing needed for part 1)
total = 1
for tile in [x for x in board.tiles.values() if x.is_border]:
    if tile.is_corner:
        total *= tile.id
print(f'Part 1: {total}')

# now place tiles in grid
# let's start by putting the tiles in the lower row
corner_1 = [x for x in board.tiles.values() if x.is_corner][0]
for x in range(int(sqrt(len(board.tiles)))):
    coord = (x, 0)
    if x == 0:
        # rotate tile until borders are in left col and bottom row
        for _ in range(4):
            corner_1.rotate()
            if 'bottom_row' in corner_1.outer_borders and 'left_col' in corner_1.outer_borders:
                board.place(corner_1.id, coord)
                break
        if board.places.get(coord) is None:
            raise Exception(f'corner 1 {corner_1.id} could not be rotated correctly')
        continue

    anchor = (x - 1, 0)  # reference tile is the one on the left
    anchor_tile = board.tiles[board.places[anchor]]

    for tile in board.border_tiles_free():
        for _ in range(2):
            tile.flip()
            for _ in range(4):
                tile.rotate()
                if 'bottom_row' not in tile.outer_borders:
                    continue
                if tile.left_col() == anchor_tile.right_col():
                    board.place(tile.id, coord)
                    break
            if coord in board.places:
                break
        if coord in board.places:
            break

    # sanity check
    if coord not in board.places:
        raise Exception(f'tile for coord {coord} not found')
    if x == int(sqrt(len(board.tiles))):
        assert board.tiles[board.places[coord]].is_corner

# now the left column
for y in range(1, int(sqrt(len(board.tiles)))):
    coord = (0, y)
    anchor = (0, y - 1)  # reference tile is the one on the left
    anchor_tile = board.tiles[board.places[anchor]]

    for tile in board.border_tiles_free():
        for _ in range(4):
            tile.rotate()
            for _ in range(2):
                tile.flip()
                if tile.bottom_row() == anchor_tile.top_row():
                    board.place(tile.id, coord)
                    break
            if coord in board.places:
                break
        if coord in board.places:
            break
    # sanity check
    if coord not in board.places:
        raise Exception(f'tile for coord {coord} not found')
    if y == int(sqrt(len(board.tiles))):
        assert board.tiles[board.places[coord]].is_corner

# now the right column
for y in range(1, int(sqrt(len(board.tiles)))):
    coord = (int(sqrt(len(board.tiles))) - 1, y)
    anchor = (int(sqrt(len(board.tiles))) - 1, y - 1)  # reference tile is the one on the left
    anchor_tile = board.tiles[board.places[anchor]]

    for tile in board.border_tiles_free():
        for _ in range(4):
            tile.rotate()
            for _ in range(2):
                tile.flip()
                if tile.bottom_row() == anchor_tile.top_row():
                    board.place(tile.id, coord)
                    break
            if coord in board.places:
                break
        if coord in board.places:
            break
    # sanity check
    if coord not in board.places:
        raise Exception(f'tile for coord {coord} not found')
    if y == int(sqrt(len(board.tiles))):
        assert board.tiles[board.places[coord]].is_corner

# now the top row
for x in range(1, int(sqrt(len(board.tiles))) - 1): # first two (corners) are already placed
    coord = (x, int(sqrt(len(board.tiles))) - 1)
    anchor = (x-1, int(sqrt(len(board.tiles))) - 1)  # reference tile is the one on the left
    anchor_tile = board.tiles[board.places[anchor]]

    for tile in board.border_tiles_free():
        for _ in range(4):
            tile.rotate()
            for _ in range(2):
                tile.flip()
                if tile.left_col() == anchor_tile.right_col():
                    board.place(tile.id, coord)
                    break
            if coord in board.places:
                break
        if coord in board.places:
            break
    # sanity check
    if coord not in board.places:
        raise Exception(f'tile for coord {coord} not found')
    if x == int(sqrt(len(board.tiles))):
        assert board.tiles[board.places[coord]].is_corner

# now all the border tiles are set
# for each row the rest of the tiles can be set and can be compared with two sides
# in this case left and bottom (as we go from bottom to top. and left to right)

for y in range(1, int(sqrt(len(board.tiles))) - 1):
    for x in range(1, int(sqrt(len(board.tiles))) - 1):
        coord = (x, y)
        anchor_left = (x-1, y)  # reference tile is the one on the left
        anchor_left_tile = board.tiles[board.places[anchor_left]]
        anchor_bottom = (x, y - 1)
        anchor_bottom_tile = board.tiles[board.places[anchor_bottom]]

        for tile in board.inner_tiles_free():
            for _ in range(4):
                tile.rotate()
                for _ in range(2):
                    tile.flip()
                    if tile.left_col() == anchor_left_tile.right_col() and \
                        tile.bottom_row() == anchor_bottom_tile.top_row():
                        board.place(tile.id, coord)
                        break
                if coord in board.places:
                    break
            if coord in board.places:
                break
        # sanity check
        if coord not in board.places:
            raise Exception(f'tile for coord {coord} not found')

# now the board should be assembled
# let's trim the borders of each tile and search sea monsters

# we now know the corners, and the know it's a 12x12 square grid (sqrt(len(tiles))
# the image will be constructed top to bottom, left to right
image = []
for y in range(int(sqrt(len(board.tiles))) - 1, -1, -1):
    for line_num in range(1, 9):  # skip top and bottom row
        line = []
        for x in range(int(sqrt(len(board.tiles)))):
            coord = (x, y)
            tile_id = board.places[coord]
            row = board.tiles[tile_id].tile[line_num][1:-1]  # skip left and tight column
            line.extend(row)
        image.append(line)

# sanity checks
assert len(image) == int(sqrt(len(board.tiles))) * 8
assert len(image[0]) == int(sqrt(len(board.tiles))) * 8

# now the image is assembled and all of the tiles' borders have been removed
# rotate and flip and search for a pattern. if the pattern matches anywhere convert
# coincidences to . (from #) and then count the total number of #
img2 = Image(image)

# sanity check
amount_hash_original = 0
for x in img2.tile:
    for y in x:
        if y == '#':
            amount_hash_original += 1
print('original amount', amount_hash_original)

for _ in range(4):
    img2.rotate()
    for _ in range(2):
        img2.flip()
        img = deepcopy(img2)
        for y in range(len(img.tile) - 2):
            for x in range(len(img.tile) - 19):
                coord = (x, y)
                """
                pattern:
                                  # 
                #    ##    ##    ###
                 #  #  #  #  #  #   
                """
                locs = [(x+18, y),
                        (x, y+1), (x+5, y+1), (x+6, y+1), (x+11, y+1), (x+12, y+1), (x+17, y+1), (x+18, y+1), (x+19, y+1),
                        (x+1, y+2), (x+4, y+2), (x+7, y+2), (x+10, y+2), (x+13, y+2), (x+16, y+2)]
                found = True
                for loc in locs:
                    if img.tile[loc[1]][loc[0]] != '#':
                        found = False
                        break
                if not found:
                    continue
                # found. remove coincidences
                for loc in locs:
                    img.tile[loc[1]][loc[0]] = '.'

        amount_hash = 0
        for x in img.tile:
            for y in x:
                if y == '#':
                    amount_hash += 1
        if amount_hash != amount_hash_original:
            print(f'Part 2: {amount_hash}')
            break
