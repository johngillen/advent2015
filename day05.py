import enum


f = open("day05.input")
lines = f.readlines()

nice = 0

for line in lines:
    naughty = False

    vowels = 0
    consecutive = False
    for i, character in enumerate(line):
        if 'aeiou'.find(character) != -1:
            vowels += 1
        
        if i < len(line) - 1 and line[i] == line[i + 1]:
            consecutive = True
        
    if not naughty and vowels < 3:
        naughty = True

    if not naughty and not consecutive:
        naughty = True

    if not naughty and line.find('ab') != -1:
        naughty = True
    if not naughty and line.find('cd') != -1:
        naughty = True
    if not naughty and line.find('pq') != -1:
        naughty = True
    if not naughty and line.find('xy') != -1:
        naughty = True

    if not naughty:
        nice += 1

print("part 1: " + str(nice))
