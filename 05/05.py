import md5

input = 'ugkcyxxp'

i = 0
cnt = 0
psw1 = ''
psw2 = []

while cnt < 8:
    hd = md5.new(input + str(i)).hexdigest()
    if hd[0:5] == '00000':
        if len(psw1) < 8:
            psw1 = psw1 + hd[5:6]
        pos = int(hd[5:6], 16)
        val = hd[6:7]
        if pos < 8 and not filter(lambda x: x['pos'] == pos, psw2):
            psw2.append({ 'pos': pos, 'val': val})
            cnt = cnt + 1
    i = i + 1

print 'password 1: ' + psw1
print 'password 2: ' + ''.join(map(lambda x: x['val'], sorted(psw2, key=lambda x: x['pos'])))

