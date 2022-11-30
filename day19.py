f = open('input/day19.txt')
lines = [line.rstrip() for line in f.readlines()]

replacements = {}
molecule = lines[-1]
molecules = set()
electrons = []

for line in lines:
    if '=>' in line:
        k, v = line.split(' => ')
        if k not in replacements:
            replacements[k] = []
        replacements[k].append(v)

for k, v in replacements.items():
    for i in range(len(molecule)):
        if molecule[i:].startswith(k):
            for r in v:
                molecules.add(molecule[:i] + r + molecule[i + len(k):])

while True:
    for k, v in replacements.items():
        for r in v:
            if r in molecule:
                molecule = molecule.replace(r, k, 1)
                electrons.append(molecule)
    if molecule == 'e':
        break

part1 = len(molecules)
part2 = len(electrons)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
