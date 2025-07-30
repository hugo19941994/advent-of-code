from collections import defaultdict

# Build directed graph
graph = defaultdict(list)


class Node:
    def __init__(self, name, amount):
        self.amount = int(amount)
        self.name = name

    def __eq__(self, another):
        return hasattr(another, 'name') and self.name == another.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"({self.name}, {self.amount})"

    def __str__(self):
        return f"({self.name}, {self.amount})"


with open('input2.txt') as f:
    for line in f:
        line = line.strip().split(' => ')
        left = line[0].split(',')
        right = Node(line[1].split()[1], line[1].split()[0])

        graph[right] = [Node(x.split()[1], x.split()[0]) for x in left]

print(graph)
TOTAL = 0
# Might not work if two nodes are the same
generated = defaultdict(int)


# amount is the amount of the parent compound needed
def calculate_ore_amount(node, amount, parent_node=None):
    # To generate parent consume node

    if node.name == 'ORE':
        print('found ore adding ', node.amount)
        #generated[node.name] += node.amount
        return node.amount

    parents = graph[node]
    generated[node.name] += node.amount

    for n in parents:
        print('subtracting ', node.name, ' ', node.amount)
        generated[node.name] -= n.amount
        calculate_ore_amount(n, n.amount)
    return


def print_nodes(node):
    global TOTAL
    find = graph[node]
    print('NODE', node)
    for n in find:
        generated[n.name] += n.amount

        print('FOUND ', n)
        if n == Node('ORE', 0):
            TOTAL += n.amount
        print_nodes(n)
    print()


#print_nodes(Node('FUEL', '1'))
calculate_ore_amount(Node('FUEL', '1'), 1)
# print(TOTAL)

print('More than 33100')
print(generated)
