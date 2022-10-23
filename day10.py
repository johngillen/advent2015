import re

f = open("input/day10.txt")
input = f.readline().strip()

part1 = input
for i in range(40):
    matches = re.finditer(r'(\d)\1*', part1)
    part1 = ''
    for match in matches:
        part1 += str(match.span()[1] - match.span()[0]) + match.group()[0]

part2 = part1
for i in range(10):
    matches = re.finditer(r'(\d)\1*', part2)
    part2 = ''
    for match in matches:
        part2 += str(match.span()[1] - match.span()[0]) + match.group()[0]

part1 = len(part1)
part2 = len(part2)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
