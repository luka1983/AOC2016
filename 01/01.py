import math

dirs = []
with open('input.txt', 'r') as f:
    dirs = map(lambda x: {'m': int(x[1:]), 'dc': math.pi/2 if x[0] == 'L' else -math.pi/2 }, str.split(f.read(), ', '))

# first part
x = 0
y = 0
d = math.pi

for dir in dirs:
    d = d + dir['dc']
    x = x + int(round(dir['m'] * math.cos(d)))
    y = y + int(round(dir['m'] * math.sin(d)))

print 'dist: ' + str(int(math.fabs(x) + math.fabs(y)))

# second part
x = 0
y = 0
d = math.pi
pos = {}
found = False

for dir in dirs:
    d = d + dir['dc']
    dx = int(round(dir['m'] * math.cos(d)))
    dy = int(round(dir['m'] * math.sin(d)))
    ddx = int(round(dx / math.fabs(dx))) if dx != 0 else 0
    ddy = int(round(dy / math.fabs(dy))) if dy != 0 else 0
    lim = int(math.fabs(dx)) if dx != 0 else int(math.fabs(dy))

    for i in range(0, lim):
        x = x + ddx
        y = y + ddy
        s = 'x' + str(x) + 'y' + str(y)
        if s in pos:
            found = True
            break
        pos[s] = True

    if found:
        break

if found:
    print 'dist: ' + str(int(math.fabs(x) + math.fabs(y)))
else:
    print 'not found'