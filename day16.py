f = open("input/day16.txt")
lines = [line.rstrip() for line in f.readlines()]

ticker = \
'''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''

mysteryaunt = {k:v for k,v in [line.split(': ') for line in ticker.split('\n')]}
giftaunt = 0
calibratedaunt = 0

for line in lines:
    line = [line.split(': ') for line in line.split(', ')]
    auntnum = int(line[0].pop(0)[4:])
    aunt = {k:v for k,v in line}

    for k, v in line:
        if k in mysteryaunt and aunt[k] != mysteryaunt[k]:
            break
    else:
        giftaunt = auntnum

    for k, v in line:
        if k in mysteryaunt:
            if k in ['cats', 'trees']:
                if aunt[k] <= mysteryaunt[k]:
                    break
            elif k in ['pomeranians', 'goldfish']:
                if aunt[k] >= mysteryaunt[k]:
                    break
            elif aunt[k] != mysteryaunt[k]:
                break
    else:
        calibratedaunt = auntnum if calibratedaunt == 0 else calibratedaunt


part1 = giftaunt
part2 = calibratedaunt

print(f'part 1: {part1}')
print(f'part 2: {part2}')
