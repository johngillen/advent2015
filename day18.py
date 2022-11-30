f = open('input/day18.txt')
lines = [line.rstrip() for line in f.readlines()]

grid = [[0] * len(lines) for i in range(len(lines))]
stuckgrid = [[0] * len(lines) for i in range(len(lines))]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[i][j] = 1 if lines[i][j] == '#' else 0
        stuckgrid[i][j] = 1 if lines[i][j] == '#' else 0

def update(grid):
    newgrid = [i.copy() for i in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[i]):
                        continue
                    if x == i and y == j:
                        continue
                    neighbors += grid[x][y]
            if grid[i][j] == 1:
                if neighbors != 2 and neighbors != 3:
                    newgrid[i][j] = 0
            else:
                if neighbors == 3:
                    newgrid[i][j] = 1
    return newgrid

for i in range(100):
    grid = update(grid)

for i in range(100):
    stuckgrid[0][0] = 1
    stuckgrid[0][len(stuckgrid) - 1] = 1
    stuckgrid[len(stuckgrid) - 1][0] = 1
    stuckgrid[len(stuckgrid) - 1][len(stuckgrid) - 1] = 1
    stuckgrid = update(stuckgrid)

stuckgrid[0][0] = 1
stuckgrid[0][len(stuckgrid) - 1] = 1
stuckgrid[len(stuckgrid) - 1][0] = 1
stuckgrid[len(stuckgrid) - 1][len(stuckgrid) - 1] = 1

part1 = sum([sum(i) for i in grid])
part2 = sum([sum(i) for i in stuckgrid])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
