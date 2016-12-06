import re

class Room:
    r = re.compile('^([a-zA-Z-]+)-(\d+)\[([a-zA-Z]+)\]$')

    def __init__(self, s):
        mo = self.r.match(s)
        self.letters = mo.group(1)
        self.sector = int(mo.group(2))
        self.csum = mo.group(3)

    def shiftc(self, c, cnt):
        return chr(int((ord(c) - ord('a') + cnt) % 26) + ord('a'))

    def decript(self):
        return ''.join(map(lambda x: ' ' if x == '-' else self.shiftc(x, self.sector), self.letters))

    def compare(self, x, y):
        if x['c'] == y['c'] and x['l'] == y['l']:
            return 0
        elif x['c'] < y['c'] or (x['c'] == y['c'] and x['l'] > y['l']):
            return 1
        else:
            return -1

    def is_valid(self):
        lcount = {}
        letters = filter(lambda x: x != '-', self.letters)
        for ltr in letters:
            lcount[ltr] = lcount[ltr] + 1 if ltr in lcount else 1
        larr = []
        for ltr in lcount:
            larr.append({ 'l': ltr, 'c': lcount[ltr]})
        return ''.join(map(lambda x: x['l'], sorted(larr, cmp=self.compare)))[0:5] == self.csum

with open('input.txt', 'r') as f:
    rooms = [Room(x) for x in f.read().splitlines()]

#first part
print 'sector sum: ' + str(reduce(lambda x, y: x + y.sector if y.is_valid() else x + 0, rooms, 0))

#second part
for room in rooms:
    if re.search('^.*north.*pole.*$', room.decript(), re.IGNORECASE):
        print 'room sector: ' + str(room.sector) + '\tdecripted: ' + room.decript()

