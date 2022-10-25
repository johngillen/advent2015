from itertools import permutations

f = open("input/day13.txt")
lines = [line.rstrip() for line in f.readlines()]

party = {}

for line in lines:
    line = line.split()
    a = line[0]
    b = line[10][:-1]
    c = int(line[3])
    c = c if line[2] == 'gain' else 0 - c

    if a not in party.keys():
        party[a] = {}
    party[a][b] = c

def seating(members):
    happiness = float('-inf')
    for person in permutations(list(party.keys())):
        n = 0
        for i in range(len(person)):
            n += party[person[i]][person[i - 1]]
            n += party[person[i - 1]][person[i]]
        if happiness < n:
            happiness = n
    return happiness

part1 = seating(party)

party['Me'] = {}
for person in party.keys():
    party['Me'][person] = 0
    party[person]['Me'] = 0

part2 = seating(party)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
