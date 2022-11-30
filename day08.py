import re as regex

f = open('input/day08.txt')
lines = [line.rstrip() for line in f.readlines()]

code = sum([len(line) for line in lines])

memory = 0
newcode = 0

for line in lines:
    memory += len(line) - 2
    memory -= 1 * len(regex.findall(r'\\[\\']', line))
    memory -= 3 * len(regex.findall(r'\\x[a-f0-9]{2}', line))
    
    newcode += len(line) + 2
    newcode += len(regex.findall(r'[\\\']', line))

print('part 1: ' + str(code - memory))
print('part 2: ' + str(newcode - code))
