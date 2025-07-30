from collections import defaultdict
import queue

# Load file
with open('input.txt') as f:
    orbits = [i.strip().split(')') for i in f]

# Build directed graph
graph = defaultdict(list)
for orbs in orbits:
    # 0 <- 1, 1 orbits 0
    # graph[orbs[0]].append(orbs[1])
    graph[orbs[1]].append(orbs[0])


# count orbits for a node
def count_orbits(node):
    if node not in graph:
        #print(node, 'not in graph')
        return 0

    if node in totals:
        #print(node, totals[node], 'totals precalculated')
        return totals[node]

    count = 0
    for orbit in graph[node]:
        #print('checking internal node', node)
        count += 1
        count += count_orbits(orbit)
    #print(count, 'total for node', node)
    totals[node] = count
    return count


# Store total orbits for each station
totals = {}
totals['COM'] = 0
for key in graph.keys():
    totals[key] = count_orbits(key)


nodes = defaultdict(list)


def BFS(node, obj):
    count = 0
    q = queue.Queue()
    q.put(node)
    discovered = []
    discovered.append('YOU')
    while not q.empty():
        v = q.get()
        count += 1
        print(v, end=" ")
        nodes[node].append(v)
        if v == obj:
            return count
        for i in graph[v]:
            if i not in discovered:
                q.put(i)
                discovered.append(i)


# TODO: ugly, redo
count = BFS('YOU', 'COM')
print(count - 2)
count = BFS('SAN', 'COM')
print(count - 2)

inter = [i for i in set(nodes['YOU']).intersection(nodes['SAN'])]
inter.sort(key=lambda x: totals[x])

total = 0
print(inter)
count = BFS('YOU', inter[-1])
total += count - 2
print(count - 2)
count = BFS('SAN', inter[-1])
total += count - 2
print(count - 2)
print(total)
