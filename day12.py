import re
import json

f = open('input/day12.txt')
lines = [line.rstrip() for line in f.readlines()]
f.seek(0)
input = json.load(f)

part1 = 0
part2 = 0

for line in lines:
    for n in re.findall(r'-?\d*', line):
        part1 += int(n) if n != '' else 0

def traverse(data):
    if type(data) == int:
        return data
    if type(data) == list:
        return sum([traverse(data) for data in data])
    if type(data) != dict:
        return 0
    if 'red' in data.values():
        return 0
    return traverse(list(data.values()))

part2 = traverse(input)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
