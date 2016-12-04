commands = { 'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1) }

pattern1 = (
    ('1', '2', '3'),
    ('4', '5', '6'),
    ('7', '8', '9')
)

pattern2 = (
    (' ', ' ', '1', ' ', ' '),
    (' ', '2', '3', '4', ' '),
    ('5', '6', '7', '8', '9'),
    (' ', 'A', 'B', 'C', ' '),
    (' ', ' ', 'D', ' ', ' ')
)

def vsum(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def is_valid_pos(pos, pattern):
    if pos[0] < 0 or pos[0] >= len(pattern[0]) or pos[1] < 0 or pos[1] >= len(pattern):
        return False
    if v2dig(pos, pattern) == ' ':
        return False
    return True

def find_position(iset, start, pattern):
    pos = start
    for i in iset:
        pc = vsum(pos, i)
        pos = pc if is_valid_pos(pc, pattern) else pos
    return pos

def v2dig(v, pattern):
    return pattern[v[1]][v[0]]

def find_number(instructions, start, pattern):
    digits = []
    pos = start
    for iset in instructions:
        pos = find_position(iset, pos, pattern)
        digits.append(pos)

    return ''.join(map(lambda x: str(x), map(lambda x: v2dig(x, pattern), digits)))

#MAIN
instructions = []
with open('input.txt', 'r') as f:
    instructions = [map(lambda x: commands[x], line) for line in f.read().splitlines()]

print 'number1: ' + find_number(instructions, (1, 1), pattern1)
print 'number2: ' + find_number(instructions, (0, 2), pattern2)