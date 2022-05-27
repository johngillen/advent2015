import readline

f = open("day01.input")
lines = f.readlines()

# santa starts at floor 0
floor = 0
basement = 0

for line in lines:
    i = 1
    for character in line:
        if character == '(':
            floor += 1
        else:                   # only other possible character is ')'
            floor += -1
        
        if floor == -1 and basement == 0:
            basement = i
        i += 1

print("part 1: " + str(floor))
print("part 2: " + str(basement))
