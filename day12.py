import re

f = open("input/day12.txt")
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

for line in lines:
    for n in re.findall(r'-?\d*', line):
        part1 += int(n) if n != '' else 0

print(f'part 1: {part1}')
print(f'part 2: {part2}')
