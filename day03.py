from enum import unique


f = open("input/day03.txt")
lines = f.readlines()

houses = [(0, 0)]
santa = [(0, 0)]
robosanta = [(0, 0)]

for line in lines:
    counter = 0
    for character in line:
        if character == '<':
            houses.append((houses[-1][0] - 1, houses[-1][1]))
            if counter % 2 == 0:
                santa.append((santa[-1][0] - 1, santa[-1][1]))
            else:
                robosanta.append((robosanta[-1][0] - 1, robosanta[-1][1]))
        if character == '>':
            houses.append((houses[-1][0] + 1, houses[-1][1]))
            if counter % 2 == 0:
                santa.append((santa[-1][0] + 1, santa[-1][1]))
            else:
                robosanta.append((robosanta[-1][0] + 1, robosanta[-1][1]))
        if character == 'v':
            houses.append((houses[-1][0], houses[-1][1] - 1))
            if counter % 2 == 0:
                santa.append((santa[-1][0], santa[-1][1] - 1))
            else:
                robosanta.append((robosanta[-1][0], robosanta[-1][1] - 1))
        if character == '^':
            houses.append((houses[-1][0], houses[-1][1] + 1))
            if counter % 2 == 0:
                santa.append((santa[-1][0], santa[-1][1] + 1))
            else:
                robosanta.append((robosanta[-1][0], robosanta[-1][1] + 1))
        
        counter += 1

houses = len(list(set(houses)))
santa = len(list(set(santa + robosanta)))

print("part 1: " + str(houses))
print("part 2: " + str(santa))
