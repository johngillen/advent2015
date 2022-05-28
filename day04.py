import hashlib as hash

input = 'yzbqklnj'
adventcoin = hash.md5()

part1 = 0
part2 = 0

while str(adventcoin.hexdigest())[0:6] != '000000':
    part2 += 1
    adventcoin = hash.md5((input + str(part2)).encode())
    if str(adventcoin.hexdigest())[0:5] == '00000' and part1 == 0:
        part1 = part2

print("part 1: " + str(part1))
print("part 2: " + str(part2))
