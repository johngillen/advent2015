import re as regex

f = open("input/day05.txt")
lines = f.readlines()

nice = 0
newnice = 0

for line in lines:

    if (len(regex.findall(r'([aeiou])', line)) >= 3 and 
        regex.search(r'(.)\1', line) != None and
        regex.search(r'(ab|cd|pq|xy)', line) == None):
            nice += 1
    
    if (regex.search(r'(.{2}).*\1', line) != None and
        regex.search(r'(.)[^\1]\1', line) != None):
            newnice += 1

print("part 1: " + str(nice))
print("part 2: " + str(newnice))
