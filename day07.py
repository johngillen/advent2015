f = open("day07.input")
lines = [line.rstrip() for line in f.readlines()]

circuit = {}

def evaluate(wire):
    value = 0

    # if wire is int or wire is simple assignment to int
    if type(wire) == int:
        value = wire
    elif type(circuit[wire]) == int:
        value = circuit[wire]
    
    # bitwise operations
    elif 'AND'      in circuit[wire]:
        value = evaluate(circuit[wire][0]) &  evaluate(circuit[wire][2])
    elif 'OR'       in circuit[wire]:
        value = evaluate(circuit[wire][0]) |  evaluate(circuit[wire][2])
    elif 'LSHIFT'   in circuit[wire]:
        value = evaluate(circuit[wire][0]) << evaluate(circuit[wire][2])
    elif 'RSHIFT'   in circuit[wire]:
        value = evaluate(circuit[wire][0]) >> evaluate(circuit[wire][2])
    elif 'NOT'      in circuit[wire]:
        value = ~ evaluate(circuit[wire][1]) & 0xFFFF # enforce 16bit

    # if wire is simple assignment to another wire
    else:
        value = evaluate(circuit[wire][0])
    
    circuit[wire] = value # memoization
    return value

def convert(word):
    try:
        return int(word)
    except ValueError:
        return word

def reset():
    for line in lines:
        words = list(map(convert, line.split()))
        circuit[words[-1]] = words[:-2]

reset()
part1 = evaluate('a')
reset()
circuit['b'] = part1
part2 = evaluate('a')

print('part 1: ' + str(part1))
print('part 2: ' + str(part2))
