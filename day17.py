f = open("input/day17.txt")
lines = [line.rstrip() for line in f.readlines()]

containers = [int(line) for line in lines]

def combos(containers, eggnog):
    from itertools import combinations
    valid = []
    for i in range(1, len(containers)):
        for c in combinations(containers, i):
            if sum(c) == eggnog:
                valid.append(c)
    return valid

valid = combos(containers, 150)

part1 = len(valid)
part2 = sum([1 for c in valid \
    if len(c) == min([len(c) for c in valid])])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
