f = open('input/day14.txt')
lines = [line.rstrip() for line in f.readlines()]

class reindeer:
    score = 0
    def __init__(self, name, speed, sprint, rest) -> None:
        self.name = name
        self.speed = speed
        self.sprint = sprint
        self.rest = rest
    def distance(self, time):
        realtime, re = divmod(time, self.sprint + self.rest)
        return (realtime * self.sprint * self.speed) + \
               (min(self.sprint, re) * self.speed)

pack = []

for line in lines:
    line = line.split()
    a = line[0]
    b = int(line[3])
    c = int(line[6])
    d = int(line[13])
    pack.append(reindeer(a, b, c, d))

def race(time):
    results = {}

def score(time):
    for i in range(1, time + 1):
        lead = max(deer.distance(i) for deer in pack)
        for deer in pack:
            if deer.distance(i) == lead:
                deer.score += 1

part1 = max(deer.distance(2503) for deer in pack)
score(2503)
part2 = max(deer.score for deer in pack)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
