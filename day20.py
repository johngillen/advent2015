f = open('input/day20.txt')
lines = [line.rstrip() for line in f.readlines()]

presents = int(lines[0])

houses = [0] * (presents // 10)
lazyhouses = [0] * presents
house, lazyhouse = 0, 0

for i in range(1, len(houses)):
    for n in range(i, len(houses), i):
        houses[n] += i * 10

for i in range(1, len(lazyhouses)):
    for n in range(i, min(i * 50, len(lazyhouses)), i):
        lazyhouses[n] += i * 11

for i, h in enumerate(houses):
    if h >= presents:
        house = i
        break

for i, h in enumerate(lazyhouses):
    if h >= presents:
        lazyhouse = i
        break

part1 = house
part2 = lazyhouse

print(f'part 1: {part1}')
print(f'part 2: {part2}')
