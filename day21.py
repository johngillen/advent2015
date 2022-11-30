f = open('input/day21.txt')
lines = [line.rstrip() for line in f.readlines()]

boss = [int(line.split(': ')[-1]) for line in lines]

def battle(damage, defense):
    tmp = boss.copy()
    player = 100
    while True:
        tmp[0] -= max(1, damage - tmp[2])
        if tmp[0] <= 0:
            return True
        player -= max(1, tmp[1] - defense)
        if player <= 0:
            return False

weapons = {
    'Dagger': (8, 4, 0),
    'Shortsword': (10, 5, 0),
    'Warhammer': (25, 6, 0),
    'Longsword': (40, 7, 0),
    'Greataxe': (74, 8, 0)
}
armors = {
    'None': (0, 0, 0),
    'Leather': (13, 0, 1),
    'Chainmail': (31, 0, 2),
    'Splintmail': (53, 0, 3),
    'Bandedmail': (75, 0, 4),
    'Platemail': (102, 0, 5)
}
rings = {
    'None': (0, 0, 0),
    'Damage +1': (25, 1, 0),
    'Damage +2': (50, 2, 0),
    'Damage +3': (100, 3, 0),
    'Defense +1': (20, 0, 1),
    'Defense +2': (40, 0, 2),
    'Defense +3': (80, 0, 3)
}

wins = []
losses = []

for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                if ring1 == ring2 and ring1 != 'None':
                    continue
                cost = sum(i[0] for i in [weapons[weapon], armors[armor], rings[ring1], rings[ring2]])
                damage = sum(i[1] for i in [weapons[weapon], rings[ring1], rings[ring2]])
                defense = sum(i[2] for i in [armors[armor], rings[ring1], rings[ring2]])

                bossko = boss[0] // max(1, damage - boss[2])
                playerko = 100 // max(1, boss[1] - defense)

                if bossko <= playerko:
                    wins.append(cost)
                else:
                    losses.append(cost)
                    

part1 = min(wins)
part2 = max(losses)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
