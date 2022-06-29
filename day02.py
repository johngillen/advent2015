f = open("input/day02.input")
lines = f.readlines()

paper = 0
ribbon = 0

for line in lines:
    l, w, h = [int(i) for i in line.rstrip().split('x')]
    
    faces = (l * w, l * h, w * h)
    trim = sorted(faces)[0]
    faces = sum(2 * faces)

    paper += faces + trim
    ribbon += sum(sorted([l, w, h])[:-1]) * 2 + (l * w * h)

print("part 1: " + str(paper))
print("part 2: " + str(ribbon))
