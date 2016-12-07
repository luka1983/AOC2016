def mapd(d):
    arr = []
    for ltr in d:
        arr.append({ 'ltr': ltr, 'cnt': d[ltr]})
    return arr
        
def mostFreq(d):
    return sorted(mapd(d), key=lambda x: x['cnt'], reverse=True)[0]['ltr']

def leastFreq(d):
    return sorted(mapd(d), key=lambda x: x['cnt'])[0]['ltr']

with open('input.txt', 'r') as f:
    msgs = f.read().splitlines()

dist = []
for msg in msgs:
    for i in range(0, len(msg)):
        if len(dist) < i + 1:
            dist.append({})
        dist[i][msg[i]] = dist[i][msg[i]] + 1 if msg[i] in dist[i] else 1

print 'first part: ' + ''.join(map(lambda x: mostFreq(x), dist))
print 'second part: ' + ''.join(map(lambda x: leastFreq(x), dist))