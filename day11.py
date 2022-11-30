import re

f = open('input/day11.txt')
input = f.readline().strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
straights = list(zip(alphabet, alphabet[1:], alphabet[2:]))
for i in range(len(straights)):
    straights[i] = ''.join(straights[i])

def increment(password):
    password = [ord(c) for c in password]
    for i in range(len(password) - 1, 0 - 1, -1):
        password[i] += 1
        if password[i] <= ord('z'):
            break
        else:
            password[i] = ord('a')
    password = [chr(c) for c in password]
    return ''.join(password)

def nextpass(password):
    password = password
    valid = False
    while not valid:
        password = increment(password)

        for straight in straights:
            if straight in password:
                valid = True

        for i in 'iol':
            if i in password:
                valid = False

        if len(re.findall(r'(\w)\1', password)) < 2:
            valid = False
    return password

part1 = nextpass(input)
part2 = nextpass(part1)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
