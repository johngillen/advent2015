from itertools import permutations

f = open('input/day09.txt')
lines = [line.rstrip() for line in f.readlines()]

nodes = []
edges = {}

short = float('inf')
long = float('-inf')

for line in lines:
    a, b, weight = line.split()[::2]
    weight = int(weight)

    nodes.append(a)
    nodes.append(b)
    edges[a + b] = weight
    edges[b + a] = weight

nodes = list(set(nodes))

for attempt in permutations(nodes):
    sum = 0
    for a, b in zip(attempt, attempt[1:]):
        sum += edges[a + b]
    short = sum if sum < short else short
    long = sum if sum > long else long
        
print(f'part 1: {short}')
print(f'part 2: {long}')
