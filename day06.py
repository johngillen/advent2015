f = open("input/day06.txt")
lines = [line.rstrip() for line in f.readlines()]

lit = 0
brightness = 0

lights = [[0] * 1000 for i in range(1000)]
newlights = [[0] * 1000 for i in range(1000)]

for line in lines:
    line = line.split()

    if line[0] == 'turn':
        coordsA = [int(num) for num in line[2].split(',')]
        coordsB = [int(num) for num in line[4].split(',')]

        for i in range(coordsA[0], coordsB[0] + 1):
            for j in range(coordsA[1], coordsB[1] + 1):
                lights[j][i] = 1 if line[1] == 'on' else 0
                newlights[j][i] += 1 if line[1] == 'on' else -1
                if newlights[j][i] < 0: newlights[j][i] = 0
    
    if line[0] == 'toggle':
        coordsA = [int(num) for num in line[1].split(',')]
        coordsB = [int(num) for num in line[3].split(',')]
        
        for i in range(coordsA[0], coordsB[0] + 1):
            for j in range(coordsA[1], coordsB[1] + 1):
                lights[j][i] += 1 if lights[j][i] == 0 else -1
                newlights[j][i] += 2

for i in range(len(lights)):
    for j in range(len(lights[0])):
        lit += lights[j][i]

for i in range(len(newlights)):
    for j in range(len(newlights[0])):
        brightness += newlights[j][i]
        

print("part 1: " + str(lit))
print("part 2: " + str(brightness))
