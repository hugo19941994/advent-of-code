p1_deck_original = []
p2_deck_original = []
# load deck of cards
with open('input.txt') as f:
    deck = None
    for line in f:
        line = line.strip()
        if '' == line:
            continue
        if 'Player 1' in line:
            deck = 1
        elif 'Player 2' in line:
            deck = 2
        else:
            if deck == 1:
                p1_deck_original.append(int(line))
            elif deck == 2:
                p2_deck_original.append(int(line))
print(p1_deck_original)
print(p2_deck_original)

winning_deck = None
p1_deck = p1_deck_original.copy()
p2_deck = p2_deck_original.copy()
while True:
    c1 = p1_deck.pop(0)
    c2 = p2_deck.pop(0)
    if c1 > c2:
        p1_deck.append(c1)
        p1_deck.append(c2)
    elif c2 > c1:
        p2_deck.append(c2)
        p2_deck.append(c1)
    if len(p1_deck) == 0:
        winning_deck = p2_deck
        break
    if len(p2_deck) == 0:
        winning_deck = p1_deck
        break

total = 0
for i in range(len(winning_deck), 0, -1):
    total += i * winning_deck[len(winning_deck) - i]
print('Part 1', total)

# part 2
p1_deck = p1_deck_original.copy()
p2_deck = p2_deck_original.copy()

def recursive_combat(deck1, deck2):
    previous_configurations = []  # can't repeat any configuration inside of a recursive combat (but yes in sub-combats when compared to parents)
    while True:
        if ((deck1.copy(), deck2.copy())) in previous_configurations:
            return 'Player 1'
        else:
            previous_configurations.append((deck1.copy(), deck2.copy()))

        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if len(deck1) >= c1 and len(deck2) >= c2:
            # sub-game
            round_winner = recursive_combat(deck1.copy()[:c1], deck2.copy()[:c2])
            if round_winner == 'Player 1':
                deck1.append(c1)
                deck1.append(c2)
            elif round_winner == 'Player 2':
                deck2.append(c2)
                deck2.append(c1)
        else:
            if c1 > c2:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)

            if len(deck1) == 0:
                return 'Player 2'
            if len(deck2) == 0:
                return 'Player 1'

print()
winner = recursive_combat(p1_deck, p2_deck)
print(winner)
print(p1_deck)
print(p2_deck)
if winner in ('EXIT', 'Player 1'):
    total = 0
    for i in range(len(p1_deck), 0, -1):
        total += i * p1_deck[len(p1_deck) - i]
    print('Part 2', 'player 1', total)
else:
    total = 0
    for i in range(len(p2_deck), 0, -1):
        total += i * p2_deck[len(p2_deck) - i]
    print('Part 2', 'player 2', total)
