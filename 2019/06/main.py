from collections import defaultdict

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
for key in graph.keys():
    totals[key] = count_orbits(key)


print(sum(totals.values()))
