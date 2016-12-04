import re

r = re.compile('^\s*(\d*)\s*(\d*)\s*(\d*)\s*$')

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_valid(self):
        arr = sorted([self.a, self.b, self.c])
        return (arr[0] + arr[1]) > arr[2]

#first part
ts = []
with open('input.txt', 'r') as f:
    ts = [Triangle(int(x.group(1)), int(x.group(2)),int(x.group(3))) for x in [r.match(x) for x in f.read().splitlines()]]

print 'triangles: ' + str(len(ts)) + '\tvalid: ' + str(len(filter(lambda x: x.is_valid(), ts)))

#second part
lines = []
ts = []
with open('input.txt', 'r') as f:
     lines = [[int(x.group(1)), int(x.group(2)),int(x.group(3))] for x in [r.match(x) for x in f.read().splitlines()]]

if len(lines) % 3:
    print 'invalid number of triangles in input'
    exit(1)

for i in range(0, len(lines)):
    if i % 3 == 0:
        ts.append(Triangle(lines[i][0], lines[i+1][0], lines[i+2][0]))
        ts.append(Triangle(lines[i][1], lines[i+1][1], lines[i+2][1]))
        ts.append(Triangle(lines[i][2], lines[i+1][2], lines[i+2][2]))

print 'triangles: ' + str(len(ts)) + '\tvalid: ' + str(len(filter(lambda x: x.is_valid(), ts)))